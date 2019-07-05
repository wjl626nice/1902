from django.shortcuts import render, HttpResponse, redirect
from django.db.models import F
from django.http    import JsonResponse
from utils import verify
from manager.models import *
import hashlib
from django.conf import settings

# Create your views here.

def login(request):
    """
    展示登录页面和处理登录
    :param request:
    :return:
    """
    error = ''
    # print(request.META)
    if request.method == 'POST':
        # 登陆时做检测验证
        adminInfo = _checkLogin(request)  # _checkLogin该名字自定义的，以后所有带下划线的都作为内部调用。
        # 判断返回值是否是 字符串
        if isinstance(adminInfo, str):
            return render(request, 'admin/login.html', {'error': adminInfo})

        # 获取客户端ip
        client_ip = request.META['REMOTE_ADDR']
        # 获取当前时间
        # dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # 更新当前用户的信息  时间格式存在问题
        # Admin.objects.update(id=adminInfo[0]['id'], login_time=dt, login_num=adminInfo[0]['login_num']+1)


        # 记录本次管理员登录日志
        # admin_log = {
        #     "type": '登录',
        #     "title": adminInfo[0]['account'] + '登录',
        #     "user_agent": request.META['HTTP_USER_AGENT'],
        #     'referer': request.META['HTTP_REFERER'],
        #     'add_time': dt,
        #     'ip': client_ip,
        #     'admin_id': adminInfo[0]['id']
        # }
        # 向日志表添加数据
        # Admin_log.objects.create(**admin_log)

        # 登录成功以后把用户信息保存到session中
        request.session['user'] = adminInfo[0]  # adminInfo[0] = {'id':1,'account':'admin',"pwd":''} 字典（用户信息）
        # 登录成功以后跳转
        return redirect('/admin/index/')

    return render(request, 'admin/login.html', {"error": error})

def logOut(request):
    """
    退出登录
    :param request:
    :return:
    """
    # 清空过期的会话
    # request.session.clear()
    # 删除当前的会话
    request.session.delete()
    # 跳转到登录页面
    return redirect('/admin/login/')
def get_verify(request):
    """
    展示验证码
    :param request:
    :return:
    """
    verifys = verify.get_verify()  # 返回的是一个元组，第一个元素是图片内容，第二个图片是验证码
    # print(verifys)
    # 把验证码放入到session中的，等待登录验证
    request.session['verifys'] = verifys[1]
    return HttpResponse(verifys[0], content_type='image/png')

def _checkLogin(request):
    """
    在视图内做登录验证
    :param request: 请求对象
    :return: 字符串|Queryset集合
    """
    # 账号
    account = request.POST.get('account', None).strip()
    # 密码
    pwd = request.POST.get('pwd', None).strip()
    # 验证码
    code = request.POST.get('code').strip()
    # 判断验证码是否存在
    if not code:
        return '验证码不能为空！'
    # 验证码是否输入正确
    if code.lower() != request.session.get('verifys').lower():
        return '验证码不正确，请重新输入！'
    # 账号 或者密码不能为空
    if not account or not pwd:
        return '账号或者密码不能为空！'
    # 从数据库获取指定账号的信息
    adminInfo = Admin.objects.filter(account=account).values('id', 'account', 'pwd', 'login_ip', 'login_num')
    if len(adminInfo) <= 0:
        return '该账号不存在！'
    # 对前台传递过来的密码进行hash
    pwd = settings.SALT + pwd + settings.SALT
    # 参与哈希运算
    md5 = hashlib.md5()
    md5.update(pwd.encode('utf-8'))
    # 获取哈希后的密文
    pwd = md5.hexdigest()
    # 验证密码是否正确
    if adminInfo[0]['pwd'] != pwd:
        return '密码错误！'

    return adminInfo

def index(request):
    """
    后台首页
    :param request:
    :return:
    """
    # 获取后台菜单
    menu = settings.MENU
    # 获取信息传递到模板中
    data = {
        "user": request.session.get('user'),
        "menu": menu
    }
    return render(request, 'admin/index.html', data)

def manager(request):
    """
    管理员列表
    :param request:
    :return:
    """
    # 获取所有管理员信息
    admins = Admin.objects.all().values('id', 'account', 'mobile', 'email', 'state', 'login_time')
    # 获取后台菜单
    menu = settings.MENU
    # 获取信息传递到模板中
    data = {
        "user": request.session.get('user'),
        "menu": menu,
        'admins': admins,
        'count': admins.count()
    }
    return render(request, 'admin/manager.html', data)

def manager_add(request):
    """
    添加管理员页面
    :param request:
    :return:
    """
    if request.is_ajax():
        data = dict(request.POST)
        if data['pwd'] != data['pwd2']:
            return JsonResponse({'msg': '输入的两次密码不一致！', 'code': 1, 'data': []})
        # TODO 待优化
        # 对前台传递过来的密码进行hash
        pwd = settings.SALT + data['pwd'][0] + settings.SALT
        # 参与哈希运算
        md5 = hashlib.md5()
        md5.update(pwd.encode('utf-8'))
        # 获取哈希后的密文
        pwd = md5.hexdigest()
        # 向管理员表添加数据
        # print(data['account'][0], pwd, data['mobile'][0], data['email'][0])
        try:
            Admin.objects.create(account=data['account'][0], pwd=pwd, mobile=data['mobile'][0], email=data['email'][0])
        except Exception as e:
            # 处理异常
            return JsonResponse({'msg': e.args[1], 'code': 2, 'data': []})
        return JsonResponse({'msg': '添加成功！', 'code': 0, 'data': []})
    return render(request, 'admin/manager_add.html')

def manager_change_state(request):
    """
    改变管理员的状态
    :param request:
    :return:
    """
    id = request.GET.get('id')
    # 当修改管理员时 管理员id不能为空
    if not id:
        return JsonResponse({'msg': '请选择要操作的数据！', 'code': 1, 'data': []})
    admin = Admin.objects.get(id=id)
    admin.state = False if admin.state else True
    # 更新当前管理员状态
    admin.save()
    return JsonResponse({'msg': '操作成功', 'code': 0, 'data': [admin.state]})

def manager_del(request):
    id = request.GET.get('id')
    # 管理员id不能为空
    if not id:
        return JsonResponse({'msg': '请选择要操作的数据！', 'code': 1, 'data': []})

    # 删除指定管理员
    Admin.objects.get(id=id).delete()
    return JsonResponse({'msg': '删除成功！', 'code': 0, 'data': []})

def links(request):
    """
    友情链接管理
    :param request:
    :return:
    """
    # 获取后台菜单
    menu = settings.MENU
    # 获取信息传递到模板中
    data = {
        "user": request.session.get('user'),
        "menu": menu,
    }
    return render(request, 'admin/links.html', data)
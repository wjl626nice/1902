import os, re
from django.shortcuts import render, HttpResponse, redirect
from django.db.models import F
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from utils import verify, common
from manager.models import *
import hashlib
from django.conf import settings
# 验证器
from manager.formModel.categoryForm import *
from manager.formModel.articleForm import *


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
    admins = Admin.objects.filter(id__gt=1).values('id', 'account', 'mobile', 'email', 'state', 'login_time')
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
    """
    管理员删除
    :param request:
    :return:
    """
    id = request.GET.get('id')
    # 管理员id不能为空
    if not id:
        return JsonResponse({'msg': '请选择要操作的数据！', 'code': 1, 'data': []})

    # 删除指定管理员
    Admin.objects.get(id=id).delete()
    return JsonResponse({'msg': '删除成功！', 'code': 0, 'data': []})


def manager_edit(request):
    """
    管理员修改
    :param request:
    :return:
    """
    # ajax请求  返回的都是json
    if request.is_ajax():
        id = request.POST.get('id', 0)
        pwd = request.POST.get('pwd', '')
        pwd2 = request.POST.get('pwd2', '')
        email = request.POST.get('email', '')
        mobile = request.POST.get('mobile', '')
        if not id:
            return JsonResponse({'msg': '要修改的管理员id不能为空！', 'code': 2, 'data': []})

        adminInfo = Admin.objects.get(id=id)
        # 只修改管理员信息，不修改密码
        if pwd and pwd2:
            if pwd != pwd2:
                return JsonResponse({'msg': '输入的两次密码不一致！', 'code': 1, 'data': []})
            # TODO 待优化
            # 对前台传递过来的密码进行hash
            pwd = settings.SALT + pwd + settings.SALT
            # 参与哈希运算
            md5 = hashlib.md5()
            md5.update(pwd.encode('utf-8'))
            # 获取哈希后的密文
            pwd = md5.hexdigest()
            # 更新密码
            adminInfo.pwd = pwd

        # 修改邮箱
        if adminInfo.email != email: adminInfo.email = email
        # 修改手机
        if adminInfo.mobile != mobile: adminInfo.mobile = mobile
        # 更新当前管理员信息
        adminInfo.save()
        return JsonResponse({'msg': '操作成功！', 'code': 0, 'data': []})

    # get 请求,返回的都是 html
    id = request.GET.get('id')
    # 管理员id不能为空
    if not id:
        html = common.msg('要修改的管理员id不能为空！')
        return HttpResponse(html)
    try:
        # 获取指定id的管理员信息
        adminInfo = Admin.objects.get(id=id)  # 如果get查询不到数据时 会抛出异常
    except Exception as e:
        html = common.msg('修改异常！')
        return HttpResponse(html)

    return render(request, 'admin/manager_edit.html', {"adminInfo": adminInfo})


def category(request):
    """
    栏目列表
    :param request:
    :return:
    """
    # 获取所有栏目信息
    items = Category.objects.all().values('id', 'cate_name', 'pic', 'num')
    # 获取后台菜单
    menu = settings.MENU
    # 获取信息传递到模板中
    data = {
        "user": request.session.get('user'),
        "menu": menu,
        'items': items,
        'count': items.count()
    }
    return render(request, 'admin/category.html', data)


def category_add(request):
    """
    添加栏目
    :param request:
    :return:
    """
    # 表单验证器   实例化 CategoryForm类返回一个对象
    categoryForm = CategoryForm(request.POST)
    if request.is_ajax():
        # 验证通过时返回的是True
        if categoryForm.is_valid():
            # 根据验证器的字段属性 获取验证成功的数据，返回一个字典
            cate = categoryForm.cleaned_data
            cate['pic'] = request.FILES['pic']
            #  添加栏目信息
            # cate ={
            #     "cate_name": request.POST.get('cate_name'),
            #     "pic": request.FILES['pic'],
            #     "describles": request.POST.get('describles'),
            #     "seo_title": request.POST.get('seo_title'),
            #     "seo_keyword": request.POST.get('seo_keyword'),
            #     "seo_description": request.POST.get('seo_description')
            #
            # }
            Category.objects.create(**cate)
            return JsonResponse({'msg': '添加成功！', 'code': 0, 'data': []})

        return JsonResponse({'msg': '添加失败！', 'code': 1, 'data': []})

    return render(request, 'admin/category_add.html', {'categoryForm': categoryForm})


def category_edit(request):
    # get 请求,返回的都是 html
    id = request.GET.get('id')
    # id不能为空
    if not id:
        html = common.msg('要修改的栏目id不能为空！')
        return HttpResponse(html)

    # 表单验证器   实例化 CategoryForm类返回一个对象
    categoryForm = CategoryForm(request.POST)
    if request.is_ajax():
        if categoryForm.is_valid():
            # 获取验证成功并且要修改的内容
            cate = categoryForm.cleaned_data
            # 追加要修改的图片对象
            if request.FILES.get('pic', None):
                cate['pic'] = request.FILES['pic']
                # 可以删除老的图片
                # # 获取图片的绝对物理路径
                # pic = os.path.join(settings.BASE_DIR, request.POST.get('oldpic'))
                # # 删除物理图片
                # if cate.pic and os.path.isfile(pic): os.remove(pic)

            else:
                del cate['pic']

            # 更新当前栏目信息
            # Category(id=id, **cate) 创建category模型对象
            # update_fields要求更新那些字段
            Category(id=id, **cate).save(update_fields=cate.keys())
            return JsonResponse({'msg': '操作成功！', 'code': 0, 'data': []})
        return JsonResponse({'msg': '操作失败！', 'code': 1, 'data': []})

    try:
        # 获取指定id的栏目信息
        cateInfo = Category.objects.get(id=id)  # 如果get查询不到数据时 会抛出异常
    except Exception as e:
        html = common.msg('修改异常！')
        return HttpResponse(html)

    return render(request, 'admin/category_edit.html', {"cateInfo": cateInfo, "categoryForm": categoryForm})


def category_del(request):
    """
    栏目删除
    :param request:
    :return:
    """
    id = request.GET.get('id')
    # id不能为空
    if not id:
        return JsonResponse({'msg': '请选择要操作的数据！', 'code': 1, 'data': []})

    # 删除指定数据
    cate = Category.objects.get(id=id)
    # 获取图片的绝对物理路径
    pic = os.path.join(settings.BASE_DIR, str(cate.pic))
    # 删除物理图片
    if cate.pic and os.path.isfile(pic): os.remove(pic)
    cate.delete()
    return JsonResponse({'msg': '删除成功！', 'code': 0, 'data': []})


def article(request):
    """
    文章列表
    :param request:
    :return:
    """
    # 获取所有信息
    items = Article.objects.all().values('id', 'title', 'pic', 'flag', 'add_time', 'click', 'admin__account', 'category__cate_name')
    # 获取后台菜单
    menu = settings.MENU
    # 获取信息传递到模板中
    data = {
        "user": request.session.get('user'),
        "menu": menu,
        'items': items,
        'count': items.count()
    }
    return render(request, 'admin/article.html', data)


def article_add(request):
    """
    添加文章
    :param request:
    :return:
    """
    # 表单验证器   实例化 ArticleForm类返回一个对象
    articleForm = ArticleForm(request.POST)
    if request.is_ajax():
        # 验证通过时返回的是True
        if articleForm.is_valid():
            # 根据验证器的字段属性 获取验证成功的数据，返回一个字典
            data = articleForm.cleaned_data
            data['pic'] = request.FILES['pic']

            Article.objects.create(**data)
            return JsonResponse({'msg': '添加成功！', 'code': 0, 'data': []})

        return JsonResponse({'msg': '添加失败！', 'code': 1, 'data': []})
    # 获取所有的栏目
    cates = Category.objects.all().values('id', 'cate_name')
    return render(request, 'admin/article_add.html', {'articleForm': articleForm, 'cates': cates})


def article_edit(request):
    # get 请求,返回的都是 html
    id = request.GET.get('id')
    # id不能为空
    if not id:
        html = common.msg('要修改的栏目id不能为空！')
        return HttpResponse(html)

    # 表单验证器   实例化 CategoryForm类返回一个对象
    categoryForm = CategoryForm(request.POST)
    if request.is_ajax():
        if categoryForm.is_valid():
            # 获取验证成功并且要修改的内容
            cate = categoryForm.cleaned_data
            # 追加要修改的图片对象
            if request.FILES.get('pic', None):
                cate['pic'] = request.FILES['pic']
                # 可以删除老的图片
                # # 获取图片的绝对物理路径
                # pic = os.path.join(settings.BASE_DIR, request.POST.get('oldpic'))
                # # 删除物理图片
                # if cate.pic and os.path.isfile(pic): os.remove(pic)

            else:
                del cate['pic']

            # 更新当前栏目信息
            # Category(id=id, **cate) 创建category模型对象
            # update_fields要求更新那些字段
            Category(id=id, **cate).save(update_fields=cate.keys())
            return JsonResponse({'msg': '操作成功！', 'code': 0, 'data': []})
        return JsonResponse({'msg': '操作失败！', 'code': 1, 'data': []})

    try:
        # 获取指定id的栏目信息
        cateInfo = Category.objects.get(id=id)  # 如果get查询不到数据时 会抛出异常
    except Exception as e:
        html = common.msg('修改异常！')
        return HttpResponse(html)

    return render(request, 'admin/category_edit.html', {"cateInfo": cateInfo, "categoryForm": categoryForm})


def article_del(request):
    """
    栏目删除
    :param request:
    :return:
    """
    id = request.GET.get('id')
    # id不能为空
    if not id:
        return JsonResponse({'msg': '请选择要操作的数据！', 'code': 1, 'data': []})

    # 删除指定数据
    cate = Category.objects.get(id=id)
    # 获取图片的绝对物理路径
    pic = os.path.join(settings.BASE_DIR, str(cate.pic))
    # 删除物理图片
    if cate.pic and os.path.isfile(pic): os.remove(pic)
    cate.delete()
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


@csrf_exempt
def fileupload(request):
    """
    编辑器上传文件
    :param request:
    :return:
    """
    action = request.GET.get('action')
    if action == 'config':
        # 获取编辑器的初始化配置
        with open('static/admin/lib/ueditor/1.4.3/php/config.json') as f:
            config = f.read()
        config = re.sub('\/\*[\s\S]+?\*\/', '', config)

        return HttpResponse(config)
    elif action == 'webupload':
        pass
    print(request.FILES['file'],request.FILES['file'].size)
    return HttpResponse('saa')


from django.shortcuts import render, HttpResponse, redirect
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
    if request.method == 'POST':
        # 登陆时做检测验证
        adminInfo = _checkLogin(request)  # _checkLogin该名字自定义的，以后所有带下划线的都作为内部调用。
        # 判断返回值是否是 字符串
        if isinstance(adminInfo, str):
            return render(request, 'admin/login.html', {'error': adminInfo})
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

def index(request):
    """
    后台首页
    :param request:
    :return:
    """
    # 获取管理员信息
    adminInfo = {
        "user": request.session.get('user')
    }
    return render(request, 'admin/index.html', adminInfo)

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
    adminInfo = Admin.objects.filter(account=account).values('id', 'account', 'pwd')
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
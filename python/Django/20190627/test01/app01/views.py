from django.shortcuts import render, HttpResponse, redirect
from test01 import settings
import datetime

# Create your views here.
def abc(request):
    response = HttpResponse('测试Cookie')
    nowDT = datetime.datetime.now()
    # datetime.timedelta(seconds=20) 20秒的时间间隔
    # nowDT 在当前时间对象上 加 20秒
    nowDT = datetime.timedelta(seconds=20) + nowDT

    # 创建cookie标识
    # max_age (单位秒) 设置Cookie在浏览器的存在时间,  默认情况下 退出浏览器 cookie过期。
    # response.set_cookie('name', 'yakun', max_age=10)
    # expires 未来的时间格式  设置Cookie在浏览器的过期时间
    # response.set_cookie('name', 'yakun', expires=nowDT)
    # path  设置cookie的生效目录 ， 默认情况下种到跟目录也就是紧跟着域名后边的
    # domain 设置主机，把cookie种到对应的主机下边
    response.set_cookie('name', 'yakun', )
    # print(response, type(response))
    return response


def aaa(request):
    # 获取标识
    cookie = request.COOKIES
    print(cookie)
    return HttpResponse('测试获取Cookie' + cookie.get('name', ''))


def login(request):
    # 判断登录
    if request.method == 'POST':
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        # 判断用户名和密码
        if username == 'admin' and pwd == 'admin888':
            # 获取来源页
            referer = request.GET.get('referer')
            if not referer:
                referer = '/index/'
            # 决定跳转页面
            res = redirect(referer)
            print(res, type(res))
            # 登录成功以后种个标识到客户端
            # res.set_cookie('is_login', username)      settings.SALT盐（配置文件中的设置）
            res.set_signed_cookie('is_login', username, settings.SALT)
            return res

    return render(request, 'login.html')

def loginOut(request):
    """
    退出
    :param request:
    :return:
    """
    red = redirect('/login')
    # 删除指定键的Cookie
    red.delete_cookie('is_login')
    return red
"""
检测登录装饰器
"""
def checkLogin(func):
    def inner(request, *args, **kwargs):
        # 如果键不存会报错，索引用try捕获
        try:
            ret = request.get_signed_cookie('is_login', salt=settings.SALT)
        except KeyError as e:
            ret = ''
        if ret:
            return func(request, *args, **kwargs)
        else:
            # request.path_info 获取当前页面的url
            return redirect('/login/?referer='+request.path_info)
    return inner

# def checkLogin(request):
#     username = request.POST.get('username')
#     pwd = request.POST.get('pwd')
#     # 判断用户名和密码
#     if username == 'admin' and pwd == 'admin888':
#         res = redirect('/index/')
#         print(res, type(res))
#         # 登录成功以后种个标识到客户端
#         res.set_cookie('is_login', 1)
#         return res


def index(request):
    # 判断是否登录
    if not request.COOKIES.get('is_login'):
        return redirect('/login/')

    # get_signed_cookie 获取加盐后的值
    return HttpResponse('后台首页！ <a href="/loginOut/">退出</a>' + request.get_signed_cookie('is_login', salt=settings.SALT))

@checkLogin
def article(request):
    # get_signed_cookie 获取加盐后的值
    return HttpResponse('文章列表！' + request.get_signed_cookie('is_login', salt=settings.SALT))

@checkLogin
def manager_admin(request):
    return HttpResponse('管理员管理')

@checkLogin
def category(request):
    return HttpResponse('栏目管理')

@checkLogin
def category_add(request):
    return HttpResponse('栏目添加')
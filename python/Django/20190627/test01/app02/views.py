from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from test01 import settings
# Create your views here.

# @csrf_exempt  # 设置post提交时不进行csrf验证   csrf_protect 设置csrf验证
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
                referer = '/app02/index/'
            # 决定跳转页面
            res = redirect(referer)
            print(res, type(res))
            # 登录成功以后种个标识到客户端
            # 设置session
            request.session['is_login'] = username
            # 设置session的过期时间
            request.session.set_expiry(30 * 60)  # 单位秒
            return res

    return render(request, 'app02/login.html')

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

def index(request):
    # 从请求对象中获取session值
    username = request.session.get('is_login', None)
    print(request.session.__dict__)
    if not username:
        return redirect('/app02/login/')
    return HttpResponse('后台首页，欢迎'+username+'来到后台！')
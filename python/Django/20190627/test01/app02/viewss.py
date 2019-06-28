from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
# 对类中的方法进行装饰
from django.utils.decorators import method_decorator
from django.views import View
from functools import wraps
from django.forms import Form
from django.forms import  fields
from test01 import settings
# Create your views here.

# 定义一个FormModel类，用于验证form表单传递过来的数据
class CLogin(Form):
    username = fields.CharField(
        required=True,
        error_messages={
            'required': '用户名不能为空！'
        }
    )
    pwd = fields.CharField(
        required=True,
        error_messages={
            'required': '密码不能为空！'
        }
    )


def checkLogin(func):
    """
    检测是否登录
    :param func:
    :return:
    """
    @wraps(func)
    def inner(request, *args, **kwargs):
        # 获取当前页面的uri
        referer = request.get_full_path()
        # 在视图函数执行之前，先判断下是否登录
        if request.session.get('is_login'):
            return func(request, *args, **kwargs)
        else:
            return redirect('/app02/clogin/?next_url='+referer)

    return inner


class Login(View):
    def get(self, request):
        """
        处理get请求
        :param request:
        :return:
        """
        return render(request, 'app02/login.html')
    def post(self, request):
        """
        处理post请求，本视图类中就是处理 登录
        :param request:
        :return:
        """
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')

        if username == 'admin' and pwd == 'admin888':
            # 来源页
            referer = request.GET.get('next_url', None)
            if not referer:
                #  没有来源页时 跳转到后台首页
                referer = '/app02/index/'
            # 登录成功，把当前用户的名字保存在session中，后边需要用
            request.session['is_login'] = username

            return redirect(referer)
        # 当登录失败时跳转到登录页面
        return redirect('/app02/login/')

# 后台首页
class Cindex(View):
    def get(self, request):
        # 判断是否登录
        if not request.session.get('is_login'):
            return redirect('/app02/clogin/')
        return HttpResponse('get后台首页！<a href="/app02/cloginOut/">退出</a>')
    def post(self, request):
        return HttpResponse('post后台首页！')

# 栏目管理
class Ccate(View):
    # dispatch 在类视图每次被调用时，先执行
    def dispatch(self, request, *args, **kwargs):
        return super(Ccate, self).dispatch(request, *args, **kwargs)
    # 类装饰器的写法
    @method_decorator(checkLogin)
    def get(self, request):
        return HttpResponse('get栏目管理！')

    @method_decorator(checkLogin)
    def post(self, request):
        return HttpResponse('post后台首页！')

# 文章管理
class Carticle(View):
    # dispatch 在类视图每次被调用时，先执行
    @method_decorator(checkLogin)  # 在get和post方法执行之前执行。所以检查一次登录就行了
    def dispatch(self, request, *args, **kwargs):
        return super(Carticle, self).dispatch(request, *args, **kwargs)
    # 类装饰器的写法
    def get(self, request):
        return HttpResponse('get文章管理！')
    def post(self, request):
        return HttpResponse('post文章管理！')

# 当类的装饰器 在类上边写时 需要添加参数 name
@method_decorator(checkLogin, name='get')
class CloginOut(View):
    """
    退出登录
    """
    def get(self, request):
        request.session.delete()
        return redirect('/app02/clogin/')
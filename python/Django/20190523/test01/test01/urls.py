"""test01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.shortcuts import HttpResponse, render

def zongyuan(request):
    # request 包含请求结构体
    # HttpResponse 自动帮咱们拼接http响应行 和响应头，小括号内的内容是 响应正文
    return HttpResponse('宗元！')
def niuchao(request):
    print(request)
    return HttpResponse('牛超，好好听课！')

def dengshuai(request):
    with open('./templates/admin/dengshuai.html', 'r') as f:
        content = f.read()
    return HttpResponse(content)

def login(request):
    return render(request, 'admin/login.html')

# uri和函数的对应关系，映射
urlpatterns = [
    url(r'^zongyuan', zongyuan),
    url(r'^niuchao', niuchao),
    url(r'^dengshuai', dengshuai),
    url(r'^login', login),
]

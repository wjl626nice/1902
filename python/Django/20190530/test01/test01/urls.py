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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
# 封装了响应行和响应头，只需要在下边调用即可
from django.shortcuts import HttpResponse, render

def xiaoming(request):

    # 自定义获取模板内容
    # with open('./templates/xiaoming.html','r') as f:
    #     ret = f.read()
    # return HttpResponse(ret)

    # 用Django操作模板的方式
    return render(request, 'xiaoming.html')

def niuchao(request):
    print('aaaa')
    return HttpResponse('牛超')

# uri和函数的映射
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('niuchao', niuchao),
    url('xiaoming', xiaoming),
]

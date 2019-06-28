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
from django.urls import path
from app02.views import *
from app02 import viewss, viewsss

app_name = 'app02'
urlpatterns = [
    # 测试session
    path('login/', login),
    path('loginOut/', loginOut),
    path('index/', index),

    # 类视图的
    path('clogin/', viewss.Login.as_view()),
    # 后台首页
    path('cindex/', viewss.Cindex.as_view()),
    # 后台栏目管理
    path('ccate/', viewss.Ccate.as_view()),
    # 后台文章管理
    path('carticle/', viewss.Carticle.as_view()),
    # 退出
    path('cloginOut/', viewss.CloginOut.as_view()),


    # 类视图内 formModel验证
    path('cclogin/', viewsss.Login.as_view()),


]

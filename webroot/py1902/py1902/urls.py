"""py1902 URL Configuration

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
from django.urls import path, include
from manager import views as admin

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('admin/', include('manager.urls')),
    # 登录
    path('admin/login/', admin.login),
    path('admin/logOut/', admin.logOut),
    path('verify/', admin.get_verify),

    # 后台管理
    # 后台首页
    path('admin/index/', admin.index),

]

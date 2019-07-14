"""lsputao URL Configuration

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
from putao.views import *
urlpatterns = [
    # path('admin/', admin.site.urls),
    # 后台访问入口
    path('lspt20!(/', admin_login),
    # 获取极验的预处理参数
    path('pcgetcaptcha/', admin_pcgetcaptcha),
    # 后台数据接口
    path('admin/menu/', admin_menu),
    path('admin/login/', admin_check),
    path('admin/adminInfo/', admin_info),
    path('admin/changepwd/', admin_changepwd),

]

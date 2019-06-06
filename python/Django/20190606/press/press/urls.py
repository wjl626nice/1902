"""press URL Configuration

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
from manager.views import *
from app01.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # 出版社操作
    path('press_list', press_list),
    path('press_add', press_add),
    path('press_del', press_del),
    path('press_edit', press_edit),
    # 图书管理
    path('book_list', book_list),
    path('book_add', book_add),
    path('book_del', book_del),
    path('book_edit', book_edit),
    # 作者管理
    path('author_list', author_list),
    path('author_add', author_add),
    path('author_del', author_del),
    path('author_edit', author_edit),
    # 测试页面
    path('test', test),
]

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
import os
from django.contrib import admin
from django.urls import path, include
from manager import views as admin
from Home import views as home
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # 前端
    # 首页
    path('', home.index),
    # 列表
    path('list/<int:id>.html', home.list),
    # 终端
    path('show/<int:id>.html', home.show, name='show'),
    # 通用路由
    # 文件上传
    path('fileupload/', admin.fileupload),
    # path('admin/', admin.site.urls),
    # path('admin/', include('manager.urls')),
    # 登录
    path('admin/login/', admin.login),
    # 获取极验的预处理参数
    path('pcgetcaptcha/', admin.pcgetcaptcha),
    path('admin/logOut/', admin.logOut),
    path('verify/', admin.get_verify),

    # 后台管理

    # 后台首页
    path('admin/index/', admin.index),

    # 管理员管理
    path('admin/manager/', admin.manager),
    # 添加管理员
    path('admin/manager_add/', admin.manager_add),
    # 改变管理员状态
    path('admin/manager_change_state/', admin.manager_change_state),
    # 删除管理员
    path('admin/manager_del/', admin.manager_del),
    # 管理员编辑
    path('admin/manager_edit/', admin.manager_edit),

    # 栏目管理
    path('admin/category/', admin.category),
    # 栏目添加
    path('admin/category_add/', admin.category_add),
    # 栏目删除
    path('admin/category_del/', admin.category_del),
    # 栏目修改
    path('admin/category_edit/', admin.category_edit),

    # 文章管理
    path('admin/article/', admin.article),
    # 文章添加
    path('admin/article_add/', admin.article_add),
    # 文章删除
    path('admin/article_del/', admin.article_del),
    # 文章修改
    path('admin/article_edit/', admin.article_edit),


    # 友情链接管理
    path('admin/links/', admin.links),

] + static(settings.MEDIA_URL, document_root=os.path.join(settings.BASE_DIR, 'uploads'))
    # 配置上传文件访问路径



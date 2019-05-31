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
# 注意 两个应用的views 中 函数名不能重复
from app01.views import *
from app02.views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('app01_info', app01_info),
    path('app02_info', app02_info),
    # 查询所有学生
    path('students_list', students_list),
    # 添加学生
    path('add_student', add_student),
    # 删除学生
    path('del_student', del_student),
]

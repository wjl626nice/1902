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
from django.urls import path, re_path
from app01.views import *
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('abc/', abc),
    # path('news/11.html', abc),
    # path('news/12.html', abc),
    # path('news/13.html', abc),
    path('news/<int:id>.html', news_show),
    path('news/<int:year>/<int:id>.html', news_show),
    path('news/<int:c>/<int:month>/<int:id>.html', news_show),

    # path('news/<int:year>/<slug:idstr>.html', news_shows),
    # 上下两个写法是等同的， <slug:idstr>  ==  <idstr>
    path('news/<int:year>/<idstr>.html', news_shows),
    path('test/<path:aaaa>.html', test),


]

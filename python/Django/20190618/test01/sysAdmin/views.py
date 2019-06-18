from django.shortcuts import render, HttpResponse

# Create your views here.

def login(request):
    return HttpResponse('登录！<a href="/admin/index">后台首页</a>')

def index(request):
    return HttpResponse('后台首页')
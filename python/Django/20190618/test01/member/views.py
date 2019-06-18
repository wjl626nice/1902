from django.shortcuts import render, HttpResponse

# Create your views here.
def login(request):
    return HttpResponse('会员登录！<a href="/member/index">首页</a>')

def index(request):
    return HttpResponse('会员首页！<a href="/member/order">订单页</a>')

def order(request):
    return HttpResponse('订单页！<a href="/member/order">订单页</a><a href="/admin/login">后台登录</a>')
from django.shortcuts import render, HttpResponse, redirect
from test01 import settings


def aaa_a_b(request):
    response = HttpResponse()
    response.set_cookie('name', 'abc', path='/aaa/a/b/')
    response.content = '测试'
    return response


def aaa_a_b_c(request):
    name = request.COOKIES.get('name')
    return HttpResponse('测试获取' + name)

def aaa_a(request):
    name = request.COOKIES.get('name', '')
    return HttpResponse('测试获取' + name)


def wazi(request):
    response = HttpResponse()
    response.set_cookie('abc', '123', domain='.dongyang.com')
    response.content = '测试袜子站种的cookie是否在鞋站中找到'
    return response

def wazi_gc(request):
    return HttpResponse('cookie:'+request.COOKIES.get('abc', ''))

def x_gc(request):
    return HttpResponse('cookie:'+request.COOKIES.get('abc', ''))
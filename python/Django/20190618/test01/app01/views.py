from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from django.views import View
# Create your views here.


class Login(View):
    def get(self, request):
        pass
    def post(self,request):
        pass

def Loings(request):
    # request.GET  === {'id':1,'name':'afad'}
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass

    return HttpResponse('登录')

def home(request):
    return HttpResponse('首页！')

def pingguos(request):
    return HttpResponse('苹果！')

def pingguoss(request, id, area='', **kwargs):
    print(kwargs)
    # 通过路由的别名 反向获取对应的uri
    print(reverse('lpg', kwargs={'id':123}))  # pingguo/s123
    print(reverse('hpg', kwargs={'area': 'beijing', 'id': 123}))  # pingguo/s123
    # 跳转到固定的路由地址
    # return redirect('/pingguo/qinghai/s124')
    return HttpResponse('苹果！' + str(id) + area)

def news_list(request, year, month=None):
    return HttpResponse(str(year)+'年'+str(month)+'月新闻')

def news_show(request, year, id, month=None):
    return HttpResponse(str(year)+'年'+str(month)+'月第'+str(id)+'条新闻！')

def banana_type(rquest,type_id):
    return HttpResponse('香蕉' + str(type_id))

def banana_types(rquest, area, type_id):
    return HttpResponse(area + '香蕉' + str(type_id))

def banana_lists(request, year):
    return HttpResponse(year + '年的香蕉')

def banana_listss(request, year, month):

    return HttpResponse(year + '年' + month + '月的香蕉')
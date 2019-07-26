from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import json

# Create your views here.
def cate_articles(request):
    id = request.GET.get('cate_id')
    data = [
        {"id": 1, "pic": '/static/images/b01.jpg', "title": '宝宝个人博客模板-亲子博客模', "click": 1235, "comment": 12,
         "describles": '些开源的博客程序源码，都是经过很多次版本测试的，都有固定的使用人群。'},
        {"id": 1, "pic": '/static/images/b01.jpg', "title": '宝宝个人博客模板-亲子博客模', "click": 843, "comment": 123,
         "describles": '些开源的博客程序源码，都是经过很多次版本测试的，都有固定的使用人群。'}
    ]
    return HttpResponse(json.dumps(data))
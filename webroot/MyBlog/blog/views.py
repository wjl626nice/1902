from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def cate_articles(request):
    print(request.GET)
    return JsonResponse({"id": 1, 'title': '11111'})
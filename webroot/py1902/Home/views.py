from django.shortcuts import render,HttpResponse
from manager.models import *
# Create your views here.

def index(request):
    """
    前台首页
    :param request:
    :return:
    """
    # 获取所有要在导航上展示的 菜单
    cates = Category.objects.filter(is_menu=True).values('id', 'cate_name').order_by('-weight')
    # 获取推荐博文
    # articles = Article.objects.filter(flag=2).values('id', 'title', 'describles', 'add_time', 'pic').order_by('-id')[0:8]
    articles = Article.objects.filter(flag=2).order_by('-id')[0:8]
    data = {
        'cates': cates,
        'articles': articles
    }
    return render(request, 'home/index.html', data)

def list(request, id):
    """
    前台栏目页
    :param request:
    :param id:
    :return:
    """
    # 获取所有要在导航上展示的 菜单
    cates = Category.objects.filter(is_menu=True).values('id', 'cate_name').order_by('-weight')

    # 获取当前栏目的文章列表
    articles = Article.objects.filter(category_id=id).order_by('-id')
    # 获取当前栏目信息
    cateInfo = Category.objects.get(id=id)
    data = {
        'cates': cates,
        'articles': articles,
        'cateInfo': cateInfo
    }
    return render(request, 'home/list.html', data)


def show(request, id):
    """
    终端页，展示文章
    :param request:
    :param id:
    :return:
    """
    return HttpResponse(id)
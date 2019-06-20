from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from app01.models import *

# Create your views here.
class Add_Cate(View):
    def get(self, request):
        return render(request, 'add_cate.html')
    def post(self, request):
        print(request.POST)
        cate_name = request.POST.get('cate_name')
        describles = request.POST['describles']
        Category.objects.create(cate_name=cate_name, describles=describles)
        # 重定向跳转
        return redirect('/add_cate/')

def add_article(request):
    if request.method == 'GET':
        categorys = Category.objects.all()
        return render(request, 'add_article.html', {'categorys': categorys})
    if request.method == 'POST':
        title = request.POST['title']
        cate_id = request.POST['cate_id']
        content = request.POST['content']
        # Article.objects.create(title=title,category_id=cate_id,content=content)
        Article.objects.create(title=title, category=Category.objects.get(id=cate_id),content=content)
        return redirect('/add_article/')



def cate_list(request):
    categorys = Category.objects.all()
    print(Category.objects.get(id=3))
    print(categorys)
    return render(request, 'cate_list.html', {'categorys': categorys})

def article_list(request):
    artile = Article.objects.get(id=1)
    print(artile)
    print(artile.title)
    print(artile.category)
    print(artile.category.cate_name)
    return HttpResponse('文章列表')
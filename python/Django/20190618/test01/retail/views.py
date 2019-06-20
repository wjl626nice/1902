from django.shortcuts import render,HttpResponse, redirect
from django.urls  import reverse
# Create your views here.
def login(request):
    # url = reverse('lpg',kwargs={'id': 123456})
    # print(url)  #  /pingguo/s123456

    # return redirect(url)  # 发送一个响应（重定向）
    # return HttpResponse('分销登录页面！'+ str(id))
    print(reverse('rt:l'))
    # return redirect('/pingguossss/s234')
    return render(request, 'retail_login.html')


def logins(request, id):
    return HttpResponse('分销登录页面！'+ str(id))
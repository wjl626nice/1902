from django.shortcuts import render
from django.http   import JsonResponse

# Create your views here.
def login(request):
    if request.is_ajax():
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        print(request.POST)
        if not username:
            return JsonResponse({'msg': '用户名不能为空！', 'code': 1, 'data': []})
        if not pwd:
            return JsonResponse({'msg': '密码不能为空！', 'code': 2, 'data': []})

        if username == 'admin' and pwd == 'admin888':
            return JsonResponse({'msg': 'success', 'code': 0, 'data': []})

        return JsonResponse({'msg': '密码或者用户名不对！', 'code': 3, 'data': []})
        # 向客户端响应字符串
        # return JsonResponse({'msg': 'success', 'code': 0, 'data': []})
    return render(request, 'login.html')


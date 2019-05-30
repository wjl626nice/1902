from django.shortcuts import render, HttpResponse


def login(request):
    """
    展示登录页面和检测登录
    :param request:
    :return:
    """
    # 判断请求方法，请求方法不同执行的代码不同
    # if request.method == 'get':
    #     return render(request, 'login.html')
    # 如果是http是post提交方式 那么执行if中的代码
    msg = ''
    if request.method == 'post':
        # 获取用户名
        username = request.POST.get('username')
        # 获取密码
        passwd = request.POST.get('password')

        # 判断用户名和密码是否正确
        if username == 'admin' and passwd == 'admin888':
            return HttpResponse('成功！')
        else:
            msg = '用户名或者密码错误！'
    # render 渲染模板，读取模板展示到浏览器，第一个参数request,第二个参数模板文件名，第三个参数，向模板传递的参数
    return render(request, 'login.html', {'result': msg})


def logins(request):
    """
    登录页面
    :param request:  和浏览器请求相关的参数
    :return:    返回一个登录页面
    """
    return render(request, 'logins.html')


def check_login(request):
    """
    检测登录
    :param request:
    :return:
    """

    # request 包含了请求的所有参数
    # request.method 获取提交方式
    #
    print(request)
    print(request.method)
    # 获取form表单post提交的数据
    print(request.POST)
    print(request.POST['username'])
    print(request.POST['password'])
    # 获取指定的参数
    print(request.POST.get('username'))

    # 获取用户名
    username = request.POST.get('username')
    # 获取密码
    passwd = request.POST.get('password')

    # 判断用户名和密码是否正确
    if username == 'admin' and passwd == 'admin888':
        return HttpResponse('成功！')
    else:
        # 失败了需要再次回到登录页面
        return render(request, 'logins.html', {'result': '用户名或者密码错误！'})

from django.shortcuts import render, HttpResponse, redirect
from app01 import models
# Create your views here.


def app01_info(request):

    return HttpResponse('我是app01')


def students_list(request):
    """
    查询所有学生信息，并且以模板的方式展示
    :param request:
    :return:
    """
    # ret 是一个queryset 集合
    ret = models.Students.objects.all().order_by('-id')  # 取出 Students表中的所有数据
    print(ret)
    return render(request, 'students_list.html', {"students": ret})


def add_student(request):
    """
    添加学生
    :param request:
    :return:
    """
    msg = ''
    # 如果请求是post请求 那么执行if内的代码
    if request.method == 'POST':
        # 获取form表单的input  name值（用户输入的值）
        student_name = request.POST.get('student_name')
        if student_name:
            # 通过ORM对象向数据表中添加数据
            models.Students.objects.create(student_names=student_name)
            # 添加完成以后跳转到学生列表页面
            return redirect('/students_list')
        else:
            msg = '请输入学生姓名！'

    # get请求时  展示添加页面
    return render(request, 'add_student.html', {'msg': msg})


def del_student(request):
    """
    删除学生
    :param request:
    :return:
    """
    # 获取get传的参数,获取不到给默认值
    id = request.GET.get('id', None)
    if id:
        # 根据id查询数据
        #  models.Students.objects.get(id=id).delete()
        student = models.Students.objects.get(id=id)  #get 如果获取一个不存在的id时就会报错，理想使用 filter
        # 删除自身
        student.delete()
        # print(student)
        # 跳转到列表页面
        return redirect('/students_list')
    else:
        return HttpResponse('删除失败！')








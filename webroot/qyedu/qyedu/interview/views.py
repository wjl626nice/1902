from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse,HttpResponseRedirect
from django.shortcuts import render, redirect,reverse
from .models import Inview, Punish
from account.models import NewUser, UserRole
from .forms import InterviewForm, PunishForm
from new_admin.models import Menu, ClassGrade, StuClass
import datetime


# def index(request):
# #     return render(request, 'interview/index.html')


# 访谈记录展示页面
# @login_required(login_url='new_admin:login')
def interview_show(request):
    interview_show_list = Inview.objects.filter(state=0)
    return render(request,'interview/system_interview_show.html',locals())


# 添加访谈记录
# @login_required(login_url='new_admin:login')
def interview_add(request):
    
    classgrades = request.user.newuser.manager_user.filter(state=0)
    student_list = [su.student for su in StuClass.objects.filter(grade__in=classgrades)]
    # classgrades = ClassGrade.objects.all()
    
    return render(request, 'interview/system_interview_add.html', locals())


# 添加访谈记录验证
def interview_add_check(request):
    """
        访谈记录添加检测
        :param request:
        :return:
    """
    if request.method == "POST":
        classes = request.POST['classes']
        student = request.POST['student']
        teacher = request.user.newuser
        handle= request.POST['handle']
        content = request.POST['content']
        result = request.POST['result']
        interview_date = request.POST['interview_date']
        # add_date = request.POST['add_date']
        Inview.objects.create(classes_id=classes, student_id=student, teacher=teacher, handle=handle,
                              content=content, result=result, interview_date=interview_date)
        messages.info(request, "添加成功")
    return HttpResponseRedirect(reverse('interview:interview_show'))


# 删除访谈记录
def interview_del(request):
    """
            删除
            :param request:
            :return:
        """
    print('=====================')
    a_id = request.GET.get('c_id')
    print(a_id)
    if not a_id.isdigit():
        return JsonResponse({'status': 0, 'msg': '删除失败!'})
    try:
        interview = Inview.objects.get(id=a_id)
    except Menu.DoesNotExist:
        return JsonResponse({'status': 0, 'msg': '删除失败!'})
    interview.state = 1
    interview.save()
    return JsonResponse({'status': 1, 'msg': "删除成功!"})


# 修改访谈记录
def interview_modify(request):
    a_id = request.GET.get('a_id')
    interview = Inview.objects.get(id=a_id)
    form = InterviewForm(instance=interview)
    return render(request, 'interview/system_interview_modify.html', locals())


# 修改访谈记录后保存
def interview_save(request):
   if request.method == "POST":
       a_id = request.POST.get('a_id')
       interview = Inview.objects.get(id=a_id)
       form = InterviewForm(request.POST, instance=interview)
       if form.is_valid():
           form.save()
           messages.info(request, '修改成功')
       else:
           print(form.errors)
           messages.info(request, '修改失败,请重新操作')
       return HttpResponseRedirect(reverse("interview:interview_show"))
   return HttpResponseRedirect(reverse("interview:interview_show"))


# 访谈搜索
def interview_search_check(request):
    """
    访谈记录收搜判断
    :param request:
    :return:
    """
    if request.method == "POST":
        realname = request.POST.get("realname")
        print(realname)
        if realname == "":
            interview_show_list = Inview.objects.filter(state=0)
            return render(request, "interview/system_interview_show.html", locals())
        else:
            interview_show_list = Inview.objects.filter(student__realname__contains=realname)
            return render(request, "interview/system_interview_show.html", locals())
    return HttpResponseRedirect(reverse('interview:interview_show'))



#
# ....................................违纪处罚功能................................................


# 违纪处罚页面展示
def punish_show_manage(request):
    punish_show_list = Punish.objects.filter(is_del=0)
    return render(request,'interview/punish_show_manage.html', locals())
# def punish_show(request):
#     punish_show_list= Punish.objects.filter(is_del=0)
#     return render(request,'interview/punish_show.html',locals())


# 添加违纪处罚
def punish_add(request):
    classgrades = request.user.newuser.manager_user.filter(state=0)
    stu_class = StuClass.objects.filter(grade__in=classgrades)
    student_list = [su.student for su in stu_class]
    # user_list = NewUser.objects.all()
    # classgrades = ClassGrade.objects.all()
    # stu_class = StuClass.objects.all()
    return render(request, 'interview/punish_add.html', locals())


# 添加违纪处罚验证
def punish_add_check(request):
    if request.method == 'POST':
        c_id = request.POST['classes_id']
        student = request.POST['student']
        violate_date = request.POST['violate_date']
        teacher = request.user.newuser
        violate_content = request.POST['violate_content']
        Punish.objects.create(classes_id=c_id, student_id=student, teacher=teacher, violate_date=violate_date,
                              violate_content=violate_content)
        messages.info(request, "添加成功")
    return HttpResponseRedirect(reverse('interview:punish_show_manage'))


# 删除违纪处罚记录
def punish_del(request):
    """
            删除
            :param request:
            :return:
        """
    print('=====================')
    a_id = request.GET.get('c_id')
    print(a_id)
    if not a_id.isdigit():
        return JsonResponse({'status': 0, 'msg': '删除失败!'})
    try:
       punish =Punish.objects.get(id=a_id)
    except Menu.DoesNotExist:
        return JsonResponse({'status': 0, 'msg': '删除失败!'})
    punish.is_del=1
    punish.save()
    return JsonResponse({'status': 1, 'msg': "删除成功!"})


# # 违纪处罚表搜索
def punish_search_ckeck(request):
    """
    访谈记录收搜判断
    :param request:
    :return:
    """
    if request.method == "POST":
        realname = request.POST.get("realname")
        print(realname)
        if realname == "":
            punish_show_list = Punish.objects.filter(is_del=0)
            return render(request, "interview/punish_show_manage.html", locals())
        else:
            punish_show_list = Punish.objects.filter(student__realname__contains=realname)
            return render(request, "interview/punish_show_manage.html", locals())
    return HttpResponseRedirect(reverse('interview:punish_show_manage'))


# 修改违纪处罚记录
def punish_modify(request):
    a_id = request.GET.get('a_id')
    punish = Punish.objects.get(id=a_id)
    form = PunishForm(instance=punish)
    return render(request,'interview/punish_modify.html', locals())


# 修改违纪处罚后保存
def punish_save(request):
   if request.method == "POST":
       a_id = request.POST.get('a_id')
       punish = Punish.objects.get(id=a_id)
       old_state = punish.state
       form = PunishForm(request.POST, instance=punish)
       if form.is_valid():
           
           new_state = int(request.POST.get('state', 0))
           if old_state != new_state and new_state > 1:
               print('yyyyyyyy')
               punish.check_date = datetime.datetime.now()
               punish.save()
            
           messages.info(request, '修改成功')
       else:
           messages.info(request, '修改失败,请重新操作')
   return HttpResponseRedirect(reverse("interview:punish_show_manage"))

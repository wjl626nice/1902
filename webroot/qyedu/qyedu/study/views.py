# coding=utf8
import json
from django.db.models import Q
from django.shortcuts import render, redirect
import datetime
from django.contrib import messages
# Create your views here.
from account.models import NewUser, UserRole
from study.models import SignIn, WeekendSummarize, Evaluate
from new_admin.models import ClassGrade, StuClass
from study.models import SignIn
from give_lessons.models import LessonsPlan, Knowledge
import time
import datetime


def stu_main(request):
    """
    前台主页
    :param request:
    :return:
    """
    return render(request, 'study/stu_main.html')


def stu_sign(request):
    """
    签到展示
    :param request:
    :return:
    """
    if request.method == 'POST':
        grade = request.POST.get('grade')
        stu = request.POST.get('stu')
        stu_signs = stu_sign_judge(grade, stu)
        return render(request, 'study/sign.html', locals())
    stu_signs = SignIn.objects.all()
    return render(request, 'study/sign.html', locals())


def stu_sign_judge(grade, stu):
    stu_signs = SignIn.objects.all()
    if grade:
        if ClassGrade.objects.filter(classname=grade).exists():
            cla = ClassGrade.objects.get(classname=grade)
            stu_list = StuClass.objects.filter(grade=cla.id)
            stu_list_id = [stu.student_id for stu in stu_list]
            stu_signs = SignIn.objects.filter(student_id__in=stu_list_id)
        else:
            stu_signs = SignIn.objects.all()
    if stu:
        students = NewUser.objects.filter(Q(realname=stu)&Q(role_id=2))
        stu_list_id = [stu.id for stu in students]
        stu_signs = stu_signs.filter(student_id__in=stu_list_id)
    return stu_signs


# 前台学员签到
def student_sign(request, id_juge=0):
    id = request.user.id
    if NewUser.objects.filter(user_id=id).exists():
        ro = NewUser.objects.get(user_id=id)
        stu_signs = SignIn.objects.filter(student_id=ro).order_by('-date_time')
        id_juge = id_juge
        return render(request, 'study/qian_sign.html', locals())
    return redirect('new_admin:admin')


# 签到
def stu_add(request):
    if request.user.newuser.role.id != 2:
        messages.info(request, "只有学生可以签到")
        return redirect('study:stu_sign')
    
    cli_date = request.GET.get('cli_date')
    s_id = request.user.id
    try:
        stu_id = request.user.newuser.id
    except:
        return redirect('study:student_sign')
    # 签到不应限制时间 editor: kamiahti 2019-2-18
    # if '08:00:00' <= cli_date <= '08:30:00' \
    #         or '13:00:00' <= cli_date <= '13:30:00' \
    #         or '18:30:00' <= cli_date <= '19:00:00' \
    #         or '21:30:00' <= cli_date <= '22:00:00':
    if '07:00:00' <= cli_date <= "23:59:59":
        signin = SignIn()
        signin.student_id = request.user.newuser
        
        if '07:00:00' <= cli_date <= '08:30:00':
            signin.sign_in = 1
        elif '13:00:00' <= cli_date <= '13:30:00':
            signin.sign_in = 2
        elif '18:30:00' <= cli_date <= '19:00:00':
            signin.sign_in = 3
        elif '21:30:00' <= cli_date <= '23:59:59':
            signin.sign_in = 4
        else:
            # 迟到早退
            signin.sign_in = 5

        if SignIn.objects.filter(date_time__date=datetime.datetime.now().date(), date_time__hour__gt=0,
                                 date_time__hour__lt=12).exists() \
            or SignIn.objects.filter(date_time__date=datetime.datetime.now().date(), date_time__hour__gte=12,
                                     date_time__hour__lt=18).exists() \
            or SignIn.objects.filter(date_time__date=datetime.datetime.now().date(), date_time__hour__gte=18,
                                     date_time__hour__lt=24).exists():
            messages.info(request, '该时段已有签到记录')
        else:
            # 记录IP
            if 'HTTP_X_FORWARDED_FOR' in request.META:
                ip = request.META['HTTP_X_FORWARDED_FOR']
            else:
                ip = request.META['REMOTE_ADDR']
            signin.my_ip = ip
            messages.info(request, '签到成功')
            signin.save()
    else:
        messages.info(request, '当前非签到时间(07:00至21:30)')
    return redirect('study:student_sign', id_juge=0)


# 自我评价
def self_show(request):
    s_id = request.user.id
    ro = NewUser.objects.get(user=s_id)
    if ro.role_id == 1:
        selfs = Evaluate.objects.all()
    else:
        class_grade = ro.teacher_user.all()
        class_id = [classgrade.id for classgrade in class_grade]
        stu_list = StuClass.objects.filter(grade__in=class_id)
        stu_id = [stu.student_id for stu in stu_list]
        selfs = Evaluate.objects.filter(student_id__in=stu_id)
    return render(request, 'study/self_show.html', locals())


def self_add(request):
    """
    添加自我评价
    :param request:
    :return:
    """
    s_id = request.user.id
    ro = NewUser.objects.get(user=s_id)
    today1 = datetime.datetime.now()
    today = str(today1.year)+ "-" + str(today1.month) + "-" + str(today1.day)
    cls = StuClass.objects.get(student_id=ro)
    try:
        les_plan = LessonsPlan.objects.get(lessons_date=today)
    except:
        messages.info(request, '今日授课计划还未发布')
        return redirect('study:qian_selfshow')
    if request.method == 'POST':
        eval = Evaluate()
        content = request.POST.get('content')
        eval.evaluete_content = content
        for key, val in request.POST.items():
            if key != 'content' and key != 'csrfmiddlewaretoken':
                eval.knowledges = eval.knowledges + key + ': ' + val + ';<br />'
        eval.student_id = ro
        eval.give_les = les_plan
        eval.save()
        return redirect('study:qian_selfshow')
    knows = les_plan.knowledges.all()
    return render(request, 'study/self_add.html', locals())


def self_modify(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        if Evaluate.objects.filter(id=id).exists():
            content = request.POST.get('content')
            eval = Evaluate.objects.get(id=id)
            eval.knowledges = ''
            eval.evaluete_content = content
            for key, val in request.POST.items():
                if key != 'content' and key != 'csrfmiddlewaretoken' and key != 'id':
                    eval.knowledges = eval.knowledges + key + ': ' + val + ';<br />'
            eval.save()
            messages.info(request, '修改成功')
        else:
            messages.info(request, '该信息不存在')
        return redirect('study:qian_selfshow')
    else:
        id = request.GET.get('c_id')
        if Evaluate.objects.filter(id=id).exists():
            eval = Evaluate.objects.get(id=id)
            evals = eval.knowledges.split(';<br>')
            knows = []
            for ev in evals[:-1]:
                knows.append(ev.split(': '))
        return render(request, 'study/self_modify.html', locals())


# 前台自我展示（自我评价)
def qian_selfshow(request):
    s_id = request.user.id
    ro = NewUser.objects.get(user=s_id)
    today = datetime.datetime.now()
    selfs = Evaluate.objects.filter(student_id=ro.id).order_by('-plub_date')
    try:
        if today.year == selfs[0].plub_date.year and today.month == selfs[0].plub_date.month and today.day == selfs[0].plub_date.day:
            expire = 1
        else:
            expire = 0
    except:
        expire = 0
    return render(request, 'study/qian_self_show.html', locals())


# 周末总结
def stuweek_add(request):
    if request.method == 'POST':
        s_id = request.user.id
        stu_id = NewUser.objects.get(user=s_id)
        content = request.POST.get('content')
        if content is None:
            messages.info(request, '内容不能为空')
            return redirect('study:stuweek_add')
        WeekendSummarize.objects.create(student_id_id=stu_id.id, content=content)
        return redirect('study:qianweek')
    else:
        return render(request, 'study/stuweek_add.html')


def qianweek(request):
    s_id = request.user.id
    ro = NewUser.objects.get(user=s_id)
    today = datetime.datetime.now()
    stuweeks = WeekendSummarize.objects.filter(student_id=ro.id).order_by('-publish_date')
    # 判断本周是否已经评价
    try:
        if today.year == stuweeks[0].publish_date.year and today.isocalendar()[1] == stuweeks[0].publish_date.isocalendar()[1]:
            expire = 1
        else:
            expire = 0
    except:
        expire = 0
    return render(request, 'study/qian_stuweek.html', locals())


# 周末总结后台
def stuweek_show(request):
    s_id = request.user.id
    ro = NewUser.objects.get(user=s_id)
    if ro.role_id == 1:
        stuweeks = WeekendSummarize.objects.all()
    else:
        if ro.role_id == 6:
            class_grade = ro.teacher_user.all()
        class_id = [classgrade.id for classgrade in class_grade]
        stu_list = StuClass.objects.filter(grade__in=class_id)
        stu_id = [stu.student_id for stu in stu_list]
        stuweeks = WeekendSummarize.objects.filter(student_id__in=stu_id)
    return render(request, 'study/stuweek_show.html', locals())


def stuweek_modify(request):
    s_id = request.user.id
    ro = NewUser.objects.get(user=s_id)
    if request.method == 'GET':
        id = request.GET.get('c_id')
        if not WeekendSummarize.objects.filter(id=id).exists():
            messages.info(request, '该总结不存在')
            return redirect('study:stuweek_show')
        else:
            stuweek = WeekendSummarize.objects.get(id=id)
            content = stuweek.content
        return render(request, 'study/stuweek_modify.html',locals())
    else:
        id = int(request.POST.get('id'))
        if WeekendSummarize.objects.filter(id=id).exists():
            stuweek = WeekendSummarize.objects.get(id=id)
            stuweek.content = request.POST.get('content')
            if ro.role_id == 6:
                stuweek.score = request.POST.get('score')
                stuweek.score_date = request.POST.get('score_date')
                stuweek.save()
                return redirect('study:stuweek_show')
            stuweek.save()
            messages.info(request, '修改成功')
        messages.info(request, '该信息不存在')
        return redirect('study:qianweek')



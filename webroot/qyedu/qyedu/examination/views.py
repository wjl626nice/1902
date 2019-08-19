from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from account.models import NewUser
from examination.models import Exam
from new_admin.models import ClassGrade
from django.contrib import messages
from new_admin.tools import listing


@login_required(login_url='new_admin:login')
def record_info_list(request):
    """
    考试记录
    :param request:
    :return:
    """
    exam_week = Exam.objects.all().filter(category=0).filter(is_del=0)
    exam_stage = Exam.objects.all().filter(category=1).filter(is_del=0)
    context = dict(exam_week=exam_week, exam_stage=exam_stage)
    return render(request, 'examination/record_info.html', context)


@login_required(login_url='new_admin:login')
def record_info_add(request):
    """
    周考记录添加
    :param request:
    :return:
    """
    user_list = NewUser.objects.all().filter(role_id=2)
    teacher_list = NewUser.objects.all().filter(role_id=6)
    class_list = ClassGrade.objects.all()
    return render(request, 'examination/record_info_add.html', locals())


@login_required(login_url='new_admin:login')
def record_info_add_check(request):
    """
    周考记录添加检测
    :param request:
    :return:
    """
    if request.method == 'POST':
        category = request.POST.get('category')
        class_room = request.POST.get('class_room')
        course = request.POST.get('course')
        exam_time = request.POST.get('exam_time')
        score = request.POST.get('score')
        user = request.POST.get('user')
        user_tea = request.POST.get('user_tea')
        try:
            u = NewUser.objects.get(id=user)
            t = NewUser.objects.get(id=user_tea)
            c = ClassGrade.objects.get(id=class_room)
        except Exception:
            return redirect('examination:record_info_add')
        Exam.objects.create(category=category, class_room_id=c.id, course=course, exam_time=exam_time, score=score,
                            user_id=u.id, user_tea_id=t.id)
        messages.info(request, '添加成功')
        return redirect('examination:record_info_list')
    return redirect('examination:record_info_add')


@login_required(login_url='new_admin:login')
def record_info_modify(request):
    """
    周考记录修改
    :param request:
    :return:
    """
    c_id = request.GET.get('c_id')
    request.session['c_id'] = c_id
    user = NewUser.objects.all()
    class_name = ClassGrade.objects.all()
    if Exam.objects.filter(id=c_id).exists():
        exam = Exam.objects.get(id=c_id)
    return render(request, 'examination/record_info_modify.html', locals())


@login_required(login_url='new_admin:login')
def record_info_modify_check(request):
    """
    周考记录修改检测
    :param request:
    :return:
    """
    if request.method == "POST":
        c_id = request.session.get('c_id')
        exam = Exam.objects.get(id=c_id)
        exam.user_id = request.POST['user']
        exam.class_room_id = request.POST['class_room']
        exam.course = request.POST['course']
        exam.exam_time = request.POST['exam_time']
        exam.score = request.POST['score']
        exam.category = request.POST['category']
        exam.user_tea_id = request.POST['user_tea']
        exam.save()
        messages.info(request, '修改成功!')
    return redirect('examination:record_info_list')


def record_search(request):
    """
    周考记录查询
    :param request:
    :return:
    """
    if request.method == 'POST':
        category = request.POST.get('category', None)
        start_time = request.POST.get('start_time', None)
        end_time = request.POST.get('end_time', None)
        name = request.POST.get('name', None)
        exam_week = Exam.objects.filter(is_del=0).filter(category=0)
        exam_stage = Exam.objects.filter(is_del=0).filter(category=1)
        if category == '2':
            if start_time:
                exam_week = exam_week.filter(exam_time__gte=start_time)
                exam_stage = exam_stage.filter(exam_time__gte=start_time)
            if end_time:
                exam_week = exam_week.filter(exam_time__lte=end_time)
                exam_stage = exam_stage.filter(exam_time__lte=end_time)
            if name:
                exam_week = exam_week.filter(
                    Q(course__istartswith=name) | Q(user_tea_id__realname__istartswith=name) |
                    Q(user_id__realname__istartswith=name))
                exam_stage = exam_stage.filter(
                    Q(course__istartswith=name) | Q(user_tea_id__realname__istartswith=name) | Q(
                        user_id__realname__istartswith=name))
            return render(request, 'examination/record_info.html', locals())
        if category == '0':
            if start_time:
                exam_week = exam_week.filter(exam_time__gte=start_time)
            if end_time:
                exam_week = exam_week.filter(exam_time__lte=end_time)
            if name:
                exam_week = exam_week.filter(
                    Q(course__istartswith=name) | Q(user_tea_id__realname__istartswith=name) |
                    Q(user_id__realname__istartswith=name))
            return render(request, 'examination/record_info.html', locals())
        if category == '1':
            if start_time:
                exam_stage = exam_stage.filter(exam_time__gte=start_time)
            if end_time:
                exam_stage = exam_stage.filter(exam_time__lte=end_time)
            if name:
                exam_stage = exam_stage.filter(
                    Q(course__istartswith=name) | Q(user_tea_id__realname__istartswith=name) | Q(
                        user_id__realname__istartswith=name))
            return render(request, 'examination/record_info.html', locals())
    return redirect(reverse('examination:record_info_list'))


def record_info_del(request):
    """
     周考记录删除
     :param request:
     :return:
     """
    c_id = request.GET.get('c_id')
    if not c_id.isdigit():
        return JsonResponse({'status': 2, 'msg': '删除失败!'})
    try:
        exam = Exam.objects.get(id=c_id)
    except Exam.DoesNotExist:
        return JsonResponse({'status': 2, 'msg': '删除失败!'})
    else:
        exam.is_del = 1
        exam.save()
        return JsonResponse({'status': 1, 'msg': "删除成功!"})


@login_required(login_url='new_admin:login')
def record_info_many_del(request):
    """
    周考记录批量删除
    :param request:
    :return:
    """
    if request.method == 'GET':
        id_str = request.GET.get('id_str')
        if not id_str:
            return JsonResponse({'status': '2', 'msg': '删除失败,请选择后再删除'})
        exam_list = id_str.split(',')
        exams = Exam.objects.filter(id__in=exam_list)
        for e in exams:
            e.is_del = 1
            e.save()
        return JsonResponse({'status': '1', 'msg': '删除成功'})
    else:
        return JsonResponse({'status': '2', 'msg': '删除失败'})

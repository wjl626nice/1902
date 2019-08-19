# coding=utf8
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect
from .models import LessonsPlan, Knowledge
from account.models import NewUser, UserRole
from new_admin.models import ClassGrade


def giveles_add(request):
    """
    授课计划录入
    :param request:
    :return:
    """
    try:
        user = NewUser.objects.get(user_id=request.user.id)
    except Exception:
        return redirect('new_admin:login')
    if request.user.is_superuser:
        messages.info(request, "只有授课教师能够添加授课计划")
    # 这个教师所交的正式开班的班级
    classgrades = ClassGrade.objects.filter(Q(teacher_user_id=user.id) & Q(class_type=1))
    if request.method == 'POST':
        les_plan = request.POST.get('les_plan')
        class_grade_id = int(request.POST.get('class_grade_id'))
        task_check_date = request.POST.get('task_check_date')
        task_des = request.POST.get('task_des')
        lessons_date = request.POST.get('lessons_date')
        if les_plan is None:
            messages.info(request, '授课内容不能为空')
            return redirect('give_lessons:giveles_show')
        if class_grade_id is None:
            messages.info(request, '班级不能为空')
            return redirect('give_lessons:giveles_show')
        if task_des is None:
            messages.info(request, '作业不能为空')
            return redirect('give_lessons:giveles_show')
        if lessons_date is None:
            messages.info(request, '授课时间不能为空')
            return redirect('give_lessons:giveles_show')
        plan = LessonsPlan.objects.create(les_plan=les_plan, class_grade_id_id=class_grade_id, teacher_id_id=user.id,
                                          task_des=task_des, lessons_date=lessons_date, task_check_date=task_check_date,
                                          is_del=0)
        messages.info(request, '添加成功')
        return redirect('give_lessons:giveles_show')
    return render(request, 'give_lessons/giveles_add.html', locals())


def giveles_modify(request):
    """
    授课修改
    :param request:
    :return:
    """
    a = request.GET.get('a')
    try:
        user = NewUser.objects.get(user_id=request.user.id)
        plan = LessonsPlan.objects.get(id=a)
    except Exception:
        return redirect('new_admin:login')
    classgrades = ClassGrade.objects.filter(Q(teacher_user_id=user.id) & Q(class_type=1))
    return render(request, 'give_lessons/giveles_modify.html', locals())


def giveles_modify_check(request):
    """
    授课修改验证
    :param request:
    :return:
    """
    if request.method == 'POST':
        id = request.POST.get('id')
        les_plan = request.POST.get('les_plan')
        class_grade_id = int(request.POST.get('class_grade_id'))
        task_check_date = request.POST.get('task_check_date')
        task_des = request.POST.get('task_des')
        lessons_date = request.POST.get('lessons_date')
        if les_plan is None:
            messages.info(request, '授课内容不能为空')
            return redirect('give_lessons:giveles_show')
        if class_grade_id is None:
            messages.info(request, '班级不能为空')
            return redirect('give_lessons:giveles_show')
        if task_des is None:
            messages.info(request, '作业不能为空')
            return redirect('give_lessons:giveles_show')
        if lessons_date is None:
            messages.info(request, '授课时间不能为空')
            return redirect('give_lessons:giveles_show')

        try:
            plann = LessonsPlan.objects.get(id=id)
        except Exception:
            return redirect('give_lessons:giveles_show')
        plann.les_plan = les_plan
        plann.class_grade_id_id = class_grade_id
        plann.task_check_date = task_check_date
        plann.task_des = task_des
        plann.lessons_date = lessons_date
        plann.save()
        messages.info(request, '修改成功')
    return redirect('give_lessons:giveles_show')


def giveles_show(request):
    """
    授课计划展示
    :param request:
    :return:
    """
    # 查询当前讲师所教班级的授课计划
    try:
        user = NewUser.objects.get(user_id=request.user.id)
    except Exception:
        return redirect('new_admin:login')
    is_student = False
    if user.role.id == 2:
        class_grade = user.stuclass_student.first().grade
        plan_list = LessonsPlan.objects.filter(is_del=0, class_grade_id=class_grade)
        is_student = True
    else:
        # 这个讲师授课的正式开班的班级
        classgrades = ClassGrade.objects.filter(Q(teacher_user_id=user.id) & Q(class_type=1))
        cid_list = [classgrade.id for classgrade in classgrades]
        if request.user.is_superuser:
            plan_list = LessonsPlan.objects.filter(is_del=0).order_by("-id")
        else:
            plan_list = LessonsPlan.objects.filter(Q(is_del=0) & Q(teacher_id=user.id) & Q(class_grade_id__in=cid_list)).order_by('-add_date')
        if request.method == 'POST':
            search = request.POST.get('search')
            if search == 'true':
                start_date = request.POST.get('start_date')
                stop_date = request.POST.get('stop_date')
                class_name = request.POST.get('class_name')
                if start_date:
                    plan_list = plan_list.filter(add_date__gte=start_date)
                if stop_date:
                    plan_list = plan_list.filter(add_date__lte=stop_date)
                if class_name:
                    classgrades = ClassGrade.objects.filter(classname__contains=class_name)
                    id_list = [classgrade.id for classgrade in classgrades]
                    plan_list = plan_list.filter(class_grade_id__in=id_list)
    return render(request, 'give_lessons/giveles_show.html', locals())


def know_add(request):
    """
    录入知识点
    :param request:
    :return:
    """
    if request.method == 'POST':
        lessonsplan_id = request.POST.get('lessonsplan_id')
        name = request.POST.get('name')
        grasp_level = request.POST.get('grasp_level')
        if name is None:
            messages.info(request, '知识点不能为空')
            return redirect('give_lessons:giveles_show')
        if grasp_level is None:
            messages.info(request, '知识点要求掌握程度不能为空')
            return redirect('give_lessons:giveles_show')
        if Knowledge.objects.filter(name=name, lessonsplan_id=lessonsplan_id, is_del=0).count() > 0:
            messages.info(request, "此知识点已存在")
        else:
            know = Knowledge.objects.create(name=name, grasp_level=grasp_level, lessonsplan_id=lessonsplan_id, is_del=0)
            messages.info(request, '添加成功')
        return redirect('give_lessons:giveles_show')
    else:
        a = request.GET.get('a')
        try:
            plan = LessonsPlan.objects.get(id=int(a))
        except:
            messages.info(request, '该计划不存在')
            return redirect('give_lessons:giveles_show')
        knows = plan.knowledges.all()
        return render(request, 'give_lessons/know_add.html', locals())


def know_show(request):
    """
    知识点列表
    :param request:
    :return:
    """
    is_student = True if request.user.newuser.role.id == 2 else False
    # 传入计划id。则只查出此计划的知识点
    if request.GET.get('id', 0):
        know_list = Knowledge.objects.filter(is_del=0, lessonsplan__id=request.GET.get('id'))
    else:
        know_list = Knowledge.objects.filter(is_del=0).order_by('-add_date')
    if request.method == 'POST':
        name = request.POST.get('name')
        if name is not None:
            know_list = know_list.filter(name__contains=name)
    return render(request, 'give_lessons/know_show.html', locals())


def know_modify(request):
    """
    知识点修改
    :param request:
    :return:
    """
    a = request.GET.get('a')
    try:
        know = Knowledge.objects.get(id=a)
    except Exception:
        return redirect('give_lessons:know_show')
    return render(request, 'give_lessons/know_modify.html', locals())


def know_modify_check(request):
    """
    知识点验证修改
    :param request:
    :return:
    """
    if request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        grasp_level = request.POST.get('grasp_level')
        try:
            know = Knowledge.objects.get(id=id)
        except Exception:
            return redirect('give_lessons:know_show')
        know.name = name
        know.grasp_level = grasp_level
        know.save()
        messages.info(request, '修改成功')
    return redirect('give_lessons:know_show')


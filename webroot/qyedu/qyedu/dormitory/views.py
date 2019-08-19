from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from account.models import NewUser
from dormitory.models import DormHandle, DorStu
from new_admin.models import Dorm
from new_admin.tools import listing
from datetime import datetime

# Create your views here
def dormstu_list(request):
    """
    学员入住信息
    :param request:
    :return:
    """
    dormstu_list = DorStu.objects.filter(is_del=0).order_by('-entry_date')
    if request.method == 'POST':
        search = request.POST.get('search')
        if search == 'true':
            start_time = request.POST.get('start_time')
            stop_time = request.POST.get('stop_time')
            name = request.POST.get('name')
            dormstu_list = get_search(start_time, stop_time, name).order_by('-entry_date')
    count = 5
    page = request.GET.get('page')
    d_list = listing(dormstu_list, page, count)
    return render(request, 'dormitory/dormstu_list.html', locals())


def get_search(start_time, stop_time, name):
    """
    入住查询
    :param
    start_time:
    stop_time:
    name:
    :return:
    """
    dormstu_list=DorStu.objects.filter(is_del=0)
    if name:
        if Dorm.objects.filter(dorm_name=name).exists() or NewUser.objects.filter(realname=name).exists():
            try:
                dorm = Dorm.objects.get(dorm_name=name)
                dormstu_list=dormstu_list.filter(dormitory_id=dorm.id)
            except Exception:
                newuser = NewUser.objects.get(realname=name)
                dormstu_list = dormstu_list.filter(Q(user_id=newuser.id) | Q(headmaster_id=newuser.id))
        else:
            dormstu_list=DorStu.objects.filter(id=0)
    if start_time:
        dormstu_list=dormstu_list.filter(entry_date__gte=start_time)
    if stop_time:
        dormstu_list=dormstu_list.filter(entry_date__lte=stop_time)
    return dormstu_list


def dormstu_add(request):
    """
    添加学员入住信息
    :param request:
    :return:
    """
    if request.session.get('hid', False):
        username = request.user.username
        user = User.objects.get(username=username)
        new_user = NewUser.objects.get(user_id=user.id)
        newuser = NewUser.objects.filter(role_id=2).exclude(id__in=[ds.user.id for ds in DorStu.objects.filter(is_del=0)])
        dorm_list = Dorm.objects.all()
        return render(request, 'dormitory/dormstu_add.html', locals())
    return HttpResponseRedirect(reverse('new_admin:login'))


def dormstu_add_check(request):
    """
    添加学员入住验证
    :param request:
    :return:
    """
    username = request.session.get('username')
    user = User.objects.get(username=username)
    newuser = NewUser.objects.get(user_id=user.id)
    newuser_id = newuser.id
    if request.method == 'POST':
        dorm_user = request.POST.get('dorm_user')
        dorm_name = request.POST.get('dorm_name')
        entry_date = request.POST.get('entry_date')
        leave_date = request.POST.get('leave_date')
        if dorm_user == '0':
            messages.info(request, '学员不能为空')
            return redirect('dormitory:dormstu_list')
        if DorStu.objects.filter(user_id=dorm_user, is_del=0).exists():
            messages.info(request, '该学员已添加,请重新选择')
            return redirect('dormitory:dormstu_list')
        else:
            if dorm_name == '未入住':
                dormstu = DorStu()
                dormstu.user_id = dorm_user
                dormstu.headmaster_id=newuser_id
                dormstu.save()
                messages.info(request, '添加成功')
                return redirect('dormitory:dormstu_list')
            else:
                if entry_date == '':
                    messages.info(request, '入住时间不能为为空')
                    return redirect('dormitory:dormstu_list')
                dorm_count = DorStu.objects.filter(dormitory_id=dorm_name).count()
                dorm = Dorm.objects.get(id=dorm_name)
                max_stu = dorm.max_stu
                if int(dorm_count) < int(max_stu):
                    dormstu=DorStu()
                    dormstu.dormitory_id = dorm_name
                    dormstu.user_id = dorm_user
                    dormstu.entry_date = entry_date
                    dormstu.headmaster_id = newuser_id
                    if leave_date == '':
                        dormstu.save()
                    else:
                        if leave_date > entry_date:
                            dormstu.leave_date = leave_date
                            dormstu.save()
                        else:
                            messages.info(request, '离开时间大于入住时间')
                            return redirect('dormitory:dormstu_list')
                    messages.info(request, '添加成功')
                    return redirect('dormitory:dormstu_list')
                messages.info(request, '该宿舍人数已达上限 , 请重新选择宿舍添加')
                return redirect('dormitory:dormstu_list')
    return redirect('dormitory:dormstu_list')


def dormstu_modify(request):
    """
    修改学员入住信息
    :param request:
    :return:
    """
    if request.session.get('hid', False):
        m=request.GET.get('m')
        dormstu = DorStu.objects.get(id=m)
        name = NewUser.objects.get(id=dormstu.user_id)
        if Dorm.objects.filter(id=dormstu.dormitory_id).exists():
            dorm = Dorm.objects.get(id=dormstu.dormitory_id)
        else:
            dorm = ''
        headmaster = NewUser.objects.get(id=dormstu.headmaster_id)
        newuser=NewUser.objects.filter(role_id=2)
        dorm_list=Dorm.objects.all()
        return render(request, 'dormitory/dormstu_modify.html', locals())
    return HttpResponseRedirect(reverse('new_admin:login'))


def dormstu_modify_check(request):
    """
    修改学员入住验证
    :param request:
    :return:
    """
    if request.method == 'POST':
        dorm_name = request.POST.get('dorm_name')
        entry_date = request.POST.get('entry_date')
        leave_date = request.POST.get('leave_date')
        id = request.POST.get('id')
        if dorm_name == '':
            messages.info(request, '请填写宿舍名！')
            return redirect(reverse("dormitory:dormstu_modify"))
        dormname_old = DorStu.objects.get(id=id)
        dorm_count=DorStu.objects.filter(dormitory_id=dorm_name).count()
        dorm=Dorm.objects.get(id=dorm_name)
        max_stu=dorm.max_stu
        if dormname_old.dormitory_id == int(dorm_name):
            if int(dorm_count) <= int(max_stu):
                dormstu = DorStu.objects.get(id=id)
                dormstu.dormitory_id=dorm_name
                if entry_date == '' and dormstu.entry_date is not None:
                    messages.info(request, '入住时间不能修改为空!')
                    return redirect('dormitory:dormstu_list')
                elif dormstu.entry_date is None and entry_date == '':
                    dormstu.save()
                else:
                    dormstu.entry_date=entry_date
                    dormstu.save()
                if leave_date == '' and dormstu.leave_date is not None:
                    messages.info(request, '离开时间不能修改为空!')
                    return redirect('dormitory:dormstu_list')
                elif dormstu.leave_date is None and leave_date == '':
                    dormstu.save()
                elif leave_date > dormstu.entry_date and dormstu.entry_date is not None:
                    dormstu.leave_date=leave_date
                    dormstu.save()
                else:
                    messages.info(request, '离开时间要大于入住时间！')
                    return redirect('dormitory:dormstu_list')
                messages.info(request, '修改成功！')
                return redirect('dormitory:dormstu_list')
            else:
                messages.info(request, '修改失败!,该宿舍已满')
                return redirect(reverse("dormitory:dormstu_list"))
        else:
            if int(dorm_count) < int(max_stu):
                dormstu = DorStu.objects.get(id=id)
                dormstu.dormitory_id=dorm_name
                if entry_date == '' and dormstu.entry_date is not None:
                    messages.info(request, '入住时间不能修改为空!')
                    return redirect('dormitory:dormstu_list')
                elif dormstu.entry_date is None:
                    dormstu.save()
                else:
                    dormstu.entry_date=entry_date
                    dormstu.save()
                if leave_date == '' and dormstu.leave_date is not None:
                    messages.info(request, '离开时间不能修改为空!')
                    return redirect('dormitory:dormstu_list')
                elif dormstu.leave_date is None and leave_date == '':
                    dormstu.save()
                elif leave_date > dormstu.entry_date and dormstu.entry_date is not None:
                    dormstu.leave_date=leave_date
                    dormstu.save()
                else:
                    messages.info(request, '离开时间要大于入住时间！')
                    return redirect('dormitory:dormstu_list')
                messages.info(request, '修改成功！')
                return redirect('dormitory:dormstu_list')
            else:
                messages.info(request, '修改失败!,该宿舍已满')
                return redirect(reverse("dormitory:dormstu_list"))
    return render(request, 'new_admin/dorm_modify.html')


def dormstu_delete(request):
    """
    删除学生入住信息
    :param request:
    :return:
    """
    a=request.GET.get('a')
    if a.isdigit():
        try:
            dormstu=DorStu.objects.get(id=a)
            dormstu.is_del=1
            dormstu.save()
            return JsonResponse({'status': 1})
        except Exception:
            return JsonResponse({'status': 0})
    return JsonResponse({'status': 0})


def stu_dorm_problem(request):
    """
    宿舍问题处理
    :param request:
    :return:
    """
    dorm_list = DormHandle.objects.filter(is_del=0).order_by('-add_date')
    if request.method == 'POST':
        search = request.POST.get('search')
        if search == 'true':
            start_time = request.POST.get('start_time')
            stop_time = request.POST.get('stop_time')
            dorm_name = request.POST.get('dorm_name')
            dorm_list = get_date(start_time, stop_time, dorm_name).order_by('-add_date')
    count = 5
    page = request.GET.get('page')
    d_list = listing(dorm_list, page, count)
    return render(request, 'dormitory/stu_dorm_problem.html', locals())


def get_date(start_time, stop_time, dorm_name):
    """
    宿舍查询
    :param start_time:
    :param stop_time:
    """
    dorm_list=DormHandle.objects.filter(is_del=0)
    if dorm_name:
        if Dorm.objects.filter(dorm_name=dorm_name).exists():
            dorm_name=Dorm.objects.get(dorm_name=dorm_name)
            dorm_list=dorm_list.filter(dormitory_name=dorm_name.id)
        else:
            dorm_list=DormHandle.objects.filter(id=0)
    if start_time:
        dorm_list=dorm_list.filter(add_date__gte=start_time)
    if stop_time:
        dorm_list=dorm_list.filter(add_date__lte=stop_time)
    return dorm_list

def pro_add(request):
    """
    宿舍问题添加
    :param request:
    :return:
    """
    if request.session.get('hid', False):
        username = request.user.username
        dorm = Dorm.objects.filter(is_del=0)
        try:
            user = User.objects.get(username=username)
            new_user = NewUser.objects.get(user_id=user.id)
        except Exception:
            return redirect('dormitory:stu_dorm_problem')
        return render(request, 'dormitory/pro_add.html', locals())
    return HttpResponseRedirect(reverse('new_admin:login'))


def pro_add_check(request):
    """
    宿舍问题添加检测
    :param request:
    :return:
    """
    dorm = DormHandle()
    if request.method == 'POST':
        user_name = request.POST.get('username')
        dorm_name = request.POST.get('dorm_name')
        if dorm_name == '0':
            messages.info(request, '宿舍名称不能为空')
            return redirect('dormitory:stu_dorm_problem')
        dormitory_name = Dorm.objects.get(is_del=0, dorm_name=dorm_name)
        if NewUser.objects.filter(is_del=0, realname=user_name).exists():
            newuser = NewUser.objects.get(is_del=0, realname=user_name)
            dorstu = DorStu.objects.get(is_del=0 ,user_id=newuser.id)
            if dormitory_name.id != dorstu.dormitory_id:
                messages.info(request, '学员与宿舍信息不匹配,请重新输入')
                return redirect('dormitory:stu_dorm_problem')
        else:
            messages.info(request, '该学员不存在')
            return redirect('dormitory:stu_dorm_problem')
        try:
            u = NewUser.objects.get(is_del=0, realname=request.POST.get('add_user'))
        except Exception:
            messages.info(request, '提交失败')
            return redirect('dormitory:stu_dorm_problem')
        dorm.dormitory_name_id = dormitory_name.id
        dorm.user_name = user_name
        dorm.dor_problem = request.POST.get('pro_info')
        dorm.add_user_id = u.id
        dorm.save()
    messages.info(request, '添加成功')
    return redirect('dormitory:stu_dorm_problem')


def pro_modify(request):
    """
    宿舍问题编辑
    :param request:
    :return:
    """
    d_id = request.GET.get('d_id')
    try:
        dorm = DormHandle.objects.get(id=d_id)
        user = NewUser.objects.get(id=dorm.add_user_id)
        dorms = Dorm.objects.all()
    except Exception:
        return HttpResponseRedirect(reverse('dormitory:stu_dorm_problem'))
    context = dict(user=user, dorm=dorm, dorms=dorms)
    return render(request, 'dormitory/pro_modify.html', context)


def pro_modify_check(request):
    """
    宿舍问题编辑检测
    :param request:
    :return:
    """
    if request.method == 'POST':
        dor_problem = request.POST.get('pro_info')
        user_name = request.POST.get('username')
        dorm_name = request.POST.get('dorm_name')
        id = request.POST.get('id')
        try:
            dorm = DormHandle.objects.get(id=id)
        except Exception:
            return redirect("dormitory:stu_dorm_problem")
        dorm.dormitory_name_id = dorm_name
        dorm.user_name = user_name
        dorm.dor_problem = dor_problem
        dorm.save()
        messages.info(request, '修改成功')
    return HttpResponseRedirect(reverse('dormitory:stu_dorm_problem'))


def pro_del(request):
    """
    宿舍问题删除
    :param request:
    :return:
    """
    d_id = request.GET.get('d_id')
    if d_id.isdigit():
        try:
            dorm = DormHandle.objects.get(id=d_id)
        except Exception:
            return JsonResponse({'status': 0})
        dorm.is_del = 1
        dorm.save()
        return JsonResponse({'status': 1})
    else:
        return JsonResponse({'status': 0})


def pro_resolve(request):
    """
    问题已解决
    :param request:
    :return:
    """
    e = request.GET.get('e')
    if e.isdigit():
        try:
            dorm = DormHandle.objects.get(id=e)
        except Exception:
            return JsonResponse({'status': 0})
        dorm.handle_date = datetime.now()
        dorm.result = 2
        dorm.save()
        return JsonResponse({'status': 1})
    else:
        return JsonResponse({'status': 0})


def pro_to_resolve(request):
    """
    问题未解决
    :param request:
    :return:
    """
    if request.session.get('hid', False):
        e = request.GET.get('e')
        if e.isdigit():
            try:
                dorm = DormHandle.objects.get(id=e)
            except Exception:
                return JsonResponse({'status': 0})
            dorm.result = 1
            dorm.save()
            return JsonResponse({'status': 1})
        else:
            return JsonResponse({'status': 0})
    return HttpResponseRedirect(reverse('new_admin:login'))

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from account.models import UserRole,NewUser
from django.http import JsonResponse, HttpResponseRedirect
from .models import Followup_state
from .forms import FollowForm
from .models import Source_distribution


def followup_state(request):
    '''
    跟进状态录入
    :param request:
    :return:
    '''
    followup_states = Followup_state.objects.all()
    return render(request,'recruit_students/followup_state.html',locals())


def followup_add(request):
    '''
    跟进状态添加
    :param request:
    :return:
    '''
    user = request.user
    new_user = NewUser.objects.get(user=user)
    role = new_user.role
    students = NewUser.objects.filter(role=2)
    return render(request,'recruit_students/followup_add.html',locals())


def followup_save(request):
    '''
    跟进描述保存
    :param request:
    :return:
    '''
    user = request.user
    new_user = NewUser.objects.get(user=user)
    role = new_user.role
    if request.method == 'POST':
        if role in UserRole.objects.filter(Q(role_name='院校经理') | Q(role_name='咨询顾问')| Q(role_name='超级管理员')):
            followup_state = Followup_state()
            info = request.POST['info']
            s_id = request.POST['student_id']
            if Followup_state.objects.filter(pk=s_id).exists():
                messages.info(request,'该学生跟进状态已录入')
                return redirect(reverse('recruit_students:followup_add'))
            else:
                followup_state.f_s_name_id = s_id
                followup_state.f_record_person_id = role.id
                followup_state.f_info = info
                followup_state.save()
                return redirect(reverse('recruit_students:followup_state'))
        else:
            return redirect(reverse('recruit_students:followup_state'))
    else:
        return redirect(reverse('recruit_students:followup_state'))
    

def followup_edit(request):
    '''
    跟进状态编辑
    :param request:
    :return:
    '''
    s_id = request.GET.get('s_id')
    if s_id is None:
        return redirect(reverse('recruit_students:followup_state'))
    if not s_id.isdigit():
        return redirect(reverse('recruit_students:followup_state'))
    if s_id.isdigit():
        try:
            followup_state = Followup_state.objects.get(pk=s_id)
        except Followup_state.DoesNotExist:
            return redirect(reverse('recruit_students:followup_state'))
    form = FollowForm(instance=followup_state)
    return render(request,'recruit_students/followup_edit.html',locals())


def followup_edit_save(request):
    '''
    跟进状态编辑保存
    :param request:
    :return:
    '''
    if request.method == 'POST':
        user = request.user
        s_id = request.POST.get('s_id')
        if s_id is None:
            return redirect(reverse('recruit_students:followup_state'))
        if not s_id.isdigit():
            return redirect(reverse('recruit_students:followup_state'))
        try:
            followup_state = Followup_state.objects.get(pk=s_id)
        except Followup_state.DoesNotExist:
            return redirect(reverse('recruit_students:followup_state'))
        form = FollowForm(request.POST,instance=followup_state)
        if form.is_valid():
            form.save()
    return redirect(reverse('recruit_students:followup_state'))


def followup_del(request):
    '''
    跟进状态删除
    :param request:
    :return:
    '''
    id = request.GET.get('id')
    if id is None:
        return JsonResponse({'status':0,'msg':'删除失败'})
    if not id.isdigit():
        return JsonResponse({'status':2,'msg':'删除失败'})
    if id.isdigit():
        try:
            followup_state = Followup_state.objects.get(pk=id)
        except Followup_state.DoesNotExist:
            return JsonResponse({'status': 0, 'msg': '删除失败'})
        followup_state.delete()
        return JsonResponse({'status':1,'msg':'删除成功'})


def followup_search(request):
    '''
    跟进状态搜索
    :param request:
    :return:
    '''
    if request.method == 'POST':
        search = request.POST.get('search')
        if search:
            followup_states = Followup_state.objects.filter(f_s_name__realname__contains=search)
        else:
            followup_states = Followup_state.objects.all()
    return render(request, 'recruit_students/followup_state.html', locals())


@login_required(login_url='new_admin:login')
def input(request):
    '''
    生源录入页面（列表）
    :param request:
    :return:
    '''
    students = NewUser.objects.filter(state=0, role=2, is_del=0)
    login_user = NewUser.objects.get(user=request.user)
    return render(request, 'recruit_students/students.html', locals())


@login_required(login_url='new_admin:login')
def add_students(request):
    '''
    生源录入页面（添加窗口)
    :param request:
    :return:
    '''
    return render(request,'recruit_students/students_add.html',locals())


def add_students_check(request):
    '''
    生源录入页面学员添加验证
    :param request: 
    :return: 
    '''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        realname = request.POST.get('realname')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        info = request.POST.get('info')
        id_card = request.POST.get('id_card')
        birthday = request.POST.get('birthday')
        edu_level = request.POST.get('edu_level')
        home_address = request.POST.get('home_address')
        mobile_number = request.POST.get('mobile_number')
        if username == '' or User.objects.filter(username=username).exists():
            messages.info(request, '账号不能为空或已存在')
            return redirect('recruit_students:input')
        if password == '' or password2 == '' or password != password2:
            messages.info(request, '密码不能为空或两次输入密码不一致')
            return redirect('recruit_students:input')
        if realname == '':
            messages.info(request, '真实姓名不能为空')
            return redirect('recruit_students:input')
        if email == '':
            messages.info(request, '邮箱账号不能为空')
            return redirect('recruit_students:input')
        if info == '':
            messages.info(request, '简介不能为空')
            return redirect('recruit_students:input')
        if id_card == '' or NewUser.objects.filter(id_card=id_card).exists():
            messages.info(request, '身份账号不能为空或格式不正确或身份号已存在')
            return redirect('recruit_students:input')
        if home_address == '':
            messages.info(request, '家庭地址不能为空')
            return redirect('recruit_students:input')
        if mobile_number == '' or NewUser.objects.filter(mobile_number=mobile_number).exists():
            messages.info(request, '手机号不能为空或格式不正确或手机号已存在')
            return redirect('recruit_students:input')
        user = User.objects.create_user(username=username, password=password, email=email, is_staff=1, is_active=1)
        NewUser.objects.create(realname=realname, mobile_number=mobile_number, gender=gender, info=info,
                                          id_card=id_card, birthday=birthday, edu_level=edu_level,
                                          home_address=home_address, role_id=2, user_id=user.id)
        messages.info(request, '添加成功')
        return redirect('recruit_students:input')
    return redirect('recruit_students:input')


def del_student(request):
    '''
    生源删除
    :param request:
    :return:
    '''
    if request.session.get('hid', False):
        a = request.GET.get('a')
        b = request.GET.get('b')
        if User.objects.filter(id=b).exists():
            user = User.objects.get(id=b)
            user.is_active = 0
            user.save()
            if NewUser.objects.filter(id=a).exists():
                new_user = NewUser.objects.get(id=a)
                new_user.is_del = 1
                new_user.save()
                return JsonResponse({'status': 1})
            return JsonResponse({'status': 0})
        return JsonResponse({'status': 0})
    return HttpResponseRedirect(reverse('new_admin:login'))


@login_required(login_url='new_admin:login')
def modify_student(request):
    '''
    生源录入页面学员信息编辑页面
    :param request:
    :return:
    '''
    if request.session.get('hid', False):
        c = request.GET.get('c_id')
        if NewUser.objects.filter(id=c).exists():
            new_user = NewUser.objects.get(id=c)
            user = User.objects.get(id=new_user.user_id)
            return render(request, 'recruit_students/students_modify.html', {'user': user, 'new_user': new_user})
        else:
            messages.info(request, '此用户不存在')
            return render(request, 'recruit_students/students_modify.html')
    return HttpResponseRedirect(reverse('new_admin:login'))


def student_modify_check(request):
    """
    生源录入页面学生信息修改
    :param request:
    :return:
    """
    if request.method == 'POST':
        realname = request.POST.get('realname')
        id_card = request.POST.get('id_card')
        email = request.POST.get('email')
        info = request.POST.get('info')
        gender = request.POST.get('gender')
        print("性别是。。。")
        print(gender)
        edu_level = request.POST.get('edu_level')
        home_address = request.POST.get('home_address')
        mobile_number = request.POST.get('mobile_number')
        birthday = request.POST.get('birthday')
        user_id = request.POST.get('user_id')
        new_user_id = request.POST.get('new_user_id')
        if User.objects.filter(id=user_id).exists() and NewUser.objects.filter(id=new_user_id).exists():
            user = User.objects.get(id=user_id)
            new_user = NewUser.objects.get(id=new_user_id)
            if email == '':
                messages.info(request, '邮箱账号不能为空')
                return redirect('recruit_students:input')
            if info == '':
                messages.info(request, '简介不能为空')
                return redirect('recruit_students:input')
            if home_address == '':
                messages.info(request, '家庭地址不能为空')
                return redirect('recruit_students:input')
            if mobile_number == '':
                messages.info(request, '手机号不能为空')
                return redirect('recruit_students:input')
            if gender == None:
                messages.info(request, '请选择性别')
                return redirect('recruit_students:input')
            user.email = email
            user.save()
            new_user.info = info
            new_user.id_card = id_card
            new_user.realname = realname
            new_user.birthday = birthday
            new_user.edu_level = edu_level
            new_user.gender = gender
            new_user.home_address = home_address
            new_user.mobile_number = mobile_number
            new_user.save()
            messages.info(request, '修改成功')
            return redirect('recruit_students:input')
        messages.info(request, '用户不存在')
        return redirect('recruit_students:input')
    return redirect('recruit_students:input')


@login_required(login_url='new_admin:login')
def  student_search(request):
    '''
    学员搜索
    :param request: 
    :return: 
    '''
    if request.method == 'POST':
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        name = request.POST.get('name')
        students = NewUser.objects.filter(state=0,is_del=0,role=2)
        if start_time or end_time:
            if start_time:
                students = NewUser.objects.filter(birthday__gte=start_time, state=0,is_del=0,role=2)
            else:
                students = NewUser.objects.filter(birthday__lte=end_time, state=0,is_del=0,role=2)
        if name:
            students = students.filter(realname__istartswith=name, state=0,is_del=0,role=2)
        return render(request, 'recruit_students/students.html', locals())
    return redirect(reverse('recruit_students:input'))


@login_required(login_url='new_admin:login')
def students_distribute(request):
    '''
    生源分发(页面)
    :param request:
    :return:
    '''
    students = NewUser.objects.filter(state=0, role=2, is_del=0)
    user = request.user
    login_user = NewUser.objects.get(user=user)
    return render(request, 'recruit_students/students_distribution.html', locals())


@login_required(login_url='new_admin:login')
def dis_to_person(request):
    '''
    生源分配给咨询顾问(处理逻辑)
    :param request:
    :return:
    '''
    stu_id = request.GET.get("c_id")
    if request.method == "POST":
        consultant = request.POST.get('consultant')
        stu_id = request.POST.get("stu_id")
        # 若该生已分配过咨询顾问则更改。否则增加设置
        old_data = Source_distribution.objects.filter(student_id=stu_id)
        if len(old_data) > 0:
            # 更新为指定的咨询顾问
            if not old_data.filter(consultant_id=consultant):
                Source_distribution.objects.filter(student_id=stu_id).update(consultant_id=consultant)
        else:
            Source_distribution.objects.create(student_id=stu_id, consultant_id=consultant)
        messages.info(request, '分发成功')
        return redirect(reverse('recruit_students:students_distribute'))
    consultants = NewUser.objects.filter(user__is_active=1,user__is_staff=1, role=4, is_del=0)
    return render(request, 'recruit_students/students_distribution_to_person.html', locals())

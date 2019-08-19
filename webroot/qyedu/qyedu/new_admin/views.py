# coding=utf8

from django.contrib.auth.hashers import make_password
from re import split
import re
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from examination.models import Exam
from interview.models import Punish,Inview
from evaluate.models import ReviewTest, ReviewResult, TestQuestion
from new_admin.tools import listing
from .models import Menu, ClassGrade, Dorm, Subsidy
from account.models import NewUser, UserRole
from django.contrib.auth import authenticate, login as _login, logout
from django.http import HttpResponseRedirect, JsonResponse
from .forms import UserForm, ClassGradeForm, NewUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from talent_all.models import Talent, Tag
from give_lessons.models import LessonsPlan
import datetime
from itertools import chain


def login(request):
    """
    后台登录页面
    :param request:
    :return:
    """
    if request.session.get('online', False):
        online = request.session.get('online', False)
        password = request.session.get('password', False)
        username = request.session.get('username', False)
    form = UserForm()
    return render(request, 'new_admin/login.html', locals())


# 登录验证
def login_check(request):
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['password']
        online = request.POST.get('online')
        hid = request.POST.get('hid')
        user_form = UserForm(request.POST)
        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
        else:
            mg = '该用户不存在'
            form = UserForm()
            return render(request, 'new_admin/login.html', locals())
        user = authenticate(username=username, password=password)
        if user is None:
            mg = '用户名或密码不正确'
            form = UserForm()
            return render(request, 'new_admin/login.html', locals())
        if user_form.is_valid():
            if user is not None:
                if user.is_staff == 1:
                    request.session['prev_login'] = user.last_login
                    if str(online) == 'on':
                        request.session['online'] = online
                        request.session['username'] = username
                        request.session['password'] = password
                        request.session['hid'] = hid
                        request.session.set_expiry(0)
                        _login(request, user)
                        return HttpResponseRedirect(reverse('new_admin:index'))
                    elif online is None:
                        logout(request)
                        _login(request, user)
                        request.session['hid'] = hid
                        request.session['username'] = username
                        request.session.set_expiry(0)
                        return HttpResponseRedirect(reverse('new_admin:index'))
                else:
                    messages.info(request, '无登录权限')
                form = UserForm()
                return render(request, 'new_admin/login.html', locals())
            else:
                mg = '用户名或密码不正确'
                form = UserForm()
                return render(request, 'new_admin/login.html', locals())

        msg = '登录验证失败，请重新登录'
        form = UserForm()
        return render(request, 'new_admin/login.html', locals())
    return HttpResponseRedirect(reverse('new_admin:login'))


@login_required(login_url='new_admin:login')
def index(request):
    """
    后台框架
    :param request:
    :return:
    """
    if request.user.is_authenticated:
        print(request.user.is_superuser)
        if request.user.is_superuser == 1:
            menu = Menu.objects.all()
            parent_menu = menu.filter(parent_id=0)
            menu = menu.filter(parent_id__gt=0)
        else:
            menu = request.user.newuser.role.menu_set.all()
            parent_menu = Menu.objects.filter(id__in=[m.parent_id for m in menu])
        print(parent_menu)
        print(menu)
        context = dict(parent_menu=parent_menu, menu=menu, role=request.user.newuser.role,
                       username=request.user.username)
        return render(request, "new_admin/index.html", context)
    return HttpResponseRedirect(reverse('new_admin:login'))


def welcome(request):
    """
    后台欢迎页面
    :param request:
    :return:
    """
    if request.session.get('hid', False):
        context = dict()
        return render(request, "new_admin/welcome.html", context)
    else:
        return HttpResponseRedirect(reverse('new_admin:login'))


def logout_view(request):
    """
    退出登录
    :param request:
    :return:
    """
    if request.session.get('online', False):
        del request.session['hid']
        return HttpResponseRedirect(reverse('new_admin:login'))
    logout(request)
    return HttpResponseRedirect(reverse('new_admin:login'))


@login_required(login_url='new_admin:login')
def category(request):
    """
        菜单栏目
        :param request:
        :return:
    """
    if request.session.get('hid', False):
        category = Menu.objects.filter(is_del=0)
        context = dict(category_list=category)
        return render(request, 'new_admin/system_category.html', context)
    else:
        return HttpResponseRedirect(reverse('new_admin:login'))


@login_required(login_url='new_admin:login')
def category_add(request):
    """
        添加栏目
        :param request:
        :return:
        """
    if request.session.get('hid', False):
        menu = Menu.objects.all()
        user_role = UserRole.objects.all()
        context = dict(role_list=user_role, menus=menu)
        return render(request, 'new_admin/system_category_add.html', context)
    else:
        return HttpResponseRedirect(reverse('new_admin:login'))


def category_add_check(request):
    """
        栏目添加检测
        :param request:
        :return:
    """
    if request.method == "POST":
        role = request.POST['role']
        if len(role) > 1:
            role = request.POST['role'][:-1]
        role_list = role.split(',')
        memu = Menu()
        memu.menu_name = request.POST['menu_name']
        memu.page_url = request.POST['page_url']
        memu.parent_id = request.POST['parent_id']
        memu.save()
        for r in role_list:
            memu.role.add(r)
            memu.save()
        messages.info(request, '添加成功')
    return redirect("new_admin:category")


def category_del(request):
    """
        栏目删除
        :param request:
        :return:
    """
    c_id = request.GET.get('c_id')
    if not c_id.isdigit():
        return JsonResponse({'status': 2, 'msg': '删除失败!'})
    try:
        menu = Menu.objects.get(id=c_id)
    except Menu.DoesNotExist:
        return JsonResponse({'status': 2, 'msg': '删除失败!'})
    else:
        menu.is_del = 1
        menu.save()
        return JsonResponse({'status': 1, 'msg': "删除成功!"})


def category_modify(request):
    """
        栏目修改
        :param request:
        :return:
    """
    if request.session.get('hid', False):
        c_id = request.GET["c_id"]
        request.session["c_id"] = c_id
        menu = Menu.objects.filter(parent_id=0).filter(is_del=0)
        user_role = UserRole.objects.all()
        c_menu = Menu.objects.get(id=c_id)
        if c_menu.parent_id == 0:
            c_menu_parent = 0
        else:
            c_menu_parent = Menu.objects.get(id=c_menu.parent_id)
        context = dict(role_list=user_role, menus=menu, c_menu=c_menu, c_menu_parent=c_menu_parent)
        return render(request, "new_admin/system_category_modify.html", context)
    else:
        return HttpResponseRedirect(reverse('new_admin:login'))


@login_required(login_url='new_admin:login')
def category_modify_check(request):
    """
        栏目修改
        :param request:
        :return:
    """
    if request.method == "POST":
        try:
            c_id = request.session.get("c_id")
        except:
            return redirect("new_admin:category")
        else:
            role = request.POST['role']
            if len(role) > 1:
                role = request.POST['role'][:-1]
            role_list = role.split(',')
            menu = Menu.objects.get(id=c_id)
            menu.menu_name = request.POST['menu_name']
            menu.page_url = request.POST['page_url']
            menu.parent_id = request.POST['parent_id']
            menu.role.set(role_list)
            menu.save()
            del request.session["c_id"]
            messages.info(request, '修改成功')
            return redirect("new_admin:category")


def dorm(request):
    """
    宿舍列表
    :param request:
    :return:
    """
    dorm_list = Dorm.objects.filter(is_del=0)
    if request.method == 'POST':
        search = request.POST.get('search')
        if search == 'true':
            dorm_list = get_date(request.POST.get('start_time'), request.POST.get('stop_time'), request.POST.get('dorm_name'))
    count = 5
    page = request.GET.get('page')
    d_list = listing(dorm_list, page, count)
    return render(request, 'new_admin/dorm_list.html', locals())


def get_date(start_time, stop_time, dorm_name):
    """
    宿舍查询
    :param start_time:
    :param stop_time:
    :param dorm_name:
    :return:
    """
    dorm_list = Dorm.objects.filter(is_del=0)
    if dorm_name:
        dorm_list = dorm_list.filter(dorm_name__contains=dorm_name)
    if start_time:
        dorm_list = dorm_list.filter(add_time__gte=start_time)
    if stop_time:
        dorm_list = dorm_list.filter(add_time__lte=stop_time)
    return dorm_list.order_by('-add_time')


def dorm_add(request):
    """
    宿舍添加
    :param request:
    :return:
    """
    if request.session.get('hid', False):
        username = request.user.username
        try:
            user = User.objects.get(username=username)
            new_user = NewUser.objects.get(user_id=user.id)
        except Exception:
            return redirect('new_admin:dorm')
        return render(request, 'new_admin/dorm_add.html', locals())
    return HttpResponseRedirect(reverse('new_admin:login'))


def dorm_add_check(request):
    """
    添加宿舍验证
    :param request:
    :return:
    """
    if request.method == 'POST':
        dorm_name = request.POST.get('dorm_name')
        username = request.session.get('username')
        max_stu = request.POST.get('max_stu')
        try:
            u = User.objects.get(username=username)
        except Exception:
            return redirect('new_admin:dorm')
        if dorm_name is None:
            messages.info(request, '请填写宿舍名！')
            return redirect(reverse("new_admin:dorm"))
        if Dorm.objects.filter(dorm_name=dorm_name).exists():
            messages.info(request, '该宿舍已存在')
            return redirect(reverse('new_admin:dorm'))
        if max_stu is None:
            messages.info(request, '请添加上限人数！')
            return redirect(reverse("new_admin:dorm"))
        Dorm.objects.create(dorm_name=dorm_name, add_user_id=u.id, max_stu=max_stu)
        messages.info(request, '添加成功！')
        return redirect('new_admin:dorm')
    return redirect('new_admin:dorm_add')


def dorm_modify(request):
    """
    宿舍修改
    :param request:
    :return:
    """
    a = request.GET.get('a')
    try:
        dorm = Dorm.objects.get(id=a)
        new_user = NewUser.objects.get(id=dorm.add_user_id)
    except Exception:
        return redirect('new_admin:dorm')
    return render(request, 'new_admin/dorm_modify.html', locals())


def dorm_modify_check(request):
    """
    宿舍修改
    :param request:
    :return:
    """
    if request.method == 'POST':
        dorm_name = request.POST.get('dorm_name')
        max_stu = request.POST.get('max_stu')
        id = request.POST.get('id')
        if dorm_name is None:
            messages.info(request, '请填写宿舍名！')
            return redirect(reverse("new_admin:dorm"))
        if max_stu is None:
            messages.info(request, '请添加上限人数！')
            return redirect(reverse("new_admin:dorm"))
        try:
            dorm = Dorm.objects.get(id=id)
        except Exception:
            return redirect(reverse("new_admin:dorm"))
        dorm.dorm_name = dorm_name
        dorm.max_stu = max_stu
        dorm.dorm_name = dorm_name
        dorm.save()
        messages.info(request, '修改成功！')
        return redirect('new_admin:dorm')
    return render(request, 'new_admin/dorm_modify.html')


def dorm_del(request):
    """
    宿舍删除
    :param request:
    :return:
    """
    a = request.GET.get('a')
    if a.isdigit():
        try:
            dorm = Dorm.objects.get(id=a)
        except Exception:
            return JsonResponse({'status': 0})
        dorm.is_del = 1
        dorm.save()
        return JsonResponse({'status': 1})
    else:
        return JsonResponse({'status': 0})


def get_time(start_date, end_date, title):
    user = User.objects.all()
    if start_date:
        user = user.filter(date_joined__gte=start_date)
    if end_date:
        user = user.filter(date_joined__lte=end_date)
    if title:
        user = user.filter(username__contains=title)
    return user


# 管理员页面
def admin(request):
    """
    管理员列表
    :param request:
    :return:
    """
    if request.session.get('hid', False):
        user_list = NewUser.objects.filter(is_del=0)
        try:
            role = UserRole.objects.get(role_name='学员')
        except Exception:
            messages.info(request, '无此权限')
            return redirect('new_admin:admin')
        username = request.user.username
        admin_list = user_list.exclude(role_id=role.id)
        if request.method == 'POST':
            realname = request.POST.get('realname')
            if realname:
                admin_list = admin_list.filter(realname__contains=realname)
        count = 5
        page = request.GET.get('page')
        a_list = listing(admin_list, page, count)
        return render(request, 'new_admin/admin_list.html', locals())
    return HttpResponseRedirect(reverse('new_admin:login'))


def admin_add(request):
    """
    管理员添加
    :param request:
    :return:
    """
    if request.session.get('hid', False):
        role_list = UserRole.objects.exclude(role_name='学员')
        return render(request, 'new_admin/admin_add.html', locals())
    return HttpResponseRedirect(reverse('new_admin:login'))


def admin_add_check(request):
    """
    管理员添加验证
    :param request:
    :return:
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        realname = request.POST.get('realname')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        info = request.POST.get('info')
        role = request.POST.get('role_id')
        id_card = request.POST.get('id_card')
        birthday = request.POST.get('birthday')
        edu_level = request.POST.get('edu_level')
        home_address = request.POST.get('home_address')
        mobile_number = request.POST.get('mobile_number')
        if username == '' or User.objects.filter(username=username).exists():
            messages.info(request, '账号不能为空或已存在')
            return redirect('new_admin:admin')
        if password == '' or password2 == '' or password != password2:
            messages.info(request, '密码不能为空或两次输入密码不一致')
            return redirect('new_admin:admin')
        if realname == '':
            messages.info(request, '真实姓名不能为空')
            return redirect('new_admin:admin')
        if email == '':
            messages.info(request, '邮箱账号不能为空')
            return redirect('new_admin:admin')
        if info == '':
            messages.info(request, '简介不能为空')
            return redirect('new_admin:admin')
        if id_card == '' or NewUser.objects.filter(id_card=id_card).exists():
            messages.info(request, '身份账号不能为空或格式不正确或身份号已存在')
            return redirect('new_admin:admin')
        if home_address == '':
            messages.info(request, '家庭地址不能为空')
            return redirect('new_admin:admin')
        if mobile_number == '' or NewUser.objects.filter(mobile_number=mobile_number).exists():
            messages.info(request, '手机号不能为空或格式不正确或手机号已存在')
            return redirect('new_admin:admin')
        try:
            role_one = UserRole.objects.get(id=role)
        except Exception:
            messages.info(request, '该角色不存在')
            return redirect('new_admin:admin')
        if role_one.role_name == '超级管理员':
            user = User.objects.create_user(username=username, password=password, email=email, is_staff=1, is_active=1, is_superuser=1)
        else:
            user = User.objects.create_user(username=username, password=password, email=email, is_staff=1, is_active=1)
        new_user = NewUser.objects.create(realname=realname, mobile_number=mobile_number, gender=gender, info=info, id_card=id_card, birthday=birthday, edu_level=edu_level, home_address=home_address, role_id=role, user_id=user.id)
        messages.info(request, '添加成功')
        return redirect('new_admin:admin')
    return redirect('new_admin:admin_add')


def admin_del(request):
    """
    删除管理员
    :param request:
    :return:
    """
    if request.session.get('hid', False):
        a = request.GET.get('a')
        b = request.GET.get('b')
        print(a, b)
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


def admin_modify(request):
    """
    修改管理员
    :param request:
    :return:
    """
    if request.session.get('hid', False):
        c = request.GET.get('c')
        if NewUser.objects.filter(id=c).exists():
            new_user = NewUser.objects.get(id=c)
            user = User.objects.get(id=new_user.user_id)
            role_list = UserRole.objects.exclude(role_name='学员')
            return render(request, 'new_admin/admin_modify.html', {'user': user, 'new_user': new_user, 'role_list': role_list})
        else:
            messages.info(request, '此用户不存在')
            return render(request, 'new_admin/admin_modify.html')
    return HttpResponseRedirect(reverse('new_admin:login'))


def admin_modify_check(request):
    if request.method == 'POST':
        realname = request.POST.get('realname')
        id_card = request.POST.get('id_card')
        email = request.POST.get('email')
        info = request.POST.get('info')
        role = request.POST.get('role_id')
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
                return redirect('new_admin:admin')
            if info == '':
                messages.info(request, '简介不能为空')
                return redirect('new_admin:admin')
            if home_address == '':
                messages.info(request, '家庭地址不能为空')
                return redirect('new_admin:admin')
            if mobile_number == '':
                messages.info(request, '手机号不能为空')
                return redirect('new_admin:admin')
            try:
                role_one = UserRole.objects.get(id=role)
            except Exception:
                messages.info(request, '该角色不存在')
                return redirect('new_admin:admin')
            if role_one.role_name == '超级管理员':
                user.is_superuser = 1
            user.email = email
            user.save()
            new_user.info = info
            new_user.id_card = id_card
            new_user.realname = realname
            new_user.birthday = birthday
            new_user.role_id = role
            new_user.edu_level = edu_level
            new_user.home_address = home_address
            new_user.mobile_number = mobile_number
            new_user.save()
            messages.info(request, '修改成功')
            return redirect('new_admin:admin')
        messages.info(request, '用户不存在')
        return redirect('new_admin:admin')
    return redirect('new_admin:admin')


def admin_start(request):
    """
    管理员账号启用
    :param request:
    :return:
    """
    e = request.GET.get('e')
    if e.isdigit():
        try:
            admin = NewUser.objects.get(id=e)
        except Exception:
            return JsonResponse({'status': 0})
        admin.user.is_active = 1
        admin.user.save()
        return JsonResponse({'status': 1})
    else:
        return JsonResponse({'status': 0})


def admin_stop(request):
    """
    管理员账号停用
    :param request:
    :return:
    """
    if request.session.get('hid', False):
        e = request.GET.get('e')
        if e.isdigit():
            try:
                admin = NewUser.objects.get(id=e)
            except Exception:
                return JsonResponse({'status': 0})
            admin.user.is_active = 0
            admin.user.save()
            return JsonResponse({'status': 1})
        else:
            return JsonResponse({'status': 0})
    return HttpResponseRedirect(reverse('new_admin:login'))


def admin_pwd_edit(request):
    """
    修改密码
    :param request:
    :return:
    """
    if request.method == 'POST':
        password = request.POST.get('newpassword')
        password2 = request.POST.get('newpassword2')
        id = request.POST.get('id')
        if password is None:
            msg = '新密码不能为空'
            return render(request, 'new_admin/admin_password_edit.html', locals())
        if password != password2:
            msg = '两次密码不一致'
            return render(request, 'new_admin/admin_password_edit.html', locals())
        try:
            user = User.objects.get(id=id)
        except Exception:
            return redirect('new_admin:login')
        user.set_password(password)
        user.save()
        messages.info(request, '修改成功')
        return redirect('new_admin:index')
    return render(request, 'new_admin/admin_password_edit.html')


@login_required(login_url='new_admin:login')
def classgrade(request):
    """
    班级列表
    :param request:
    :return:
    """
    classgrade_list = ClassGrade.objects.filter(state=0)
    return render(request, 'new_admin/system_classgrade.html', locals())


@login_required(login_url='new_admin:login')
def classgrade_add(request):
    """
    班级添加
    :param request:
    :return:
    """
    add_user = NewUser.objects.get(user=request.user)
    print("xxxxxxxxxxx:", add_user.realname)
    user_list = NewUser.objects.exclude(role__id=2)
    return render(request, 'new_admin/system_classgrade_add.html', locals())


@login_required(login_url='new_admin:login')
def classgrade_add_check(request):
    """
        班级添加检测
        :param request:
        :return:
    """
    if request.method == "POST":
        classname = request.POST['classname']
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
        class_type = request.POST['class_type']
        manager_user = request.POST['manager_user']
        teacher_user = request.POST['teacher_user']
        add_user =NewUser.objects.get(user=request.user)
        user = NewUser.objects.get(realname=add_user)
        if start_time == '' and end_time != '':
            ClassGrade.objects.create(classname=classname, end_time=end_time, class_type=class_type,
                                      add_user_id=user.id, manager_user_id=manager_user, teacher_user_id=teacher_user)
            messages.info(request, '添加成功')
            return redirect("new_admin:classgrade")
        if end_time == '' and start_time != '':
            ClassGrade.objects.create(classname=classname, start_time=start_time, class_type=class_type,
                                      add_user_id=user.id, manager_user_id=manager_user, teacher_user_id=teacher_user)
            messages.info(request, '添加成功')
            return redirect("new_admin:classgrade")
        if start_time == '' and end_time == '':
            ClassGrade.objects.create(classname=classname, class_type=class_type, add_user_id=user.id,
                                      manager_user_id=manager_user, teacher_user_id=teacher_user)
            messages.info(request, '添加成功')
            return redirect("new_admin:classgrade")
        else:
            ClassGrade.objects.create(classname=classname, start_time=start_time, end_time=end_time,
                                      class_type=class_type, add_user_id=user.id, manager_user_id=manager_user,
                                      teacher_user_id=teacher_user)
        messages.info(request, '添加成功')
        return redirect("new_admin:classgrade")
    return redirect(reverse('new_admin:classgrade_add'))


@login_required(login_url='new_admin:login')
def classsgrade_del(request):
    """
        班级删除
        :param request:
        :return:
    """
    c_id = request.GET.get('c_id')
    if not c_id.isdigit():
        return JsonResponse({'status': 2, 'msg': '删除失败!'})
    try:
        class_grade = ClassGrade.objects.get(id=c_id)
    except Menu.DoesNotExist:
        return JsonResponse({'status': 2, 'msg': '删除失败!'})
    else:
        class_grade.state = 1
        class_grade.save()
        return JsonResponse({'status': 1, 'msg': "删除成功!"})


@login_required(login_url='new_admin:login')
def classgrade_modify(request):
    """
    班级修改
    :param request:
    :return:
    """
    c_id = request.GET.get('c_id')
    class_grade = ClassGrade.objects.get(id=c_id)
    if class_grade.start_time is not None:
        class_grade.start_time = str(class_grade.start_time).split(' ')[0]
    if class_grade.end_time is not None:
        class_grade.end_time = str(class_grade.end_time).split(' ')[0]
    form = ClassGradeForm(instance=class_grade)
    return render(request, 'new_admin/system_classgrade_modify.html', locals())


@login_required(login_url='new_admin:login')
def classgrade_save(request):
    """
    班级修改保存
    :param request:
    :return:
    """
    if request.method == "POST":
        c_id = request.POST['c_id']
        class_type = request.POST['class_type']
        classgrade = ClassGrade.objects.get(id=c_id)
        post = request.POST.copy()
        post['start_time'] = post['start_time'].split(' ')[0]
        post['end_time'] = post['end_time'].split(' ')[0]
        form = ClassGradeForm(post, instance=classgrade)
        if form.is_valid():
            form.save()
            classgrade.class_type = class_type
            classgrade.save()
            messages.info(request, '修改成功')
            return redirect("new_admin:classgrade")
        else:
            messages.info(request, '修改失败,请重新操作')
            return redirect("new_admin:classgrade")
    return redirect(reverse('new_admin:classgrade'))


# 班级列表
@login_required(login_url='new_admin:login')
def classgrade(request):
    classgrade_list = ClassGrade.objects.filter(state=0)
    return render(request, 'new_admin/system_classgrade.html', locals())


# 班级添加
@login_required(login_url='new_admin:login')
def classgrade_add(request):
    add_user = NewUser.objects.get(user=request.user)
    user_list = NewUser.objects.exclude(role__id=2)
    return render(request, 'new_admin/system_classgrade_add.html', locals())


@login_required(login_url='new_admin:login')
def classgrade_search(request):
    """
    班级搜索
    :param request:
    :return:
    """
    if request.method == 'POST':
        start_time = request.POST.get('start_time', None)
        end_time = request.POST.get('end_time', None)
        name = request.POST.get('name', None)
        classgrade_list = ClassGrade.objects.filter(state=0)
        if start_time or end_time:
            if start_time:
                classgrade_list = ClassGrade.objects.filter(start_time__gte=start_time, state=0)
            else:
                classgrade_list = ClassGrade.objects.filter(end_time__lte=end_time, state=0)
        if name:
            classgrade_list = classgrade_list.filter(
                Q(classname__istartswith=name) | Q(manager_user__realname__istartswith=name) | Q(
                    teacher_user__realname__istartswith=name), state=0)
        return render(request, 'new_admin/system_classgrade.html', locals())
    return redirect(reverse('new_admin:classgrade'))


def student_list(request):
    """
    学员管理
    :param request:
    :return:
    """
    hid = request.session.get('hid', False)
    if hid is False:
        return HttpResponseRedirect(reverse("new_admin:login"))
    else:
        newusers = NewUser.objects.all()
        return render(request, "new_admin/student_list.html", locals())


def student_query(request):
    """
    学员搜索判断
    :param request:
    :return:
    """
    if request.method == "POST":
        realname = request.POST.get("realname")
        if realname == "":
            newusers = NewUser.objects.all()
            return render(request, "new_admin/student_list.html", locals())
        else:
            newusers = NewUser.objects.filter(realname__contains=realname)
            return render(request, "new_admin/student_list.html", locals())
    return redirect(reverse('new_admin:student_list'))


def student_amend(request):
    """
    学员信息修改
    :param request:
    :return:
    """
    # n_id 参数:当前选中的学员角色id
    n_id = request.GET.get("n_id")
    if n_id is None:
        return HttpResponseRedirect(reverse("new_admin:student_list"))
    if not n_id.isdigit():
        return HttpResponseRedirect(reverse("new_admin:student_list"))
    try:
        newuser = NewUser.objects.get(id=n_id)
    except NewUser.DoesNotExist:
        return HttpResponseRedirect(reverse("new_admin:student_list"))
    form = NewUserForm(instance=newuser)
    return render(request, "new_admin/student_modify.html", locals())


def student_check(request):
    """
    修改判断
    :param request:
    :return:
    """
    if request.method == "POST":
        # n_id 参数:当前选中的学员角色id
        n_id = request.POST.get("n_id")
        mobile_number = request.POST.get("mobile_number")
        id_card = request.POST.get("id_card")
        newuser = NewUser.objects.get(id=n_id)
        form = NewUserForm(request.POST,instance=newuser)
        phone_pat = re.compile('^((13[0-9])|(14[5,7])|(15[0-3,5-9])|(17[0,3 5-8])|(18[0-9])|166|198|199|(147))\\d{8}$')
        res = re.search(phone_pat,mobile_number)
        a = re.match("(/(^\d{15}$)|(^\d{18}$)|(^\d{17}(\d|X|x)$)/)",id_card)
        if res == None and a == None:
            messages.info(request, "修改失败，检查手机号与身份证是否输入正确！！")
            return HttpResponseRedirect(reverse("new_admin:student_list"))
        else:
            print(form.errors)
            if form.is_valid():
                form.save()
                messages.info(request, "修改成功")
                return redirect(reverse("new_admin:student_list"))
            else:
                messages.info(request, "修改失败")
                return redirect(reverse("new_admin:student_list"))
    return redirect(reverse('new_admin:student_list'))


def student_delete(request):
    """
    删除学员
    :param request:
    :return:
    """
    n_id = request.GET.get("n_id")
    # n_id 参数:当前选中的学员角色id
    if n_id is None:
        return JsonResponse({"status": 0, "msg": "删除失败"})
    try:
        newuser = NewUser.objects.get(id=n_id)
    except NewUser.DoesNotExist:
        return JsonResponse({"status": 0, "msg": "删除失败"})
    newuser.is_del = 1
    newuser.save()
    return JsonResponse({"status": 1, "msg": "删除成功"})

# .......................................结业模块.....................................................

def violate_punish(request):
    # 违纪，处罚
    hid = request.session.get('hid', False)
    if hid is False:
        return HttpResponseRedirect(reverse("new_admin:login"))
    else:
        punishs = Punish.objects.all()
    return render(request,"new_admin/violate_punish.html",locals())


def violate_punish_ckeck(request):
    """
    违纪，处罚搜索判断
    :param request:
    :return:
    """
    if request.method == "POST":
        realname = request.POST.get("realname")
        if realname == "":
            punishs = Punish.objects.all()
            return render(request, "new_admin/violate_punish.html", locals())
        else:
            punishs = Punish.objects.filter(student__realname__contains=realname)
            return render(request, "new_admin/violate_punish.html", locals())
    return redirect(reverse('new_admin:violate_punish'))


def subsidy(request):
    # 补贴
    hid = request.session.get('hid', False)
    t = request.GET.get("t", 1)
    if hid is False:
        return HttpResponseRedirect(reverse("new_admin:login"))
    subsidys = Subsidy.objects.filter(type=t).order_by("id")
    return render(request, "new_admin/subsidy.html", locals())


def subsidy_ckeck(request):
    """
    补贴搜索判断
    :param request:
    :return:
    """
    if request.method == "POST":
        realname = request.POST.get("realname")
        if realname == "":
            subsidys = Subsidy.objects.all()
            return render(request, "new_admin/subsidy.html", locals())
        else:
            subsidys = Subsidy.objects.filter(student__realname__contains=realname)
            return render(request, "new_admin/subsidy.html", locals())
    return redirect(reverse('new_admin:subsidy'))

def skill_grade(request):
    # 技能成绩
    hid = request.session.get('hid', False)
    if hid is False:
        return HttpResponseRedirect(reverse("new_admin:login"))
    else:
        exams = Exam.objects.all()
    return render(request,"new_admin/skill_grade.html",locals())

def skill_grade_ckeck(request):
    """
    技能成绩收搜判断
    :param request:
    :return:
    """
    if request.method == "POST":
        realname = request.POST.get("realname")
        if realname == "":
            exams = Exam.objects.all()
            return render(request, "new_admin/skill_grade.html", locals())
        else:
            exams = Exam.objects.filter(user__realname__contains=realname)
            return render(request, "new_admin/skill_grade.html", locals())
    return redirect(reverse('new_admin:skill_grade'))


def profession_grade(request):
    # 职业素养
    hid = request.session.get('hid', False)
    if hid is False:
        return HttpResponseRedirect(reverse("new_admin:login"))
    else:
        te = TestQuestion.objects.all()
        for test in te:
            a = test.review_test_id
        nb = a
        print(a)
        reviewresults = ReviewResult.objects.all()
    return render(request,"new_admin/profession_grade.html",locals())

def profession_grade_ckeck(request):
    """
    职业素养收搜判断
    :param request:
    :return:
    """
    if request.method == "POST":
        realname = request.POST.get("realname")
        if realname == "":
            reviewresults = ReviewResult.objects.all()
            return render(request, "new_admin/profession_grade.html", locals())
        else:
            reviewresults = ReviewResult.objects.filter(student__realname__contains=realname)
            return render(request, "new_admin/profession_grade.html", locals())
    return redirect(reverse('new_admin:profession_grade'))


def appraisal_report(request):
    # 评估报告
    hid = request.session.get('hid', False)
    if hid is False:
        return HttpResponseRedirect(reverse("new_admin:login"))
    else:
        exams = Exam.objects.all()
    return render(request,"new_admin/appraisal_report.html",locals())


def appraisal_report_ckeck(request):
    """
    评估报告收搜判断
    :param request:
    :return:
    """
    if request.method == "POST":
        realname = request.POST.get("realname")
        if realname == "":
            exams = Exam.objects.all()
            return render(request, "new_admin/appraisal_report.html", locals())
        else:
            exams = Exam.objects.filter(user__realname__contains=realname)
            return render(request, "new_admin/appraisal_report.html", locals())
    return redirect(reverse('new_admin:appraisal_report'))

def appraisal_detail(request):
    """
    评估报告详细
    :param request:
    :return:
    """
    hid = request.session.get('hid', False)
    if hid is False:
        return HttpResponseRedirect(reverse("new_admin:login"))
    else:
        e_id = request.GET.get("e_id")
        exams = list(Exam.objects.filter(user_id = e_id))
        ex = NewUser.objects.get(id = e_id)
    return render(request,"new_admin/detail.html",locals())


def interview_record(request):
    # 访谈记录
    hid = request.session.get('hid', False)
    if hid is False:
        return HttpResponseRedirect(reverse("new_admin:login"))
    else:
        inviews = Inview.objects.all()
    return render(request,"new_admin/interview_record.html",locals())

def interview_record_ckeck(request):
    """
    访谈记录收搜判断
    :param request:
    :return:
    """
    if request.method == "POST":
        realname = request.POST.get("realname")
        if realname == "":
            inviews = Inview.objects.all()
            return render(request, "new_admin/interview_record.html", locals())
        else:
            inviews = Inview.objects.filter(student__realname__contains=realname)
            return render(request, "new_admin/interview_record.html", locals())
    return redirect(reverse('new_admin:interview_record'))
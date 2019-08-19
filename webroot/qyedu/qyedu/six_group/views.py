from re import split
import re
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from new_admin.models import Menu, ClassGrade, Dorm, StuClass, Subsidy
from account.models import NewUser, UserRole, User
from django.contrib.auth import authenticate, login as _login, logout
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from new_admin.forms import UserForm, ClassGradeForm,NewUserForm
from django.contrib.auth.models import User
from datetime import datetime, date
from new_admin.urls import urlpatterns

from django.shortcuts import render


'''  ------------------------------------训练营-----------------------------------  '''

# 训练营
def training_camp(request):
    username = request.session.get('username')
    user = NewUser.objects.get(user__username=username)
    if request.method == 'POST':
        realname = request.POST.get('realname')
        stu_class = StuClass.objects.filter(grade__class_type=0).filter(student__state=0).filter(student__realname__contains=realname)
        return render(request, 'six_group/six_train_class.html', locals())
    stu_class = StuClass.objects.filter(grade__class_type=0).filter(student__state=0)
    return render(request, 'six_group/six_train_class.html', locals())


# 分配班级
def allocation_class(request):
    s_id = request.GET.get('s_id')
    student = NewUser.objects.get(id=s_id)
    user_role = UserRole.objects.all
    class_grade = ClassGrade.objects.filter(class_type=0)
    stu_class = StuClass.objects.all()
    return render(request, 'six_group/six_allocation_class.html', locals())


# 分配班级验证
def allocation_class_check(request):
    if request.method == 'POST':
        s_id = request.POST.get('s_id')
        class_grade = request.POST.get('class_grade')
        grade = ClassGrade.objects.get(id=class_grade)
        username = request.session.get('username')
        keyboarder = NewUser.objects.get(user__username=username)
        if StuClass.objects.filter(grade=grade, student_id=s_id):
            return redirect("six_group:training_camp")
        if StuClass.objects.filter(student_id=s_id):
            StuClass.objects.filter(student_id=s_id).update(grade=grade, keyboarder=keyboarder)
        else:
            StuClass.objects.create(grade=grade, student_id=s_id, keyboarder=keyboarder)
        return redirect("six_group:training_camp")
    return HttpResponse('非法入侵')


# 激活
def activate_state(request):
    s_id = request.GET.get('n_id')
    student = NewUser.objects.get(id=s_id)
    user_role = UserRole.objects.all
    class_grade = ClassGrade.objects.filter(class_type=1)
    stu_class = StuClass.objects.all()
    return render(request, 'six_group/six_activate_state.html', locals())


# 激活验证
def activate_state_check(request):
    username = request.session.get('username')
    user = NewUser.objects.get(user__username=username)
    if user.role_id == 4 or request.user.is_superuser:
        if request.method == 'POST':
            s_id = request.POST.get('s_id')
            class_grade = request.POST.get('class_grade')
            pay_mode = request.POST.get('mode')
            if class_grade == '0':
                messages.info(request, '请选择班级')
                return redirect("six_group:training_camp")
            elif pay_mode == '0':
                messages.info(request, '请选择缴费方式')
                return redirect("six_group:training_camp")
            grade = ClassGrade.objects.get(id=class_grade)
            username = request.session.get('username')
            keyboarder = NewUser.objects.get(user__username=username)
            StuClass.objects.filter(student_id=s_id).update(grade=grade, keyboarder=keyboarder)
            NewUser.objects.filter(id=s_id).update(pay_mode=pay_mode, state=1)
            return redirect("six_group:training_camp")
        return HttpResponse('非法入侵')
    messages.info(request, '权限不足')
    return redirect("six_group:training_camp")


# 不激活
def activate_state_not(request):
    username = request.session.get('username')
    user = NewUser.objects.get(user__username=username)
    if user.role_id == 4 or request.user.is_superuser:
        n_id = request.GET.get("n_id")
        # n_id 参数:当前选中的学员角色id
        if n_id is None:
            return JsonResponse({"status": 0, "msg": "操作失败"})
        try:
            newuser = NewUser.objects.get(id=n_id)
        except NewUser.DoesNotExist:
            return JsonResponse({"status": 0, "msg": "操作失败"})
        newuser.state = 0
        newuser.save()
        StuClass.objects.filter(student__id=n_id).delete()
        return JsonResponse({"status": 1, "msg": "恭喜你解脱啦"})
    return JsonResponse({"status": 2, "msg": "权限不足"})


# 普通班
def regular_class(request):
    username = request.session.get('username')
    user = NewUser.objects.get(user__username=username)
    if request.method == 'POST':
        realname = request.POST.get('realname')
        stu_class = StuClass.objects.filter(grade__class_type=1).filter(student__state=1).filter(student__realname__contains=realname)
        return render(request, 'six_group/six_regular_class.html', locals())
    stu_class = StuClass.objects.filter(grade__class_type=1).filter(student__state=1)
    return render(request, 'six_group/six_regular_class.html', locals())


# 学生修改
def student_mod(request):
   n_id = request.GET.get("n_id")
   if n_id is None:
       return HttpResponseRedirect(reverse("six_group:regular_class"))
   if not n_id.isdigit():
       return HttpResponseRedirect(reverse("six_group:regular_class"))
   try:
       newuser = NewUser.objects.get(id=n_id)
   except NewUser.DoesNotExist:
       return HttpResponseRedirect(reverse("six_group:regular_class"))
   form = NewUserForm(instance=newuser)
   return render(request, "six_group/six_student_mod.html", locals())


# 学生修改验证
def student_mod_check(request):
    username = request.session.get('username')
    user = NewUser.objects.get(user__username=username)
    if user.role_id == 4 or user.role_id == 8:
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
                return HttpResponseRedirect(reverse("six_group:regular_class"))
            else:
                if form.is_valid():
                    form.save()
                    messages.info(request, "修改成功")
                    return redirect(reverse("six_group:regular_class"))
                else:
                    messages.info(request, "修改失败")
                    return redirect(reverse("six_group:regular_class"))
        return redirect(reverse('six_group:regular_class'))
    messages.info(request,'权限不足')
    return redirect('six_group:regular_class')


'''  ------------------------------------补贴-----------------------------------  '''
# 补贴
def subsidy(request):
    if request.method == 'POST':
        realname = request.POST.get('realname')
        subsidy = Subsidy.objects.filter(type=1).filter(state=0).filter(student__realname__contains=realname)
        return render(request, 'six_group/six_subsidy.html', locals())
    subsidy = Subsidy.objects.filter(type=1).filter(state=0)
    return render(request, 'six_group/six_subsidy.html', locals())


# 补贴/住宿计划添加
def subsidy_add(request):
    n_id = request.GET.get('n_id')
    student = NewUser.objects.get(id=n_id)
    username = request.session.get('username')
    super = NewUser.objects.get(user__username=username)
    return render(request, 'six_group/six_subsidy_add.html', locals())


# 补贴/住宿添加计划验证
def subsidy_add_check(request):
    if request.method == 'POST':
        n_id = request.GET.get('n_id')
        student = NewUser.objects.get(id=n_id)
        type = request.POST.get('type')
        pay_time = request.POST.get('pay_time')
        if student.subsidys.first():
            subsidy = Subsidy.objects.filter(student_id=n_id, state=0, type=type)
            print(subsidy)
            a = compare(subsidy, pay_time)
            if a:
                messages.info(request, '此同学该天财务已存在,, 无需添加!!')
                if student.stuclass_student.first().grade.class_type == 0:
                    return redirect('six_group:training_camp')
                return redirect('six_group:regular_class')
        username = request.session.get('username')
        super = NewUser.objects.get(user__username=username)
        money = request.POST.get('money')
        if pay_time == '' or money == '':
            messages.info(request, '条件未添加完整')
            if student.stuclass_student.first().grade.class_type == 0:
                return redirect('six_group:training_camp')
            return redirect('six_group:regular_class')
        Subsidy.objects.create(student=student, keyboarder=super, pay_time=pay_time,money=money,type=type)
        if student.stuclass_student.first().grade.class_type == 0:
            return redirect('six_group:training_camp')
        return redirect('six_group:regular_class')
    return HttpResponse('非法入侵!!')


# 一个方法
def compare(subsidy, pay_time):
    year = int(pay_time.split('-')[0])
    month = int(pay_time.split('-')[1])
    day = int(pay_time.split('-')[2])
    for s in subsidy:
        if s.pay_time.year == year:
            if s.pay_time.month == month:
                if s.pay_time.day == day:
                    return True
    return False


# 财务修改
def subsidy_mod(request):
    s_id = request.GET.get('s_id')
    try:
        subsidy = Subsidy.objects.get(id=s_id)
        return render(request, 'six_group/six_subsidy_mod.html', locals())
    except:
        return HttpResponse('非法入侵')


# 财务修改验证
def subsidy_mod_check(request):
    if request.method == 'POST':
        s_id = request.GET.get('s_id')
        n_id = request.GET.get('n_id')
        student = NewUser.objects.get(id=n_id)
        subsidy = Subsidy.objects.filter(id=s_id)
        type = request.POST.get('type')
        pay_time = request.POST.get('pay_time')
        print(pay_time)
        username = request.session.get('username')
        super = NewUser.objects.get(user__username=username)
        money = request.POST.get('money')
        if pay_time == '' or money == '':
            messages.info(request, '条件未添加完整')
            if student.stuclass_student.first().grade.class_type == 0:
                return redirect('six_group:training_camp')
            return redirect('six_group:regular_class')
        subsidy.update(student=student, keyboarder=super, pay_time=pay_time,money=money,type=type)
        if type == 1:
            return redirect('six_group:dormitory')
        return redirect('six_group:subsidy')
    return HttpResponse('非法入侵!!')


# 住宿
def dormitory(request):
    if request.method == 'POST':
        realname = request.POST.get('realname')
        subsidy = Subsidy.objects.filter(type=2).filter(state=0).filter(student__realname__contains=realname)
        return render(request, 'six_group/six_dormitory.html', locals())
    subsidy = Subsidy.objects.filter(type=2).filter(state=0)
    return render(request, 'six_group/six_dormitory.html', locals())


# 交易记录
def dormitory_record(request):
    a_id = request.GET.get('a_id')
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        name = request.POST.get('name')
        subsidy = find(start_date, end_date, name, a_id)
        return render(request, 'six_group/six_dormitory_record.html', locals())
    subsidy = Subsidy.objects.filter(type=a_id).filter(state=1)
    return render(request, 'six_group/six_dormitory_record.html', locals())


# 记录查找
def find(start_date, end_date, name, a_id):
    subsidy = Subsidy.objects.filter(type=a_id).filter(state=1)
    if start_date:
        subsidy = subsidy.filter(close_time__gte=start_date)
    if  end_date:
        subsidy = subsidy.filter(close_time__lte=end_date)
    if name :
        subsidy = subsidy.filter(student__realname__contains=name)
    return subsidy


# 交易结算
def dormitory_close(request):
    username = request.session.get('username')
    user = NewUser.objects.get(user__username=username)
    if user.role_id == 7:
        s_id = request.GET.get("s_id")
        # s_id 参数:当前选中的财务数据id
        if s_id is None:
            return JsonResponse({"status": 0, "msg": "操作失败"})
        try:
            subsidy = Subsidy.objects.get(id=s_id)
        except :
            return JsonResponse({"status": 0, "msg": "操作失败"})
        subsidy.state = 1
        subsidy.data_time = datetime.now()
        subsidy.close_time = datetime.now()
        subsidy.save()
        return JsonResponse({"status": 1, "msg": "结算成功"})
    return JsonResponse({"status": 2, "msg": "权限不足"})


# 删除财务记录
def remove_subsidy(request):
    username = request.session.get('username')
    user = NewUser.objects.get(user__username=username)
    if user.role_id == 6 or user.role_id == 8:
        s_id = request.GET.get("s_id")
        # s_id 参数:当前选中的财务数据id
        if s_id is None:
            return JsonResponse({"status": 0, "msg": "操作失败"})
        try:
            subsidy = Subsidy.objects.filter(id=s_id)
        except:
            return JsonResponse({"status": 0, "msg": "删除失败"})
        subsidy.delete()
        return JsonResponse({"status": 1, "msg": "删除成功"})
    return JsonResponse({"status": 2, "msg": "权限不足"})


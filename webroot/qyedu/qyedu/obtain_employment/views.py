from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render,redirect,reverse
from django.http import JsonResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from account.models import NewUser
from .models import Suggestion_employment_record as Records, VisitedRecord,Enterprise
from .forms import EnterpriseForm
import re, os


@login_required(login_url='new_admin:login')
def graduate(request):
    # 毕业学生表
    username = request.session.get('username')
    u_id = NewUser.objects.get(user__username=username).role_id
    if u_id != 8:
        ab = 1
        user_list = NewUser.objects.filter(role_id=2).filter(state=2)
        return render(request, 'job/stu-list.html', locals())
    user_list = NewUser.objects.filter(role_id=2).filter(state=2)
    return render(request, 'job/stu-list.html', locals())

@login_required(login_url='new_admin:login')
def work_records(request):
    # 就业记录
    username = request.session.get('username')
    u_id = NewUser.objects.get(user__username=username).role_id
    if u_id != 8:
        ab = 1
    job_result = Records.objects.all()
    return render(request, 'job/records-list.html', locals())


@login_required(login_url='new_admin:login')
def add_records(request, id=0):
    """
    添加就业回访记录
    :param request:
    :param id:
    :return:
    """
    username = request.user.username
    u_id = request.user.newuser.role.id
    if u_id != 8:
        ab = 1
    newuser = NewUser.objects.get(pk=id) if int(id) else None
    recorder = request.user.newuser
    return render(request, 'job/records-add.html', locals())


@login_required(login_url='new_admin:login')
def add_records_check(request):
    # 添加验证

    if request.method == 'POST':
        v_name = request.POST.get('student_name')
        v_student = NewUser.objects.filter(realname=v_name, is_del=0)
        if v_student:
            v_student = v_student[0]
        else:
            messages.info(request, '该学生姓名不存在。请检查是否未录入该生信息')
            return redirect(reverse('job:add_records', kwargs={'id': 0}))
        com_name = request.POST.get('company_name')
        com_address = request.POST.get('company_address')
        emp_result = request.POST.get('employment_result')
        stu_feedback = request.POST.get('student_feedback')
        # rec_person_id = request.POST.get('rec_id')
        # s_name_id = request.POST.get('stu_id')
        if com_name != '' and com_address != '' and emp_result != '' and stu_feedback != '':
            
            Records.objects.create(e_name=com_name, e_address=com_address, emp_result=emp_result,
                                   stu_feedback=stu_feedback, record_person=request.user.newuser,
                                   s_name=v_student)
            messages.info(request, '添加记录成功')
            return redirect(reverse('job:work_records'))

    return render(request, 'job/records-list.html')


@login_required(login_url='new_admin:login')
def change_records(request, id):
    #修改记录验证
    if id.isdigit():
        if Records.objects.filter(id=id).exists():
            records = Records.objects.get(pk=id)
            return render(request, 'job/records-change.html', locals())
    messages.info(request,'您输入信息不存在')
    return render(request, 'job/records-list.html')

@login_required(login_url='new_admin:login')
def change_records_check(request):
    #修改记录验证
    if request.method == 'POST':
        com_name = request.POST.get('company_name')
        com_address = request.POST.get('company_address')
        emp_result = request.POST.get('employment_result')
        stu_feedback = request.POST.get('student_feedback')
        # rec_person_id = request.POST.get('rec_name')
        # s_name_id = request.POST.get('stu_name')
        r_id = request.POST.get('r_id')
        v_name = request.POST.get('student_name')
        v_student = NewUser.objects.filter(realname=v_name, is_del=0)
        if v_student:
            v_student = v_student[0]
        else:
            messages.info(request, '该学生姓名不存在。请检查是否未录入该生信息')
            return redirect(reverse('job:change_records', kwargs={'id': r_id}))
        if com_name != '' and com_address != '' and emp_result != '' and stu_feedback != '':
            if Records.objects.filter(pk=r_id).exists():
                records=Records.objects.get(pk=r_id)
                records.e_name = com_name
                records.e_address = com_address
                records.emp_result = emp_result
                records.s_name = v_student
                records.record_person = request.user.newuser
                records.stu_feedback = stu_feedback
                records.save()
                messages.info(request, '修改记录成功')
                return redirect(reverse('job:work_records'))
    return render(request, 'job/records-add.html')

@csrf_exempt
@login_required(login_url='new_admin:login')
def delete_records(request):
    #删除已添加的记录
    if request.method == 'POST':
        id = int(request.POST.get('id'))
        if 'id' in request.POST and id != '':
            Records.objects.filter(id=id).delete()
            num = Records.objects.all().count()
            return JsonResponse({'status':'1','msg': '删除成功','num':num})
    return JsonResponse({'status':'0','msg':'删除失败'})

def add_yan(request):
    username = request.session.get('username')
    u_id = NewUser.objects.get(user__username=username).role_id
    if u_id != 8:
        return JsonResponse({'status':'1','msg': '你没有操作权限'})
    else:
        return JsonResponse({'status':'0'})


@login_required(login_url='new_admin:login')
def records_search(request):
    if request.method == 'POST':
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        search = request.POST.get('search')
        if start_time or end_time:
            if start_time:
                job_result = Records.objects.filter(add_time__gte=start_time)
            else:
                job_result = Records.objects.filter(add_time__lte=end_time)
        if search:
            job_result = Records.objects.filter(
                Q(e_name__icontains=search) | Q(record_person__realname__icontains=search) | Q(
                    s_name__realname__icontains=search))
        return render(request, 'job/records-list.html', locals())
    return render(request, 'job/records-list.html', locals())

# ----------------------上面添加就业记录-------------



# 展示就业学生列表
@login_required(login_url='new_admin:login')
def job_students(request):
    username = request.session.get('username')
    u_id = NewUser.objects.get(user__username=username).role_id
    if u_id != 8:
        ab=1
    job_result = Records.objects.all()
    return render(request, 'job/job_stu_list.html', locals())


# 回访记录
@login_required(login_url='new_admin:login')
def visited(request):
    """
    回放记录
    :param request:
    :return:
    """
    username = request.session.get('username')
    u_id = NewUser.objects.get(user__username=username).role_id
    if u_id != 8:
        ab = 1
    visite_list = VisitedRecord.objects.all().order_by("-id")
    return render(request, 'job/visited_list.html', locals())


@login_required(login_url='new_admin:login')
def visited_add(request, id):
    """
    添加就业回放记录
    :param request:
    :param id:
    :return:
    """
    username = request.user.username
    u_id = request.user.newuser.role.id
    if u_id == 8:
        newuser = Records.objects.get(pk=id) if int(id) else None
        
        recorder = request.user.newuser
    
    return render(request, 'job/visited_add.html', locals())


@login_required(login_url='new_admin:login')
def visited_add_check(request):
    if request.method == 'POST':
        v_name = request.POST.get('v_name')
        v_student = NewUser.objects.filter(realname=v_name, is_del=0)
        if v_student:
            v_student = v_student[0]
        else:
            messages.info(request, '该学生姓名不存在。请检查是否未录入该生信息')
            return redirect(reverse('job:visited'))
        v_del_method = request.POST.get('v_del_method')
        
        talents = request.POST.get('talents', 0)
        visited_info = request.POST.get('visited_info')
        if v_del_method != '' and visited_info != '' and talents != '':
            VisitedRecord.objects.create(v_del_method=v_del_method, if_join_talentpool=talents,
                                         visited_info=visited_info, record_person=request.user.newuser,
                                         v_name=v_student)
            messages.info(request, '添加记录成功')
            return redirect(reverse('job:visited'))
        
    return render(request, 'job/records-add.html')




@login_required(login_url='new_admin:login')
def visited_modify(request,id):
    if VisitedRecord.objects.filter(pk=id).exists():
        visite= VisitedRecord.objects.get(pk=id)
        return render(request,'job/Visited_modify.html',locals())
    return redirect(reverse('job:visited'))

@login_required(login_url='new_admin:login')
def visited_modify_check(request):
    if request.method == 'POST':
        v_name_id = request.POST.get('stu_id')
        rec_person_id = request.POST.get('rec_id')
        v_del_method = request.POST.get('v_del_method')
        add_time = request.POST.get('add_time')
        talents = request.POST.get('talents')
        v_id = request.POST.get('v_id')
        visited_info = request.POST.get('visited_info')
        if v_name_id != '' and v_del_method != '' and add_time != '' and visited_info != '' and rec_person_id != '' and talents != '' and v_id != '':
            if rec_person_id.isdigit() and v_name_id.isdigit() and VisitedRecord.objects.filter(pk=v_id).exists():
                visited = VisitedRecord.objects.get(pk=v_id)
                visited.v_del_method=v_del_method
                visited.if_join_talentpool=talents
                visited.visited_info=visited_info
                visited.add_time=add_time,
                visited.record_person_id=rec_person_id
                visited.v_name_id=v_name_id
                visited.save()
                messages.info(request, '修改记录成功')
                return redirect(reverse('job:visited'))
        else:
            return render(request, 'job/Visited_modify.html')
    return render(request, 'job/Visited_modify.html')

@csrf_exempt
def delete_visited(request):
    if request.method == 'POST':
        id = int(request.POST.get('id'))
        if 'id' in request.POST and id != '':
            VisitedRecord.objects.filter(id=id).delete()
            num = VisitedRecord.objects.all().count()
            return JsonResponse({'status':'1','msg': '删除成功','num':num})
    return JsonResponse({'status':'0','msg':'删除失败'})

@login_required(login_url='new_admin:login')
def search_visited(request):
    if request.method == 'POST':
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        search = request.POST.get('search')
        if start_time or end_time:
            if start_time:
                visite_list = VisitedRecord.objects.filter(add_time__gte=start_time)
            else:
                visite_list = VisitedRecord.objects.filter(add_time__lte=end_time)
        if search:
            visite_list = VisitedRecord.objects.filter(
                Q(v_name__realname__icontains=search) | Q(record_person__realname__icontains=search) | Q(
                    visited_info__icontains=search))
        return render(request, 'job/visited_list.html', locals())
    return render(request, 'job/visited_list.html', locals())


# --------------------- 上面是回访记录----------
#---------------------- 下面是录入企业信息------------
def enterprise(request):
    '''
    企业库列表
    :param request:
    :return:
    '''
    if request.method == 'POST':
        start_time = request.POST.get('start_time')
        stop_time = request.POST.get('stop_time')
        enter_name = request.POST.get('enter_name')
        enterprise_list = get_enterprise(start_time, stop_time, enter_name)
        return render(request, 'job/enterprise_list.html', locals())
    enterprise_list = Enterprise.objects.all()
    return render(request, 'job/enterprise_list.html', locals())


def get_enterprise(start_time,stop_time,enter_name):
    """
    企业搜索
    :param request:
    :return:
    """
    enterprise_list = Enterprise.objects.all()
    if enter_name:
        enterprise_list = enterprise_list.filter(e_name__contains=enter_name)
    if start_time:
        enterprise_list = enterprise_list.filter(add_time__gte=start_time)
    if stop_time:
        enterprise_list = enterprise_list.filter(add_time__lte=stop_time)
    return enterprise_list


def enterprise_add(request):
    '''
    企业添加
    :param request:
    :return:
    '''
    form = EnterpriseForm()
    return render(request, 'job/enterprise_add.html', locals())


def enterprise_check(request):
    '''
    企业添加验证
    :param request:
    :return:
    '''
    if request.method == 'POST':
        form = EnterpriseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, '添加成功！')
            return redirect('job:enterprise')
        else:
            messages.info(request, '添加失败!请重新输入...')
            return redirect('job:enterprise_add')
    return redirect('job:enterprise_add')


def enterprise_modify(request):
    '''
    企业信息修改
    :param request:
    :return:
    '''
    form = EnterpriseForm()
    e_id = request.GET.get("e_id")
    # e_id = int(e_id)
    if e_id is None:
        return HttpResponseRedirect(reverse("job:enterprise"))
    if not e_id.isdigit():
        return HttpResponseRedirect(reverse("job:enterprise"))
    try:
        newuser = Enterprise.objects.get(id=e_id)
    except NewUser.DoesNotExist:
        return HttpResponseRedirect(reverse("job:enterprise"))
    form = EnterpriseForm(instance=newuser)
    photo = newuser.e_prtocol
    return render(request, "job/enterprise_modify.html", locals())


def enterprise_modify_check(request):
    '''
    企业修改验证
    :param request:
    :return:
    '''
    if request.method == "POST":
        e_id = request.POST.get('e_id')
        e_contact_phone = request.POST.get("e_contact_phone")
        new = Enterprise.objects.get(id=e_id)
        p_path = str(new.e_prtocol)
        form = EnterpriseForm(request.POST,request.FILES,instance=new)
        phone_pat = re.compile('^((13[0-9])|(14[5,7])|(15[0-3,5-9])|(17[0,3 5-8])|(18[0-9])|166|198|199|(147))\\d{8}$')
        res = re.search(phone_pat,e_contact_phone)
        if res == None:
            messages.info(request, "修改失败，检查手机号是否输入正确！！")
            return HttpResponseRedirect(reverse("job:enterprise"))
        else:
            if form.is_valid():
                p1_path = settings.MEDIA_ROOT+p_path
                if p_path != '':
                    if os.path.exists(p1_path):
                        os.remove(p1_path)
                form.save(commit=True)
                messages.info(request, "修改成功")
                return redirect("job:enterprise")
            else:
                messages.info(request, "修改失败")
                return redirect(reverse("job:enterprise"))
    return redirect(reverse('job:enterprise'))


def enterprise_del(request):
    """
        企业删除
        :param request:
        :return:
    """
    e_id = request.GET.get('e_id')
    if not e_id.isdigit():
        return JsonResponse({'status': 2, 'msg': '删除失败!'})
    try:
        enterprise = Enterprise.objects.get(id=e_id)
    except NewUser.DoesNotExist:
        return JsonResponse({'status': 2, 'msg': '删除失败!'})
    else:
        enterprise.delete()
        return JsonResponse({'status': 1, 'msg': "删除成功!"})
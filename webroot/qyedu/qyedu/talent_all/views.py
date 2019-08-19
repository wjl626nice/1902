# coding=utf8
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, reverse


from account.models import NewUser
from talent_all.models import Talent, Tag


def talent_list(request):
    if request.session.get('hid', False):
        t_list = Talent.objects.filter(is_del=0)
        return render(request, 'talent_all/talent_list.html', {"t_list": t_list})
    return HttpResponseRedirect(reverse('new_admin:login'))


# 标签列表
def tag_list(request):
    if request.session.get('hid', False):
        t_list = Tag.objects.filter(is_del=0)
        return render(request, 'talent_all/tag_list.html', locals())
    return HttpResponseRedirect(reverse('new_admin:login'))


def talent_add(request):
    return render(request, 'talent_all/talent_add.html')


def talent_delete(request):
    if request.session.get('hid', False):
        t_id = request.GET.get('t_id')
        if Talent.objects.filter(id=t_id):
            talent = Talent.objects.get(id=t_id)
            talent.is_del = 1
            talent.save()
            return JsonResponse({'status': 1, 'msg': '已删除'})
    return JsonResponse({'status': 0, 'msg': '删除失败,位置错误'})


def tag_add(request):
    if request.session.get('hid', False):
        username = request.session.get('username')
        user = User.objects.get(username=username)
        new_user = user.newuser
        print(request.GET.get('s'))
        if str(request.GET.get('s')) == 'None':
            s_id = request.GET.get('s_id')
            tag_list = Tag.objects.filter(is_del=0)
            return render(request, 'talent_all/tag_add.html', locals())
        else:
            return render(request, 'talent_all/tag_add_to.html', locals())
    return HttpResponseRedirect(reverse('new_admin:login'))


def tag_delete(request):
    if request.session.get('hid', False):
        t_id = request.GET.get('t_id')
        if Tag.objects.filter(id=t_id):
            tag = Tag.objects.get(id=t_id)
            tag.is_del = 1
            tag.save()
            return JsonResponse({'status': 1, 'msg': '已删除'})
    return JsonResponse({'status': 0, 'msg': '删除失败,位置错误'})


def tag_modify(request):
    return render(request, 'talent_all/tag_modify.html')


def tag_show(request):
    if request.session.get('hid', False):
        s_id = request.GET.get('s_id')
        student = NewUser.objects.get(id=s_id)
        talent = Talent.objects.get(student_id_id=s_id)
        return render(request, 'talent_all/talent_detail.html', locals())
    return HttpResponseRedirect(reverse('new_admin:login'))


# 打标签
def tag_save(request):
    if request.session.get('hid', False):
        if request.method == 'POST':
            id_list = request.POST.get('tag').split(',')
            name = request.POST.get('tag_name')
            username = request.session.get('username')
            user = User.objects.get(username=username)
            s_id = request.POST.get('s_id')
            talent = Talent.objects.get(student_id_id=s_id)
            if name != '':
                if name in [tag.name for tag in Tag.objects.filter(is_del=0)]:
                    messages.info(request, '添加的标签已存在')
                else:
                    tag = Tag()
                    tag.name = name
                    new_user = user.newuser
                    tag.Recruiter_id = new_user
                    tag.save()
                    talent.tags.add(tag)
            for id in id_list:
                if id != '':
                    tag1 = Tag.objects.get(id=id)
                    if tag1 in talent.tags.all():
                        messages.info(request, '添加的标签已存在')
                    else:
                        talent.tags.add(tag1)
            return HttpResponseRedirect(reverse('talent:talent_list'))
    return HttpResponseRedirect(reverse('new_admin:login'))


# 添加标签2
def tag_save_to(request):
    if request.session.get('hid', False):
        if request.method == 'POST':
            name = request.POST.get('tag_name')
            username = request.session.get('username')
            user = User.objects.get(username=username)
            new_user = user.newuser
            if name != '':
                if name in [tag.name for tag in Tag.objects.all()]:
                    messages.info(request, '添加的标签已存在')
                else:
                    tag = Tag()
                    tag.name = name
                    tag.Recruiter_id = new_user
                    tag.save()
            return HttpResponseRedirect(reverse('talent:tag_list'))
    return HttpResponseRedirect(reverse('new_admin:login'))

# 搜索人才
def student_query(request):
    pass


# 搜索标签
def tag_query(request):
    pass


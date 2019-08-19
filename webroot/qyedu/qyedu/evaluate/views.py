from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from evaluate.forms import AnswerForm
from django.http import JsonResponse
from new_admin.models import *
from evaluate.models import *


def evaluate_test_show(request):
    review_test_list = ReviewTest.objects.all()
    context = dict(review_test_list=review_test_list)
    return render(request, 'evaluate/test_show.html', context)

 
def evaluate_test_add(request):
    """
    :param request:
    :return:
    """
    class_grade_list = ClassGrade.objects.all()
    teacher_list = NewUser.objects.all()
    return render(request, 'evaluate/test_add.html', locals())


def evaluate_test_add_check(request):
    if request.method == 'POST':
        class_id = request.POST.get('class_id')
        test_name = request.POST.get('test_name')
        test_date = request.POST.get('test_date')
        teacher_id = request.POST.get('teacher_id')
        if not class_id:
            messages.info(request, '没有班级')
            return redirect('evaluate:evaluate_test')
        if not test_name:
            messages.info(request, '没有姓名')
            return redirect('evaluate:evaluate_test')
        if not test_date:
            messages.info(request, '没有日期')
            return redirect('evaluate:evaluate_test')
        if not teacher_id:
            messages.info(request, '没有选择老师')
            return redirect('evaluate:evaluate_test')
        if ReviewTest.objects.filter(test_name=test_name).exists():
            messages.info(request, '已存在')
            return redirect('evaluate:evaluate_test')
        review_test = ReviewTest()
        review_test.class_grade_id = int(class_id)
        review_test.test_name = test_name
        review_test.review_test_date = test_date
        review_test.teacher_name_id = int(teacher_id)
        review_test.save()
        return redirect('evaluate:evaluate_test_show')
    return render(request, 'evaluate/test_add.html', locals())



def evaluate_test_modify(request):
    test_info_id = request.GET.get('test_info_id')
    test_info = ReviewTest.objects.get(id=test_info_id)
    class_grade_list = ClassGrade.objects.all()
    teacher_list = NewUser.objects.all()
    can_test = request.session.get('can_test', False)
    context = dict(test_info=test_info, class_grade_list=class_grade_list, teacher_list=teacher_list, can_test=can_test)
    return render(request, 'evaluate/test_modify.html', context)



def evaluate_test_modify_check(request):
    if request.method == 'POST':
        test_info_id = request.GET.get('t_info')
        class_id = request.POST.get('class_id')
        test_name = request.POST.get('test_name')
        test_date = request.POST.get('test_date')
        teacher_id = request.POST.get('teacher_id')
        can_test = request.POST.get('can_test')
        if not class_id:
            messages.info(request, '没有班级')
            return redirect('evaluate:evaluate_test')
        if not test_name:
            messages.info(request, '没有名称')
            return redirect('evaluate:evaluate_test')
        if not test_date:
            messages.info(request, '没有日期')
            return redirect('evaluate:evaluate_test')
        if not teacher_id:
            messages.info(request, '没有选择老师')
            return redirect('evaluate:evaluate_test')
        review_test = ReviewTest.objects.get(id=test_info_id)
        review_test.class_grade_id = int(class_id)
        review_test.test_name = test_name
        review_test.review_test_date = test_date
        review_test.teacher_name_id = int(teacher_id)
        if can_test == 'on':
            request.session['can_test'] = can_test
            review_test.can_test = 1
        else:
            if request.session.get('can_test'):
                del request.session['can_test']
            review_test.can_test = 0
        review_test.save()
        return redirect('evaluate:evaluate_test_show')
    return redirect('evaluate:evaluate_test_modify')



def evaluate_test_delete(request):
    test_info_id = request.GET.get('test_info')
    if not test_info_id.isdigit():
        return JsonResponse({'status': 2, 'msg': '数据错误'})
    try:
        test_info = ReviewTest.objects.get(id=test_info_id)
    except ReviewTest.DoesNotExist:
        return JsonResponse({'status': 2, 'msg': 'ɾ��ʧ��'})
    test_info.delete()
    return JsonResponse({'status': 1, 'msg': 'ɾ���ɹ�'})


def evaluate_test_question(request):
    question_list = TestQuestion.objects.all()
    return render(request, 'evaluate/test_question.html', locals())


def evaluate_test_question_add(request):
    print(request.session.get('can_test'))
    if request.session.get('can_test'):
        messages.info(request, '���ڿ���,�������')
        return redirect('evaluate:evaluate_test_question')
    test_list = ReviewTest.objects.all()
    return render(request, 'evaluate/test_question_add.html', locals())



# ����--��Ŀ���
def evaluate_test_question_add_check(request):
    if request.method == 'POST':
        test_id = request.POST.get('test_id')
        test_type_id = request.POST.get('test_type_id')
        question_type_id = request.POST.get('question_type_id')
        test_content = request.POST.get('test_content')
        test_score = request.POST.get('test_score')
        if not test_id:
            messages.info(request, '�������Ʋ���Ϊ��')
            return redirect('evaluate:evaluate_test_question')
        if not test_type_id:
            messages.info(request, '�������Ͳ���Ϊ��')
            return redirect('evaluate:evaluate_test_question')
        if not question_type_id:
            messages.info(request, '��Ŀ���Ͳ���Ϊ��')
            return redirect('evaluate:evaluate_test_question')
        if not test_content:
            messages.info(request, '�������ݲ���Ϊ��')
            return redirect('evaluate:evaluate_test_question')
        if not test_score:
            messages.info(request, '���Է�������Ϊ��')
            return redirect('evaluate:evaluate_test_question')
        test_question = TestQuestion()
        test_question.review_test_id = test_id
        test_question.test_category = test_type_id
        test_question.test_question_category = question_type_id
        test_question.test_question_content = test_content
        test_question.max_score = test_score
        test_question.save()
        return redirect('evaluate:evaluate_test_question')
    return render(request, 'evaluate/test_question.html', locals())


# �����޸Ŀ���ҳ��
def evaluate_test_question_modify(request):
    if request.session.get('can_test'):
        test_id = request.GET.get('test_id')
        test = TestQuestion.objects.get(id=test_id)
        test_list = ReviewTest.objects.all()
        context = dict(test_list=test_list, test=test)
        return render(request, 'evaluate/test_question_modify.html', context)
    messages.info(request, '���ڿ���,�����޸�')
    return redirect('evaluate:evaluate_test_question')


# �޸Ŀ���
def evaluate_test_question_modify_check(request):
    if request.method == 'POST':
        test_id = request.POST.get('test_id')
        t_id = request.GET.get('t_id')
        test_type_id = request.POST.get('test_type_id')
        question_type_id = request.POST.get('question_type_id')
        test_content = request.POST.get('test_content')
        test_score = request.POST.get('test_score')
        if not test_id:
            messages.info(request, '�������Ʋ���Ϊ��')
            return redirect('evaluate:evaluate_test_question')
        if not test_type_id:
            messages.info(request, '�������Ͳ���Ϊ��')
            return redirect('evaluate:evaluate_test_question')
        if not question_type_id:
            messages.info(request, '��Ŀ���Ͳ���Ϊ��')
            return redirect('evaluate:evaluate_test_question')
        if not test_content:
            messages.info(request, '�������ݲ���Ϊ��')
            return redirect('evaluate:evaluate_test_question')
        if not test_score:
            messages.info(request, '���Է�������Ϊ��')
            return redirect('evaluate:evaluate_test_question')
        test_question = TestQuestion.objects.get(id=t_id)
        test_question.review_test_id = test_id
        test_question.test_category = test_type_id
        test_question.test_question_category = question_type_id
        test_question.test_question_content = test_content
        test_question.max_score = test_score
        test_question.save()
    return redirect('evaluate:evaluate_test_question')


# ɾ������
def evaluate_question_delete(request):
    if request.session.get('can_test'):
        test_id = request.GET.get('test_id')
        if not test_id.isdigit():
            return JsonResponse({'status': 2, 'msg': 'ɾ��ʧ��'})
        try:
            test = TestQuestion.objects.get(id=test_id)
        except ReviewTest.DoesNotExist:
            return JsonResponse({'status': 2, 'msg': 'ɾ��ʧ��'})
        test.delete()
        return JsonResponse({'status': 1, 'msg': 'ɾ���ɹ�'})
    messages.info(request, '���ڿ���,����ɾ��')
    return redirect('evaluate:evaluate_test_question')


# �����������ҳ��
def evaluate_test_answer(request):
    if request.session.get('hid', False):
        answer_list = Answer.objects.all()
        return render(request, 'evaluate/answer.html', locals())
    return HttpResponseRedirect(reverse('new_admin:login'))


# ������Ӵ�ҳ��
def evaluate_test_answer_add(request):
    # ������Ŀչʾ
    if request.session.get('hid', False):
        test_question_list = TestQuestion.objects.all()
        return render(request, 'evaluate/answer_add.html', locals())
    return HttpResponseRedirect(reverse('new_admin:login'))


# ��Ӵ�
def evaluate_test_answer_add_check(request):
    if request.session.get('hid', False):
        if request.method == 'POST':
            question = request.POST.get('question')
            # ��������Ϊ��
            answer_content = request.POST.get('answer_content')
            answer_score = request.POST.get('answer_score')
            if not question:
                messages.info(request, '��ѡ������Ŀ')
                return HttpResponseRedirect(reverse('evaluate:evaluate_test_answer'))
            if not answer_score:
                messages.info(request, '����д�𰸷���, ��Ҫ������߷���')
                return HttpResponseRedirect(reverse('evaluate:evaluate_test_answer'))
            answer = Answer()
            answer.question_id = question
            answer.answer_content = answer_content
            answer.answer_score = answer_score
            answer.save()
            return HttpResponseRedirect(reverse('evaluate:evaluate_test_answer'))
        return HttpResponse('�Ƿ�����!!!!!!!')
    return HttpResponseRedirect(reverse('new_admin:login'))


# չʾ���޸�ҳ��
def evaluate_test_answer_modify(request):
    if request.session.get('hid', False):
        a_id = request.GET.get('a_id')
        if a_id.isdigit():
            answer = Answer.objects.get(id=a_id)
            answer_form = AnswerForm(instance=answer)
            return render(request, 'evaluate/answer_modify.html', locals())
        return HttpResponseRedirect(reverse('evaluate:evaluate_test_answer'))
    messages.info(request, '�Ƿ�����!�����µ�¼')
    return HttpResponseRedirect(reverse('new_admin:login'))


# �ύ���޸�
def evaluate_test_answer_modify_check(request):
    if request.session.get('hid', False):
        if request.method == 'POST':
            a_id = request.POST.get('a_id')
            if a_id.isdigit():
                answer = Answer.objects.get(id=a_id)
                answer_form = AnswerForm(request.POST, instance=answer)
                if answer_form.is_valid():
                    answer_form.save()
                messages.info(request, '���޸ĳɹ�!')
                return HttpResponseRedirect(reverse('evaluate:evaluate_test_answer'))
            messages.info(request, '��ȡ��������ȷ, �޷�ɾ��!')
            return HttpResponseRedirect(reverse('evaluate:evaluate_test_answer'))
        messages.info(request, '�Ƿ�����!�����µ�¼')
        return HttpResponseRedirect(reverse('new_admin:login'))
    messages.info(request, '�Ƿ�����!�����µ�¼')
    return HttpResponseRedirect(reverse('new_admin:login'))


# ɾ�������
def evaluate_test_answer_delete(request):
    if request.session.get('hid', False):
        a_id = request.GET.get('a_id')
        print(a_id)
        if a_id.isdigit():
            answer = Answer.objects.get(id=a_id)
            # answer.question.delete()
            answer.delete()
            messages.info(request, '��ɾ��!')
            return HttpResponseRedirect(reverse('evaluate:evaluate_test_answer'))
        messages.info(request, '��ȡ��������ȷ, �޷�ɾ��!')
        return HttpResponseRedirect(reverse('evaluate:evaluate_test_answer'))
    messages.info(request, '�Ƿ�����!�����µ�¼')
    return HttpResponseRedirect(reverse('new_admin:login'))


# ְҵ������----�Ծ�չʾ
def evaluate_course_test_show(request):
    question_list = TestQuestion.objects.filter(test_category=4)[0]
    question_type1 = TestQuestion.objects.filter(test_category=4).filter(test_question_category=1)
    question_type2 = TestQuestion.objects.filter(test_category=4).filter(test_question_category=2)
    question_type3 = TestQuestion.objects.filter(test_category=4).filter(test_question_category=3)
    context = dict(test_category=question_list, question_type1=question_type1, question_type2=question_type2, question_type3=question_type3)
    return render(request, 'evaluate/course_test_show.html', context)


# ְҵ������----�����ύ
def evaluate_course_test_submit(request):
    question_list = TestQuestion.objects.filter(test_category=4)[0]
    review_test = question_list.review_test
    username = request.session.get('username')
    student = NewUser.objects.get(user__username=username)
    if StudentAnswer.objects.filter(student_id=student.id):
        return HttpResponse('�ѿ���!')
    if request.method == 'POST':
        for k,v in request.POST.items():
            if k != 'csrfmiddlewaretoken':
                k = int(k.split('_')[1])
                answer = v
                question = TestQuestion.objects.get(id=k)
                StudentAnswer.objects.create(review_test=review_test, student=student, answer=answer, question=question)
        return redirect('evaluate:evaluate_course_test_answer')


# ְҵ�����ο���----��չʾ
def evaluate_course_test_answer(request):
    username = request.session.get('username')
    student = NewUser.objects.get(user__username=username)
    answer_list = StudentAnswer.objects.filter(student_id=student.id).filter(question__test_category=4)
    answer_list1 = StudentAnswer.objects.filter(student_id=student.id).filter(question__test_category=4)[0]
    score_list = []
    for s_answer in answer_list:
        for answer in s_answer.question.a_question.all():
            if answer.question.test_question_category != 3:
                score_list.append(answer.answer_score)
    sum_score = sum(score_list)
    return render(request, 'evaluate/course_test_answer.html', locals())


def evaluate_teacher_test(request):
    """
    讲师评测
    :param request:
    :return:
    """
    if TestQuestion.objects.filter(test_category=1):
        teacher_test1 = TestQuestion.objects.filter(test_category=1)[0]
        teacher_test = TestQuestion.objects.filter(test_category=1).filter(test_question_category=1)
        teacher_test2 = TestQuestion.objects.filter(test_category=1).filter(test_question_category=2)
        teacher_test3 = TestQuestion.objects.filter(test_category=1).filter(test_question_category=3)
        answer = Answer.objects.filter()
        return render(request, 'evaluate/teacher_test.html', locals())
    else:
        messages.info(request, '没有数据')
        return HttpResponseRedirect(reverse('evaluate:evaluate_test_question'))


def evaluate_teacher_test_submit(request):
    """
    讲师评测提交
    :param request:
    :return:
    """
    teacher_test1 = TestQuestion.objects.filter(test_category=1)[0]
    review_test = teacher_test1.review_test
    username = request.session.get('username')
    student = NewUser.objects.get(user__username=username)
    if StudentAnswer.objects.filter(student_id=student.id):
        return HttpResponse('学生答案已存在')
    if request.method == 'POST':
        print(request.POST)
        print(request.POST.items())
        for k,v in request.POST.items():
            if k != 'csrfmiddlewaretoken':
                k = int(k.split('_')[1])
                answer = v
                # question = Answer.objects.get(id=k).question
                question = TestQuestion.objects.get(id=k)
                StudentAnswer.objects.create(question=question,student=student,answer=answer,review_test=review_test)
        return redirect('evaluate:evaluate_student_answer')


def evaluate_student_answer(request):
    print('------------------------')
    username = request.session.get('username')
    print(username)
    student = NewUser.objects.get(user__username=username)
    student_answer = StudentAnswer.objects.filter(student_id=student.id).filter(question__test_category=1)
    student_answer1 = StudentAnswer.objects.filter(student_id=student.id).filter(question__test_category=1)[0]
    score_list = []
    for s_answer in student_answer:
        for answer in s_answer.question.a_question.all():
            if answer.question.test_question_category != 3:
                score_list.append(answer.answer_score)
    sum_score = sum(score_list)
    return render(request, 'evaluate/student_answer.html', locals())


def evaluate_headteacher_test(request):
    """
    班主任评测
    :param request:
    :return:
    """
    if TestQuestion.objects.filter(test_category=2):
        headteacher_test = TestQuestion.objects.filter(test_category=2)[0]
        headteacher_test1 = TestQuestion.objects.filter(test_category=2).filter(test_question_category=1)
        headteacher_test2 = TestQuestion.objects.filter(test_category=2).filter(test_question_category=2)
        headteacher_test3 = TestQuestion.objects.filter(test_category=2).filter(test_question_category=3)
        context = dict(headteacher_test=headteacher_test, headteacher_test1=headteacher_test1, headteacher_test2=headteacher_test2, headteacher_test3=headteacher_test3)
        return render(request, 'evaluate/headteacher_test.html', context)
    messages.info(request, '评测')
    return HttpResponseRedirect(reverse('evaluate:evaluate_test_question'))


def evaluate_headteacher_test_submit(request):
    """
    班主任评测提交
    :param request:
    :return:
    """
    if TestQuestion.objects.filter(test_category=2):
        headteacher_test = TestQuestion.objects.filter(test_category=2)[0]
        review_test = headteacher_test.review_test
        username = request.session.get('username')
        # user = User.objects.get(username=username)
        # student = NewUser.objects.get(user_id=user.id)
        if username is not None:
            student = NewUser.objects.get(user__username=username)
        else:
            messages.info(request, '用户名不能为空')
            return HttpResponseRedirect(reverse('new_admin:login'))
        if request.method == 'POST':
            for k, v in request.POST.items():
                if k != 'csrfmiddlewaretoken':
                    k = int(k.split('_')[1])
                    answer = v
                    # question = Answer.objects.get(id=k).question
                    question = TestQuestion.objects.get(id=k)
                    review_test = question.review_test
                    StudentAnswer.objects.create(review_test=review_test, question=question, answer=answer, student=student)
            messages.info(request, '操作成功')
            return HttpResponseRedirect(reverse('evaluate:evaluate_headteacher_test_answer'))
        return HttpResponse('操作错误')
    messages.info(request, '不存在')
    return HttpResponseRedirect(reverse('evaluate:evaluate_test_question'))



def evaluate_headteacher_test_answer(request):
    """
    班主任评测结果
    :param request:
    :return:
    """
    username = request.session.get('username')
    student = NewUser.objects.get(user__username=username)
    student_answer = StudentAnswer.objects.filter(student_id=student.id).filter(question__test_category=2)
    student_answer1 = StudentAnswer.objects.filter(student_id=student.id).filter(question__test_category=2)[0]
    score_list = []
    for s_answer in student_answer:
        
        for answer in Answer.objects.filter(answer_content=s_answer.answer):
            
            if answer.question.test_question_category != 3:
                score_list.append(answer.answer_score)
    sum_score = sum(score_list)
    return render(request, 'evaluate/ht_student_answer.html', locals())


def evaluate_headteacher_test_sum(request):
    """
    班主任评测
    :param request:
    :return:
    """
    review_test_score = request.GET.get('sum')
    test_category = request.GET.get("test_category")
    test_name = request.GET.get('test_name')
    review_test = ReviewTest.objects.get(test_name=test_name)
    student_id = request.GET.get('s_id')
    student = NewUser.objects.get(id=student_id)
    ReviewResult.objects.create(review_test_score=review_test_score,test_category=test_category,review_test=review_test, student=student)
    return JsonResponse({'data': review_test_score})


def show_all(request):
    return render(request, 'evaluate/show_all.html', locals())


def evaluate_service_test(request):
    """
    后勤评测
    :param request:
    :return:
    """
    question_list = TestQuestion.objects.filter(test_category=3)[0]

    type_list1 = TestQuestion.objects.filter(test_category=3).filter(test_question_category=1)
    type_list2 = TestQuestion.objects.filter(test_category=3).filter(test_question_category=2)
    type_list3 = TestQuestion.objects.filter(test_category=3).filter(test_question_category=3)
    context = dict(question_list=question_list, type_list1=type_list1, type_list2=type_list2, type_list3=type_list3)
    return render(request, 'evaluate/service_test_show.html', context)



def evaluate_service_test_submit(request):
    """
    后勤评测提交
    :param request:
    :return:
    """
    question_list = TestQuestion.objects.filter(test_category=3)[0]
    review_test = question_list.review_test
    username = request.session.get('username')
    student = NewUser.objects.get(user__username=username)
    if StudentAnswer.objects.filter(student_id=student.id):
        return HttpResponse('已提交过')
    if request.method == 'POST':
        for k,v in request.POST.items():
            if k != 'csrfmiddlewaretoken':
                k = int(k.split('_')[1])
                answer = v
                question = TestQuestion.objects.get(id=k)
                StudentAnswer.objects.create(review_test=review_test, student=student, question=question, answer=answer)
        return redirect('evaluate:evaluate_service_test_answer')


def evaluate_service_test_answer(request):
    """
    后勤评测答案
    :param request:
    :return:
    """
    username = request.session.get('username')
    student = NewUser.objects.get(user__username=username)
    answer_list = StudentAnswer.objects.filter(student_id=student.id).filter(question__test_category=3)
    answer_list1 = StudentAnswer.objects.filter(student_id=student.id).filter(question__test_category=3)[0]
    score_list = []
    for s_answer in answer_list:
        for answer in s_answer.question.a_question.all():
            if answer.question.test_question_category != 3:
                score_list.append(answer.answer_score)
    sum_score = sum(score_list)
    return render(request, 'evaluate/service_test_answer.html', locals())

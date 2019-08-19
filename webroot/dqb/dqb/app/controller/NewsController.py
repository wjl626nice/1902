from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from base.myjson import JSONResponse
from app.model.NewsModel import QyNews,News_getRespondent,News_getApplicant
from app.model.MemberModel import QyMember
from base.my_page import mypage
import json,time

# Create your views here.



@csrf_exempt
def friendApplication(request):
    '''
    查询'球友'发送来的申请
    :param request:
    :return:
    '''
    if request.method == 'GET':
        try:
            page = request.GET.get('page')
            openid = request.GET.get('respondent_openid')
            id = QyMember.objects.get(openid=openid).id
            objs = QyNews.objects.filter(respondent_id=int(id))

            p = mypage(page,objs)
            obj = p.get('page_list')
            total = p.get('page_sum')

            serializer = News_getApplicant(obj,many=True)
            return JSONResponse(0,serializer.data,total)
        except:
            return JSONResponse(1007)
    else:
        return JSONResponse(1054)



@csrf_exempt
def myApplication(request):
    '''
    查询'本人'发出的申请信息
    :param request:
    :return:
    '''
    if request.method == 'GET':
        try:
            page = request.GET.get('page')
            openid = request.GET.get('applicant_openid')
            id = QyMember.objects.get(openid=openid).id
            objs = QyNews.objects.filter(applicant_id=int(id))

            p = mypage(page,objs)
            obj = p.get('page_list')
            total = p.get('page_sum')

            serializer = News_getRespondent(obj,many=True)
            return JSONResponse(0,serializer.data,total)
        except:
            return JSONResponse(1007)
    else:
        return JSONResponse(1054)



@csrf_exempt
def news_create(request):
    '''
    创建申请信息
    :param request:
    :return:
    '''
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            applicant_openid = data.get('applicant_openid')
            applicant_id = QyMember.objects.get(openid=applicant_openid).id
            respondent_id = data.get('respondent_id')
            # 申请人 与 被申请人 不能一致
            if applicant_id == respondent_id:
                return JSONResponse(1005)
            with transaction.atomic():
                # 创建申请信息
                obj = QyNews(
                    applicant_id = applicant_id,
                    respondent_id = respondent_id,
                    content = data.get('content'),
                    apply_time = str(int(time.time())),
                )
                obj.save()
                objs = QyNews.objects.get(pk=obj.pk)
                serializer = News_getRespondent(objs, many=False)
                return JSONResponse(0, serializer.data)
        except:
            return JSONResponse(1007)
    else:
        return JSONResponse(1055)


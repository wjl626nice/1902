from django.urls import path
from app.controller.NewsController import friendApplication,\
    news_create,\
    myApplication

app_name = 'group'


urlpatterns = [
    # 查询 球友发送来的申请
    path('application/',friendApplication),

    # 创建申请信息
    path('create/',news_create),

    # 查询 本人发出的申请信息
    path('respondent/',myApplication),
]

from django.urls import path
from app.controller.ReplayController import get_replyAll,create_reply

app_name = "reply"

urlpatterns = [
    # 查询 指定留言下的所有回复
    # path('getAll/',get_replyAll,name='reply'),

    # 创建回复信息
    path('create/',create_reply)
]

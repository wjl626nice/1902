from django.urls import path
from app.controller.MessageController import getMessageAll,createMessage,delete_message

app_name = "message"

urlpatterns = [
    # 获取指定活动下的所有留言
    path('getAll/',getMessageAll),

    # 在指定活动下创建留言
    path('create/',createMessage),

    # 删除留言
    path('delete/',delete_message),
]

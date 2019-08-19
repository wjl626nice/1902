from django.urls import path
from app.controller.GroupController import myGroup,\
    create_myfriends,\
    common_friend,\
    delete_myfriends,\
    up_myGroup


app_name = "group"

urlpatterns = [
    # 查询 我的球友
    path('myGroup/',myGroup),

    # 同意添加球友
    path('create/',create_myfriends),

    # 查询 共同球友
    path('common/',common_friend),

    # 删除球友
    path('delete/',delete_myfriends),

    # 修改分组/标签
    path('up/',up_myGroup)
]

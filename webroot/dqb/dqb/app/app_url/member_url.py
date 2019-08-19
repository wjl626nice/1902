from django.urls import path
from app.controller.MemberController import MemberRegistration,\
    get_member_info,\
    change_member_info,\
    UserGetOpenID,\
    Transaction_details,\
    select_member_list,\
    Boolean

app_name = "member"

urlpatterns = [
    # 根据前端code码返回相应的openID
    path('userGetOpenID/',UserGetOpenID,name='userGetOpenID'),
    # 用户登录时拉取用户信息
    path('member/',MemberRegistration,name='member'),
    # 获取当前用户信息
    path('getMemberInfo/',get_member_info,name='get_member_info'),
    # 根据请求信息对当前用户信息进行更改
    path('changeMemberInfo/',change_member_info,name='change_member_info'),
    # 根据条件获取指定用户列表
    path('memberSelect/',select_member_list,name='memberSelect'),
    # 获取当前用户所有交易明细
    path('transactionDetails/',Transaction_details,name='transactionDetails'),
    # 返回审核状态
    path('boolean/',Boolean,name='boolean'),
]

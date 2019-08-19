from django.urls import path
from app.controller.RechargeController import get_recharge_record,\
    get_recharge_details,\
    select_recharge_record,\
    Weixin_recharge,\
    Callback_verification

app_name = "recharge"

urlpatterns = [
    # 创建充值记录
    # path('createRecharge/',create_recharge_record,name='createRecharge'),
    # 获取当前用户所有充值记录
    path('getRecordList/',get_recharge_record,name='getRecordList'),
    # 获取当前提现充值详情
    path('getDetails/',get_recharge_details,name='getDetails'),
    # 根据条件获取指定充值列表
    path('selectRecordList/',select_recharge_record,name='selectRecordList'),
    # 微信支付
    path('rechargePay/',Weixin_recharge,name='rechargePay'),
    # 微信支付成功回调
    path('callback/',Callback_verification),
]
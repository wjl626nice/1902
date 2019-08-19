from django.urls import path
from app.controller.PutForwardController import get_info,\
    create_put_forward_record,\
    update_put_forward_record,\
    get_bank

app_name = "put_forward"

urlpatterns = [
    # 获取用户'持卡人','身份证号','银行卡号','银行预留手机号'
    path('getInfo/',get_info,name='getInfo'),
    # 创建提现记录
    path('createPutForward/',create_put_forward_record,name='createPutForward'),
    # 修改提现记录状态
    path('updatePutForward/',update_put_forward_record,name='updatePutForward'),
    path('get_bank/',get_bank)
]
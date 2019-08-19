from app.model.PayModel import QyPay,PaySerializer
from app.model.MemberModel import QyMember,MemberPayment
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from base.myjson import JSONResponse
import requests
import json
import time


@csrf_exempt
def get_info(request):
    '''
    获取用户'持卡人','身份证号','银行卡号','银行预留手机号'
    :param request:
    :return:
    '''
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            open_id = data.get('openid')
            # 获取登录用户
            user = QyMember.objects.get(openid=open_id)
            with transaction.atomic():
                user.cardholder = data.get('cardholder',user.cardholder)
                user.ID_number = data.get('ID_number',user.ID_number)
                user.opening_bank = data.get('opening_bank',user.opening_bank)
                user.bank_card_number = data.get('bank_card_number',user.bank_card_number)
                user.reserved_phone_number = data.get('reserved_phone_number',user.reserved_phone_number)
                user.save()
            users = QyMember.objects.get(openid=open_id)
            serializer = MemberPayment(users, many=False)
            return JSONResponse(0, serializer.data)
        except:
            return JSONResponse(1000)
    else:
        return JSONResponse(1054)


@csrf_exempt
def create_put_forward_record(request):
    '''
    创建提现记录
    :param request:
    :return:
    '''
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            out_trade_no = str(int(time.time() * 1000000))
            with transaction.atomic():
                member = QyMember.objects.get(openid=data.get('openid'))
                if eval(member.balance) < eval(data.get('pay_amount')):
                    return JSONResponse(2003)
                else:
                    member.balance = "%.2f" % (eval(member.balance) - eval(data.get('pay_amount')))
                    member.save()
                    pay = QyPay(
                        pay_type=2,
                        out_trade_no=out_trade_no,
                        member_id=member.id,
                        pay_amount="%.2f" % eval(data.get('pay_amount')),
                        pay_state=data.get('pay_state'),
                        add_time=int(time.time())
                    )
                    pay.save()
                    serializer = PaySerializer(pay, many=False)
                    return JSONResponse(0, serializer.data)
        except:
            return JSONResponse(1000)
    else:
        return JSONResponse(1054)


@csrf_exempt
def update_put_forward_record(request):
    '''
    修改提现记录状态
    :param request:
    :return:
    '''
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            with transaction.atomic():
                info = QyPay.objects.get(pk=data.get('id'),pay_type=2)
                if data.get('pay_state') == 3:
                    info.pay_state = data.get('pay_state', info.pay_state)
                    info.save()
                elif data.get('pay_state') == 1:
                    user = QyMember.objects.get(pk=info.member_id)
                    user.balance = "%.2f" % (eval(user.balance) + eval(info.pay_amount))
                    user.save()
                    info.pay_state = data.get('pay_state', info.pay_state)
                    info.save()
            infoes = QyPay.objects.get(pk=info.pk)
            serializer = PaySerializer(infoes, many=False)
            return JSONResponse(0, serializer.data)
        except:
            return JSONResponse(1010)
    else:
        return JSONResponse(1054)


@csrf_exempt
def get_bank(request):
    '''
    验证银行卡
    :param request:
    :return:
    '''
    if request.method == 'POST':
        data = json.loads(request.body)
        url = "https://ccdcapi.alipay.com/validateAndCacheCardInfo.json"
        params = {
            "_input_charset": "utf-8",
            "cardNo": data.get('cardNo'),
            "cardBinCheck": "true",
        }
        try:
            bank = requests.get(url=url, params=params).json()["bank"]
            return JSONResponse(0,{'bank':bank})
        except:
            return JSONResponse(2004)

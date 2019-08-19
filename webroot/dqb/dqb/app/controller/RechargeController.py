from django.views.decorators.csrf import csrf_exempt
from app.model.PayModel import QyPay,PaySerializer
from app.model.MemberModel import QyMember
from django.shortcuts import HttpResponse
from base.ergodic import Pay_ergodic
from base.myjson import JSONResponse
from django.db import transaction
from base.my_page import mypage
from base.Var import wx
import json
import time


@csrf_exempt
def get_recharge_record(request):
    '''
    获取当前用户所有充值/提现记录
    :param request:
    :return:
    '''
    if request.method == 'GET':
        try:
            member_id = QyMember.objects.get(openid=request.GET.get('openid')).id
            obj = QyPay.objects.filter(member_id=member_id,pay_type=request.GET.get('pay_type')).order_by('-id')
            # 进行分页
            pag = mypage(request.GET.get('page'), obj)
            serializer = PaySerializer(pag['page_list'], many=True)
            return JSONResponse(0, serializer.data, pag['page_sum'],pag['page_count'])
        except:
            return JSONResponse(1000)
    else:
        return JSONResponse(1054)


@csrf_exempt
def get_recharge_details(request):
    '''
    获取当前提现充值/提现详情
    :param request:
    :return:
    '''
    if request.method == 'GET':
        try:
            obj = QyPay.objects.get(pk=request.GET.get('id'),pay_type=request.GET.get('pay_type'))
            serializer = PaySerializer(obj, many=False)
            return JSONResponse(0, serializer.data)
        except:
            return JSONResponse(1010)
    else:
        return JSONResponse(1054)


@csrf_exempt
def select_recharge_record(request):
    '''
    根据条件获取指定充值/提现列表
    :param request:
    :return:
    '''
    if request.method == 'POST':
        try:
            state = json.loads(request.body).get('pay_state')
            phone_num = json.loads(request.body).get('phoneNum')
            nick_name = json.loads(request.body).get('nickName')
            pay_type = json.loads(request.body).get('pay_type')
            if state and (not nick_name) and (not phone_num):
                recharge_list = QyPay.objects.filter(pay_state=state,pay_type=pay_type).order_by('-id')
            elif nick_name and (not state) and (not phone_num):
                member_list = QyMember.objects.filter(nickname__contains=nick_name)
                recharge_list = Pay_ergodic(member_list,pay_type)
            elif phone_num and (not nick_name) and (not state):
                member_list = []
                for x in QyMember.objects.filter(phonenum__isnull=False):
                    if str(x.phonenum).__contains__(str(phone_num)):
                        member_list.append(x)
                recharge_list = Pay_ergodic(member_list,pay_type)
            elif state and nick_name:
                member_list = QyMember.objects.filter(nickname__contains=nick_name)
                recharge_list = Pay_ergodic(member_list,pay_type,state)
            elif state and phone_num:
                member_list = []
                for x in QyMember.objects.filter(phonenum__isnull=False):
                    if str(x.phonenum).__contains__(str(phone_num)):
                        member_list.append(x)
                recharge_list = Pay_ergodic(member_list,pay_type,state)
            else:
                recharge_list = QyPay.objects.filter(pay_type=pay_type).order_by('-id')
            # 进行分页
            pag = mypage(json.loads(request.body).get('page'), recharge_list)
            serializer = PaySerializer(pag['page_list'], many=True)
            return JSONResponse(0, serializer.data, pag['page_sum'], pag['page_count'])
        except:
            return JSONResponse(1000)
    else:
        return JSONResponse(1054)


@csrf_exempt
def Weixin_recharge(request):
    '''
    微信充值并创建充值记录
    :param request:
    :return:
    '''
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            price = int(data.get('price') * 100)
            if price < 1:
                return JSONResponse(1047)
            out_trade_no = str(int(time.time() * 1000000))
            request_info = {
                'trade_type': 'JSAPI',  # 签名类型
                'out_trade_no': out_trade_no,  # 定单号
                'total_fee': price,  # 充值金额 分为单位
                'openid': data.get('openid'),
                'body': '点球吧用户充值',
            }
            # 生成统一下单请求:(交易类型,定单号,标价金额,用户标识,通知地址)
            unifiedorder = wx.unifiedorder(**request_info)

            if unifiedorder.result['return_code'] == 'SUCCESS':  # 如果请求成功
                if unifiedorder.result['result_code'] == 'SUCCESS':  # 业务结果
                    prepay_id = 'prepay_id={}'.format(unifiedorder.prepay_id)
                    timestamp = str(int(time.time()))
                    info = {
                        "appId": unifiedorder.result['appid'],
                        "nonceStr": wx.random_str(),
                        "package": prepay_id,
                        "signType": "MD5",
                        "timeStamp": timestamp
                    }
                    paySign = wx._gen_sign(info)
                    info['paySign'] = paySign
                    with transaction.atomic():
                        member_id = QyMember.objects.get(openid=data.get('openid')).id
                        user = QyPay(
                            pay_type=1,
                            out_trade_no=out_trade_no,
                            member_id=member_id,
                            pay_amount="%.2f" % float(data.get('price')),
                            pay_state=2,
                            add_time=int(time.time())
                        )
                        user.save()
                    # 签名后返回给前端做支付参数
                    return JSONResponse(0, info)
                else:
                    return JSONResponse(1046)
        except:
            return JSONResponse(1000)
    else:
        return JSONResponse(1054)


@csrf_exempt
def Callback_verification(request):
    '''
    微信支付成功回调验证
    :param request:
    :return:
    '''
    if request.method == 'POST':
        try:
            request.data = request.body
            callback_info = wx.verify_notify(request)
            if callback_info.result['return_code'] == 'SUCCESS':
                if callback_info.result['result_code'] == 'SUCCESS':
                    with transaction.atomic():
                        obj = QyPay.objects.get(out_trade_no=callback_info.result['out_trade_no'])
                        obj.pay_state = 3
                        obj.save()
                        user = QyMember.objects.get(pk=obj.member_id)
                        user.balance = "%.2f" % (eval(user.balance) + eval(obj.pay_amount))
                        user.save()
                    info = {
                        "return_code": callback_info.result['return_code'],
                        "return_msg": 'OK',
                    }
                    return HttpResponse(wx.to_xml(info))
                else:
                    return JSONResponse(1046)
        except Exception as e:
            print(e)
            return JSONResponse(1000)
    else:
        return JSONResponse(1054)


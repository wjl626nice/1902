from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.conf import settings
from geetest import GeetestLib
from putao.models import *
import hashlib

from utils import common as lscommon


# Create your views here.
# 后台视图

def admin_login(request):
    return render(request, 'admin/admin_login.html')


def admin_menu(request):
    """
    提供后台菜单
    :param request:
    :return:
    """
    return JsonResponse(settings.MENU)


def admin_pcgetcaptcha(request):
    """
    获取极验官方的的一些参数
    :param request:
    :return:
    """
    user_id = 'test'
    gt = GeetestLib(settings.GEETEST['id'], settings.GEETEST['key'])
    status = gt.pre_process(user_id)
    request.session[gt.GT_STATUS_SESSION_KEY] = status
    request.session["user_id"] = user_id
    response_str = gt.get_response_str()
    return HttpResponse(response_str)


def admin_check(request):
    """
    检测登录返回状态
    :param request:
    :return:
    """

    # 账号
    account = request.POST.get('username', None).strip()
    # 密码
    pwd = request.POST.get('password', None).strip()

    # 极验 验证start
    gt = GeetestLib(settings.GEETEST['id'], settings.GEETEST['key'])
    challenge = request.POST.get(gt.FN_CHALLENGE, '')
    validate = request.POST.get(gt.FN_VALIDATE, '')
    seccode = request.POST.get(gt.FN_SECCODE, '')
    status = request.session[gt.GT_STATUS_SESSION_KEY]
    user_id = request.session["user_id"]
    if status:
        result = gt.success_validate(challenge, validate, seccode, user_id)
    else:
        result = gt.failback_validate(challenge, validate, seccode)
    # 极验 验证end
    # result： True验证通过,False 验证没有通过
    if not result:
        return JsonResponse(lscommon.get_json_error('验证码错误', 1001))

    # # 验证码
    # code = request.POST.get('code').strip()
    # # 判断验证码是否存在
    # if not code:
    #     return '验证码不能为空！'
    # # 验证码是否输入正确
    # if code.lower() != request.session.get('verifys').lower():
    #     return '验证码不正确，请重新输入！'

    # 账号 或者密码不能为空
    if not account or not pwd:
        return JsonResponse(lscommon.get_json_error('账号或者密码不能为空!', 1002))
    # 从数据库获取指定账号的信息
    adminInfo = Admin.objects.filter(account=account).values('id', 'account', 'pwd', 'login_ip', 'login_num')
    if len(adminInfo) <= 0:
        return JsonResponse(lscommon.get_json_error('该账号不存在!', 1003))
    # 对前台传递过来的密码进行hash
    pwd = settings.SALT + pwd + settings.SALT
    # 参与哈希运算
    md5 = hashlib.md5()
    md5.update(pwd.encode('utf-8'))
    # 获取哈希后的密文
    pwd = md5.hexdigest()
    # 验证密码是否正确
    if adminInfo[0]['pwd'] != pwd:
        return JsonResponse(lscommon.get_json_error('密码错误!', 1004))

    # 生成令牌的字符串
    sign = settings.SALT + str(datetime.time()) + settings.SALT
    # 参与哈希运算
    md5 = hashlib.md5()
    md5.update(sign.encode('utf-8'))
    # 获取哈希后的密文
    access_token = md5.hexdigest()
    # 当用户登录成功时 要保存当前用户的身份令牌
    admin = Admin.objects.get(id=adminInfo[0]['id'])
    admin.access_token = access_token
    admin.save()

    result = {
        "code": 0
        , "msg": "登录成功"
        , "data": {
            "access_token": access_token
        }
    }
    return JsonResponse(result)


def admin_info(request):
    access_token = request.POST.get('access_token', None)
    if not access_token:
        return JsonResponse(lscommon.get_json_error('身份令牌不能为空！请重新登录获取！', 1004))

    # 根据身份令牌在管理员表中获取当前管理员
    adminInfo = Admin.objects.get(access_token=access_token)
    result = {
        "code": 0
        , "msg": ""
        , "data": {
            "username": adminInfo.nickname
            , "sex": "男"
            , "role": 1
        }
    }
    return JsonResponse(result)

def admin_changepwd(request):
    """
    修改密码接口
    :param request:
    :return:
    """
    # 获取令牌
    access_token = request.POST.get('access_token', None)
    if not access_token:
        return JsonResponse(lscommon.get_json_error('身份令牌不能为空！请重新登录获取！', 1004))
    # 获取当前用户密码
    oldpassword = request.POST.get('oldPassword')
    if not oldpassword:
        return JsonResponse(lscommon.get_json_error('请输入当前密码！', 1005))

    # 获取新密码
    password = request.POST.get('password')
    # 获取确认密码
    repassword = request.POST.get('repassword')
    # 两个新密码不能为空
    if not password or not repassword:
        return JsonResponse(lscommon.get_json_error('新密码不能为空！', 1007))
    # 判断两个新密码是否一致
    if password != repassword:
        return JsonResponse(lscommon.get_json_error('两次输入的新密码不一样！', 1008))

    # 对前台传递过来的密码进行hash
    pwd = settings.SALT + oldpassword + settings.SALT
    # 参与哈希运算
    md5 = hashlib.md5()
    md5.update(pwd.encode('utf-8'))
    # 获取哈希后的密文
    oldpassword = md5.hexdigest()
    # 根据身份令牌和密码在管理员表中获取当前管理员
    adminInfo = Admin.objects.filter(access_token=access_token, pwd=oldpassword)
    if not adminInfo:
        return JsonResponse(lscommon.get_json_error('当前密码不正确！', 1006))

    # 对前台传递过来的密码进行hash
    password = settings.SALT + password + settings.SALT
    # 参与哈希运算
    md5 = hashlib.md5()
    md5.update(pwd.encode('utf-8'))
    # 获取哈希后的密文
    password = md5.hexdigest()
    # 把新的密码 更新到当前用户表中
    adminInfo[0].pwd = password
    adminInfo[0].save()

    result = {
        "code": 0
        , "msg": "修改成功！"
        , "data": {
        }
    }
    return JsonResponse(result)


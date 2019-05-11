#!/usr/bin/python3

import smtplib
from email.mime.text import MIMEText
from email.header import Header
import randomcc

# 第三方 SMTP 服务
# mail_host = "smtp.XXX.com"  # 设置服务器
# mail_user = "XXXX"  # 用户名
# mail_pass = "XXXXXX"  # 口令不是自己的登录密码，而是
mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "779646692@qq.com"  # 用户名
mail_pass = "esqljpjmbfzwbehi"  # 口令不是自己的登录密码，而是授权码

sender = '779646692@qq.com'


def sendCheckCodeFromEmail(receiver):
    receivers = [receiver]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    # 验证码
    checkcode = randomcc.checkCode()

    ccstring = "图书馆系统会员找回密码 验证码：" + checkcode

    message = MIMEText(ccstring, 'plain', 'utf-8')
    message['From'] = sender
    message['To'] = ';'.join(receivers)

    subject = '图书管理系统，找回密码'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())

        # print(checkcode)
        print("邮件发送成功")
        return checkcode
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")


# sendCheckCodeFromEmail("1036052028@qq.com")
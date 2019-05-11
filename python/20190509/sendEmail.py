#!/usr/bin/python3

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
# mail_host = "smtp.XXX.com"  # 设置服务器
# mail_user = "XXXX"  # 用户名
# mail_pass = "XXXXXX"  # 口令不是自己的登录密码，而是授权码

# qq 邮箱
# mail_host = "smtp.qq.com"  # 设置服务器
# mail_user = "779646692@qq.com"  # 用户名
# mail_pass = "esqljpjmbfzwbehi"  # 口令不是自己的登录密码，而是授权码
# sender = '779646692@qq.com'

# 163邮箱
mail_host = "smtp.163.com"  # 设置服务器
mail_user = "wangjl626@163.com"  # 用户名
mail_pass = "leo18625521061"  # 口令不是自己的登录密码，而是授权码
sender = 'wangjl626@163.com'

receivers = ['1036052028@qq.com',  "wangjl@hnqingyun.com", "lisuchen002@vip.qq.com"]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText('验证码 8548', 'plain', 'utf-8')

message['From'] = sender
message['To'] = ';'.join(receivers)

subject = '测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except EOFError:
    print(EOFError)
    print("Error: 无法发送邮件")
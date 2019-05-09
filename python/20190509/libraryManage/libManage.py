from userManage import *

menu = (("会员注册", 0), ("会员登录", 1),("密码找回", 2), ("退出系统", 3))

while True:
    for x in menu:
        print("{}:{}".format(x[0], x[1]))

    index = int(input("请选择功能:"))

    if index == 0:
        register()
    elif index == 1:
        login()
    elif index == 2:
        findPwd()
    elif index == 3:
        logout()

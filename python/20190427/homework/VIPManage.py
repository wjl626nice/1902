# 注册
def register():
    print("注册")

    un = input("请输入用户名:")
    pwd = input("请输入密码:")
    role1 = input("请输入你的角色")

    # 判断用户名和密码是否符合要求
    # 判断用户名是否存在
    f = open("./db/user_info.txt", "r")
    users = f.readlines()
    f.close()

    # 用户名不存在
    unIsExist = False
    for u in users:
        tempUn = u.split("|")[0]
        if tempUn == un:
            unIsExist = True
            break

    # 用户名不存在，把用户名和密码存储到 ./db/user_info.txt ，注册成功
    '''
    用户名|密码|权限|....
    '''
    if not unIsExist:
        str1 = un + "|" + pwd + "|" + "1" + "\n"
        f = open("./db/user_info.txt", "a")
        f.write(str1)
        f.close()

        print("注册成功")
    else:
        # 用户名存在，那么提示用户名已存在，注册失败
        print("用户名已存在，注册失败")


# 登录
def login():
    print("登录")
    pass


# 会员管理
def vipManage():
    print("会员管理")
    pass


# 注销登录
def logout():
    print("注销登录")
    pass


menu = (("会员注册", 0), ("会员登录", 1), ("会员管理", 2), ("注销登录", 3))

for x in menu:
    print("{}:{}".format(x[0], x[1]))

index = int(input("请选择功能:"))

if index == 0:
    register()
elif index == 1:
    login()
elif index == 2:
    vipManage()
elif index == 3:
    logout()

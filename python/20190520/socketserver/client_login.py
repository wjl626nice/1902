import socket
import json
# 登录客户端

username = input('用户名:')
password = input('密码:')

def get_conn():
    # 封装了sk的初始化，返回一个套接字
    sk = socket.socket()
    sk.connect(('', 8888))
    return sk

# 判断用户名和密码是否为空
if username.strip() and password.strip():
    # 获取套接字对象
    sk = get_conn()
    # 把用户名和密码拼接成字典，然后在转换成json字符串
    userInfo = json.dumps({'username': username, 'password': password})
    sk.send(bytes(userInfo, 'utf-8'))
    sk.close()
import socketserver
import json
import hashlib

# 盐  目的：增加密码长度和破解难度
salt = b'abcd'
def get_md5(password):
    # hashlib对象
    hashObj = hashlib.md5()
    hashObj.update(salt)
    hashObj.update(password.encode())
    # 对盐和密码生成hash哈希值（密文）
    return hashObj.hexdigest()

def login(userInfo):
    # 登录处理
    # 把json字符串转换成json对象
    userInfo = json.loads(userInfo)
    # 对密码进行hash哈希，生成哈希值
    newPwd = get_md5(userInfo['password'])
    with open('userInfo', 'r') as handler:
        # 循环读取文件内的数据（一次一行）
        for line in handler:
            user, pwd = line.strip().split('|')  # [用户名，密码]
            print(user, userInfo['username'])
            print(pwd, newPwd)
            if user == userInfo['username'] and newPwd == pwd:
                print('登录成功！')
                break
        else:
            print('登录失败！')



# 负责接收socket客户端传过来的值
class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        # self.request 跟平常的 conn一样
        # 获取用户名和密码
        userInfo = self.request.recv(1024).decode('utf-8')
        login(userInfo)

if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('', 8888),MyServer)
    server.serve_forever()
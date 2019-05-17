import socket, subprocess
from socket import SO_REUSEADDR, SOL_SOCKET
# 创建套接字
sk = socket.socket()
sk.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
# 绑定端口和ip
sk.bind(('', 12345))
# 监听
sk.listen()
# 阻塞登录客户端连接
conn, addr = sk.accept()  # 三次握手

while True:
    # 接收客户端信息
    command = conn.recv(1024)
    # cd 命令执行待解决
    sp = subprocess.Popen(command, shell=True,
                          stdout=subprocess.PIPE,  # 成功执行以后把结果放入管道
                          stderr=subprocess.PIPE  # 执行错误把结果放入管道
                          )
    # sp.stdout.read() 获取到的内容是字节
    stdout = sp.stdout.read()  # 管道只能使用一次

    # 判断命令执行的结果
    if stdout.decode():
        msg_len = str(len(stdout))
        # 在发送内容之前先把内容的长度发送给客户端
        conn.send(msg_len.encode())
        conn.recv(1024)  # 解决黏包
        # 发送命令执行的结果
        conn.send(stdout)
    # 获取执行错误的结果
    stderr = sp.stderr.read()
    # 判断命令执行的结果
    if stderr.decode():
        conn.send(sp.stderr.read())
    # 当客户端的命令在服务器端执行时没有结果，默认返回ok
    if not stdout.decode() and not stderr.decode():
        conn.send(b'ok')
# 关闭客户端连接
conn.close()  # 四次挥手
# 关闭套接字
sk.close()


import socket, time
# 创建套接字
sk = socket.socket()
# 连接服务器端套接字
sk.connect(('', 12345))
while True:
    command = input('>>>')
    sk.send(command.encode())
    # 接收服务器端返回内容的长度
    msg_len = sk.recv(1024)
    # 告诉服务器我已经接收，解决黏包
    sk.send(b'ok')
    # 把msg_len转成字符串，并且在转成整形
    msg_len = int(msg_len.decode())
    # 根据服务器传的内容长度获取内容。
    result = sk.recv(msg_len)
    print(result.decode())
# 关闭套接字
sk.close()
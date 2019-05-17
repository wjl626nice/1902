import socket, time, struct
# 创建套接字
sk = socket.socket()
# 连接服务器端套接字
sk.connect(('', 12345))
while True:
    command = input('>>>')
    sk.send(command.encode())
    # 接收服务器端返回内容的长度
    msg_len = struct.unpack('i', sk.recv(4))[0]
    # 根据服务器传的内容长度获取内容。
    result = sk.recv(msg_len)
    print(result.decode())
# 关闭套接字
sk.close()
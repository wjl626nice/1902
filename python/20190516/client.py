import socket

sk = socket.socket()
# 对指定的ip+端口发起链接请求
sk.connect(('', 6666))
while True:
    # 接收要发送的信息，并且转换成字节
    msg = input('>>>')

    # 向服务器端套接字发送信息
    sk.send(msg.encode('utf-8'))
    # 主动退出本次聊天
    if msg == 'q':  # quit exit
        break

    # 阻塞接收服务器端套接字的消息
    server_msg = sk.recv(1024).decode('utf-8')
    print(server_msg)
    # 如果服务器端发送q字符串，那么客户端退出
    if server_msg == 'q':
        break

# 关闭客户端套接字
sk.close()

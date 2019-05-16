import socket
# 创建一个udp的套接字
udp_sk = socket.socket(type=socket.SOCK_DGRAM)

ip_port = ('', 6666)
bufsize = 1024
# 绑定端口
udp_sk.bind(ip_port)
# 所有客户端的ip和端口
clients = set()
while True:
    # 阻塞 等待接收客户端消息
    client_msg, addr = udp_sk.recvfrom(bufsize)
    # 把所有向我发送信息的ip_port记录
    clients.add(addr)
    print(clients)
    if client_msg.decode() == 'bye': continue  # 结束本次循环进入下次循环
    # print(client_msg.decode(), addr)  测试
    print('来自[%s:%d]的一个消息：\033[1;32m %s \033[0m' % (addr[0], addr[1], client_msg.decode()))
    for ar in clients:
        msg = '来自[%s:%d]的一个消息：\033[1;32m %s \033[0m' % (ar[0], ar[1], client_msg.decode())
        # 向每一个客户端发送消息
        udp_sk.sendto(msg.encode(), ar)
    # print('来自[%s:%s]的一个消息：%s' .format(addr[0], addr[1], client_msg))
    # 获取服务器端要发送的信息

    # server_msg = input('>>>').strip()  # strip 过滤字符串两端的空格
    # if server_msg == 'q': break  # 服务器端的套接字退出
    # # 向客户端发送消息
    # udp_sk.sendto(server_msg.encode(), addr)

# 关闭服务器端套接字
udp_sk.close()
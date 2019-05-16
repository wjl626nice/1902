import socket
# 创建客户端套接字
udp_sk = socket.socket(type=socket.SOCK_DGRAM)
# 要发送的ip和端口
ip_port = ('', 6666)
# 设置接收的数据大小
bufsize = 1024
while True:
    # 获取要发送的数据
    msg = input('输入要发送的消息，回车发送，输入bye退出！').strip()
    if not msg: continue  # 如果msg没有获取到内容让客户端一直输入
    # 向服务器发送信息
    udp_sk.sendto(msg.encode(), ip_port)
    if msg == 'bye': break  # 结束客户端聊天
    # 接收服务器的消息
    server_msg, addr = udp_sk.recvfrom(bufsize)
    print(server_msg.decode())
    # print(server_msg.decode(), addr)
    # print('来自[%s:%d]的一个消息：\033[1;32m%s \033[0m' % (addr[0], addr[1], server_msg.decode()))
# 关闭客户端的套接字
udp_sk.close()
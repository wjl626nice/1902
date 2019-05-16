import socket
# 创建客户端套接字
udp_sk = socket.socket(type=socket.SOCK_DGRAM)
# 要发送的ip和端口
ip_port = ('', 6666)
# 设置接收的数据大小
bufsize = 1024
msg = input('>>>').strip().encode()

print(ip_port)
# 向服务器发送信息
udp_sk.sendto(msg, ip_port)
# 接收服务器的消息
server_msg, addr = udp_sk.recvfrom(bufsize)
print(server_msg.decode(), addr)
# 关闭客户端的套接字
udp_sk.close()
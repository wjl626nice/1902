import socket
# 创建一个udp的套接字
udp_sk = socket.socket(type=socket.SOCK_DGRAM)

ip_port = ('', 6666)
bufsize = 1024
# 绑定端口
udp_sk.bind(ip_port)
# 等待接收客户端消息
client_msg, addr = udp_sk.recvfrom(bufsize)
print(client_msg.decode(), addr)
# 向客户端发送消息
udp_sk.sendto(b'aaaaa', addr)
# 关闭服务器端套接字
udp_sk.close()
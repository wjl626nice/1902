import socket
# 创建套接字
sk = socket.socket()
# 绑定端口和ip
sk.bind(('', 12345))
# 监听
sk.listen()
# 阻塞登录客户端连接
conn, addr = sk.accept()  # 三次握手

# 接收客户端信息
msg1 = conn.recv(10)
msg2 = conn.recv(1024)
print(msg1.decode())
print(msg2.decode())
# 关闭客户端连接
conn.close()  # 四次挥手
# 关闭套接字
sk.close()


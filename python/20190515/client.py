from socket import socket

# 创建socket对象
sk = socket()
# 向服务器发起链接请求，建立链接
sk.connect(('127.0.0.1', 6666))
# 获取要发送的内容,并且转换成字节
send_msg = input('请输入要发送的内容...')
print(send_msg, type(send_msg), send_msg.encode('utf-8'))
# 向服务器端发送消息
sk.send(send_msg.encode('utf-8'))
# 接收服务器的消息,并且把字节转换成字符串
s_msg = sk.recv(1024).decode('utf-8')
print(s_msg)
# 关闭socket对象
sk.close()
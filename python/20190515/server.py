# from socket import socket
import socket
# 创建socket对象
sk = socket.socket()  # 第一个参数设置套接字操作类型，第二个参数设置传输协议(SOCK_STREAM(流) TCP协议 SOCK_DGRAM UDP协议)
# 对ip绑定端口ConnectionRefusedError:
ip_port = ('127.0.0.1', 6666)
sk.bind(ip_port)
# 监听端口
sk.listen()

print('我在accept之前')
# 接收客户端连接，程序会阻塞（挂起）不会往下继续执行，直到有客户端链接时  ,connection 链接  address 地址
conn, addr = sk.accept()

print('我在accept之后')
# 接收客户端消息(message),并且把字节转换成字符串,如果客户端没发送消息就会被挂起，有消息会就会被唤醒执行。
client_msg = conn.recv(1024).decode('utf-8')
print(client_msg)
# 服务器要回复的暗号，发送的消息必须是字节
send_msg = '宝塔镇河妖'.encode('utf-8')
# 向客户端发送消息
conn.send(send_msg)
# 关闭客户端链接
conn.close()

# 关闭服务器的链接
sk.close()



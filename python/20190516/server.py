# 实现一对一聊天

import socket
from socket import SOL_SOCKET,SO_REUSEADDR  # reset  use  address
# 创建基于流的套接字
sk = socket.socket(socket.AF_INET, type=socket.SOCK_STREAM)
# 为了解决  错误：OSError: [Errno 48] Address already in use
sk.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
# 绑定ip和端口
sk.bind(('', 6666))
# 监听客户端请求
sk.listen()
# 阻塞等待客户链接
print('等待客户端链接')
conn, addr = sk.accept()  # accept会返回一个元组
print('客户端%s已链接' % (addr,))
while True:
    # conn.recv(1024) 接收的是字节，decode把字节转成成字符串
    client_msg = conn.recv(1024).decode('utf-8')  # 阻塞等待客户端发送信息
    print(client_msg)
    msg = input('>>>')

    # 'abcd'.encode('utf-8') 把'abcd'转换成字节，等同于 b'abcd'
    # conn.send(b'abcd')

    # msg.encode('utf-8') 把msg转换成字节
    conn.send(msg.encode('utf-8'))
    # 退出本次聊天
    if msg == 'q':
        break

# 关闭客户端链接
conn.close()
# 关闭服务器端的套接字
sk.close()


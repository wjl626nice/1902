#三（1）
# 一对多聊天

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
while 1:
    # 阻塞等待客户链接
    print('等待客户端链接')
    conn, addr = sk.accept()  # accept会返回一个元组
    print('客户端%s已链接' % (addr,))
    while True:
        # conn.recv(1024) 接收的是字节，decode把字节转成成字符串
        client_msg = conn.recv(1024).decode('utf-8')  # 阻塞等待客户端发送信息
        print(client_msg)
        # 判断客户端是否退出，如果退出 服务器端当前聊天也应该退出
        if client_msg == 'q':
            break
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















#三（2）
# 一对多聊天

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
while 1:
    # 阻塞等待客户链接
    print('等待客户端链接')
    conn, addr = sk.accept()  # accept会返回一个元组
    print('客户端%s已链接' % (addr,))
    while True:
        # conn.recv(1024) 接收的是字节，decode把字节转成成字符串
        client_msg = conn.recv(1024).decode('utf-8')  # 阻塞等待客户端发送信息
        print(client_msg)
        # 判断客户端是否退出，如果退出 服务器端当前聊天也应该退出
        if client_msg == 'q':
            break
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









#三（3）
# 一对多聊天

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
while 1:
    # 阻塞等待客户链接
    print('等待客户端链接')
    conn, addr = sk.accept()  # accept会返回一个元组
    print('客户端%s已链接' % (addr,))
    while True:
        # conn.recv(1024) 接收的是字节，decode把字节转成成字符串
        client_msg = conn.recv(1024).decode('utf-8')  # 阻塞等待客户端发送信息
        print(client_msg)
        # 判断客户端是否退出，如果退出 服务器端当前聊天也应该退出
        if client_msg == 'q':
            break
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




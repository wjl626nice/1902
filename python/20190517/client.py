import socket, time
# 创建套接字
sk = socket.socket()
# 连接服务器端套接字
sk.connect(('', 12345))

sk.send(b'aaaaccccccccccccccaaaaccccccccccccccaaaaccccccccccccccaaaaccccccccccccccaaaaccccccccccccccaaaaccccccccccccccaaaaccccccccccccccaaaaccccccccccccccaaaaccccccccccccccaaaaccccccccccccccaaaaccccccccccccccaaaaccccccccccccccaaaaccccccccccccccaaaaccccccccccccccaaaaccccccccccccccaaaaccccccccccccccaaaacccccccccccccc')
# time.sleep(0.000001)
sk.recv(1024)
sk.send(b'bbbb')

# 关闭套接字
sk.close()
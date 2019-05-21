import socket

# 创建一个套接字对象
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.connect(('127.0.0.1', 9999))
while True:
    msg = input('>>>').strip()
    sk.send(('邓帅说：' + msg).encode('utf-8'))
    if msg == 'q': break
    server_msg = sk.recv(1024).decode()
    print(server_msg)

sk.close()
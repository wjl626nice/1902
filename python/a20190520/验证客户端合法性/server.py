import socket
import os
import hmac
# 约定一个私钥
secret_key = b'py1902'
# 创建一个服务器端socket对象
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_port = ('', 8888)
# 绑定ip+端口
sk.bind(ip_port)
# 启动监听
sk.listen()
# 阻塞等待客户端链接
conn, addr = sk.accept()  #（客户端对象，客户端地址）

def check_conn(conn):
    # 生成一个32位的随机字节
    urandom = os.urandom(32)
    # 把随机字节发送给客户端
    conn.send(urandom)
    # 创建一个hmac对象
    hm = hmac.new(secret_key, urandom)
    # 获取摘要（hash值）
    digest = hm.digest()
    # 客户端摘要
    client_digest = conn.recv(1024)
    # compare_digest 正确是True 失败 False
    return hmac.compare_digest(digest, client_digest)
# 检测客户端
ret = check_conn(conn)
if ret:
    print('合法的')
else:
    print('不合法')

conn.close()
sk.close()


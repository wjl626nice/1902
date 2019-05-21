import socket
import hmac
# 约定一个私钥

# 网络编程时常用方法
# secret_key = b'py1902'  # 直接定义成字节
# secret_key = bytes('py1902', 'utf-8')  # bytes实例化创建一个字节
secret_key = 'py19021'.encode('utf-8')  # 把字符串转成字节

# 创建一个套接字对象
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.connect(('127.0.0.1', 8888))

# 阻塞等待接收服务器端的消息（字节）
urandom = sk.recv(1024)
hm = hmac.new(secret_key, urandom)
digest = hm.digest()  # 获取摘要(字节) 密文
sk.send(digest)
sk.close()

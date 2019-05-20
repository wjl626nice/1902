import socket
import struct
import json

# 设置数据大小
bufersize = 1024

sk = socket.socket()
sk.bind(('', 8888))
sk.listen()

# 阻塞等待客户端链接
conn, addr = sk.accept()
# 获取包头的长度
pack_head_len = conn.recv(4) # 接收固定的四个字节
# 把四个字节转成整型（包头长度）
pack_head_len = struct.unpack(b'i', pack_head_len)[0]
# 获取包头
file_head = conn.recv(pack_head_len).decode('utf-8')  # json字符串

# json.loads(file_head) 把json字符串转换成字典
file_head = json.loads(file_head)
filesize = file_head['filesize']  # filesize 将要发送过来的文件大小

with open(file_head['filename'], 'xb+') as f:
    while filesize:
        if filesize > bufersize:
            content = conn.recv(bufersize)
            f.write(content)
            filesize -= bufersize
        else:
            content = conn.recv(bufersize)
            f.write(content)
            break

conn.close()
sk.close()
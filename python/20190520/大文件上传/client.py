import socket
import os
import json
import struct

# 设置发送数据大小
bufsize = 1024

sk = socket.socket()
sk.connect(('', 8888))

# 定义包头
fileHead = {'filename':'mysql-5.7.20-macos10.12-x86_64.dmg',
 'filesize': None, 'filePath': r'/Users/qingyun/Downloads'}
# 拼接文件路径
file_path = os.path.join(fileHead['filePath'], 
    fileHead['filename'])
# 根据文件路径获取文件大小字节
filesize = os.path.getsize(file_path)
# 把文件大小放入包头中
fileHead['filesize'] = filesize
# 把字典转换成json字符串
json_head = json.dumps(fileHead)
# 把json字符串转换成字节
bytes_head = json_head.encode('utf-8')

# 计算包头字节的长度
head_len = len(bytes_head)
# 把整形转换成固定的4个字节
pack_head_len = struct.pack(b'i', head_len)

# 发送包头
sk.send(pack_head_len)
sk.send(bytes_head)

# 发送数据  r只读，b字节
with open(file_path, 'rb') as f:
    while filesize:
        # 判断文件是否将要发完
        if filesize > bufsize:
            # 读取固定的文件内容
            content = f.read(bufsize)
            # 发送文件内容
            sk.send(content)
            # 从总的文件字节大小中减去当前已经发送的内容字节数
            filesize -= bufsize  # filesize = filesize - bufsize
        else:
            # 剩余的大小内容
            content = f.read(filesize)
            sk.send(content)
            break
sk.close()
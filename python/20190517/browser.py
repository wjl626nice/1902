# 通过socket模拟浏览器请求

import socket
# 创建一个socket套接字
sk = socket.socket()
# 链接服务器
sk.connect(('www.dahepiao.com', 80))

# 按http的规定 拼接的请求行+请求头+请求主体
requestHeader = """
GET /venue/venue_23798.html HTTP/1.1
Host: www.dahepiao.com
Connection: close
User-Agent: Mozilla\/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/74.0.3729.131 Safari\/537.36\r\n
"""
# 向百度服务器发送信息
sk.send(requestHeader.encode('gbk'))

# 接收相应内容
msg = sk.recv(1024)
for aa in msg:
    msg += sk.recv(1024)

print(msg.decode('gbk'))

sk.close()

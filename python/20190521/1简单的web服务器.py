import socket
# 创建一个服务器端socket（套接字）
sk = socket.socket()
# 绑定ip_port
sk.bind(('', 8080))
# 监听
sk.listen()

while True:
    # 阻塞等待客户端链接
    conn, addr = sk.accept()  # accept 结果（'客户端对象', 客户端地址）
    # 接收客户端的http请求结构,网络传输的数据都是字节
    client_request = conn.recv(1024).decode('utf-8')
    # 对请求结构体进行拆分，转换成列表
    request_datas = client_request.split('\r\n')
    # 获取请求行
    request_line = request_datas[0]
    # 对请求行进行拆分  strip：去除字符串两端的空格，split:默认根据空格拆分字符串
    request_line_block = request_line.strip().split()
    print(request_line_block)
    # 获取资源（uri）
    uri = request_line_block[1]
    print(request_line_block, request_line_block[1])
    # 向客户端发送响应结构体（响应行和响应头）
    conn.send(b'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n')
    # 向客户端发送响应正文（响应主体）
    conn.send('人生苦短，快用python!'.encode('utf-8'))
    conn.close()

sk.close()
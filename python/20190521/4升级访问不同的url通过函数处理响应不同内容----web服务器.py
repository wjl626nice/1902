import socketserver


def zongyuan():
    return '<h1 style="color:#000">宗元</h1>'


def yu():
    return '瑜说我想静静！（既生瑜何生亮！）'


def r404():
    return '页面跑丢了！'


def niuchao():
    return '又睡了！'

# uri 和函数的对应
uri_func = [
    ('/zongyun', zongyuan),
    ('/yu', yu),
    ('/niuchao', niuchao),
]

class MyServer(socketserver.BaseRequestHandler):

    def handle(self):
        # 当有客户端链接时被调用，方法内部实现客户端消息的接收和发送

        # self.request 跟 conn一样
        # 接收客户端发送的http请求结构
        client_request = self.request.recv(1024).decode('utf-8')
        # 对请求结构体进行拆分，转换成列表
        request_datas = client_request.split('\r\n')
        # 获取请求行
        request_line = request_datas[0]
        # 对请求行进行拆分  strip：去除字符串两端的空格，split:默认根据空格拆分字符串
        if not request_line: return
        request_line_block = request_line.strip().split()
        # 获取资源（uri）
        uri = request_line_block[1]
        # 向客户端发送响应结构体（响应行和响应头）
        self.request.send(b'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n')
        print(uri)
        # 根据不同的uri 响应不同内容
        for u in uri_func:
            if u[0] == uri:
                func = u[1]  # u[1] 函数体
                break
        else:
            func = r404  # r404代表函数体

        # func 代表uri对应的函数体，func() 函数调用
        response_content = func()
        # 向客户端发送响应正文（响应主体）
        self.request.send(response_content.encode('utf-8'))


if __name__ == '__main__':
    # 设置ip+port重用
    socketserver.ThreadingTCPServer.allow_reuse_address = True
    # 实例化线程类创建一个对象
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 8080), MyServer)
    # 永远执行下去
    server.serve_forever()
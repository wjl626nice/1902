# 通过socketserver模块封装的类实现并发处理，1对多的通信
import socketserver

# 自定义类，对客户端数据的接收和发送
class my_socket_server(socketserver.BaseRequestHandler):

    def handle(self):
        # 此方法名必须是handle 不能更改
        # self.request 相当于 conn（客户端对象）
        while True:
            # 接收客户端消息
            client_msg = self.request.recv(1024).decode('utf-8')
            if client_msg == 'q': break
            print(client_msg)
            msg = input('>>>').strip().encode('utf-8')
            # 向客户端发送消息
            self.request.send(msg)

if __name__ == '__main__':
    ip_port = ('', 9999)
    socketserver.ThreadingTCPServer.allow_reuse_address = True
    # 一般一个正在运行的程序就是一个进程，但是真正处理代码的是线程（线程是被进程创建）
    server = socketserver.ThreadingTCPServer(ip_port, my_socket_server)  #实现了线程并发问题

    server.serve_forever() # 永远执行下去
from wsgiref.simple_server import make_server
import time
from jinja2 import Template
import pymysql

def zongyuan():
    # 读取静态页面返回
    with open('./template/zongyuan.html', 'rb') as f:
        ret = f.read()
    return ret


def yu():
    # 动态网页
    with open('./template/yu.html', 'rb') as f:
        ret = f.read()
    # 获取指定格式的时间
    datetime = time.strftime('%Y-%m-%d %X')
    # 对ret中的内容进行替换
    ret = ret.replace('{time}'.encode(), datetime.encode())

    name = '宋瑜'
    # 对ret中的内容进行替换
    ret = ret.replace('{name}'.encode(), name.encode())

    return ret


def studentList():
    with open('./template/students.html', 'r') as f:
        ret = f.read()
    template = Template(ret)

    conn = pymysql.connect(host="127.0.0.1", user="root", password="123456", database="python1902", charset='utf8')
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    sql = 'select * from students'
    cursor.execute(sql)
    datas = cursor.fetchall()
    # print(datas)
    # render渲染  返回字符串
    return template.render({"name":'aaaa', 'datas':datas}).encode()


def r404():
    return '页面跑丢了！'.encode('utf-8')


def niuchao():
    return '又睡了！'.encode('utf-8')

# uri 和函数的对应
uri_func = [
    ('/zongyuan', zongyuan),  # zongyuan代表上边的函数体
    ('/yu', yu),
    ('/niuchao', niuchao),
    ('/studentList', studentList)
]

# run_server 在客户端发起请求时自动被调用
def run_server(environ, start_response):
    # environ 包含客户端请求结构体
    #start_response 设置响应行和响应头


    # 响应行
    request_line = '200 OK'  # HTTP Status
    # 响应头
    request_headers = [('Content-type', 'text/html')]  # HTTP Headers
    # 设置响应行和响应头
    start_response(request_line, request_headers)

    # 获取客户端访问的uri
    uri = environ['PATH_INFO']
    for u in uri_func:
        # 判断当前请求的uri 和已经设置好的uri是否匹配
        if u[0] == uri:
            func = u[1]
            break
    else:
        func = r404

    # 执行当前请求 uri对应的函数
    response_content = func() if isinstance(func(), bytes) else func().encode()
    # 设置响应正文
    return [response_content]


if __name__ == '__main__':
    # 服务器对象
    httpd = make_server('', 8080, run_server)
    # 永远执行下去
    httpd.serve_forever()


from django.shortcuts import render, HttpResponse
from django.views import View
from django.http import HttpResponse as Response
import json

# Create your views here.
# request请求对象
def abc(request):
    print(type(request))
    return HttpResponse('测试')

# 函数式写法
def add_book(request):
    if request.method == 'POST':
        return HttpResponse('是post请求！')
    return render(request, 'add_book.html')

# 类的写法
# 类的写法需要继承 View基类
class add_books(View):
    def get(self, request):
        return  render(request, 'add_book.html')
    def post(self, request):
        return HttpResponse('类的post请求！')

def get_attr_by_request(request):
    # 协议
    scheme = request.scheme
    # 本次请求的方法
    method = request.method
    # 获取get参数
    get = request.GET
    # 获取post参数
    post = request.POST
    # 请求资源路径 uri
    path = request.path
    path_info = request.path_info
    # 获取的原始数据(字节) 只有post提交时才有
    body = request.body
    body = body.decode()
    # 获取客户端和服务器端的信息
    meta = request.META
    full_path = request.get_full_path()
    """
        HTTP_REFERER # 来源页
        HTTP_USER_AGENT # 可以判断用户访问用的设备
        REMOTE_ADDR # ip地址，可以获取用户所在的城市
    """
    print(meta, type(meta))
    # dir查看对象的所有属性和方法
    print(dir(request))
    dicts = {
        'scheme': scheme,
        'method': method,
        'get': get,
        'post': post,
        'path': path,
        'path_info': path_info,
        'body': body,
        'full_path': full_path,
        # 'meta': meta
    }
    # json.dumps(dicts) 把字典转换成 json字符串
    return HttpResponse(json.dumps(dicts))

def upload_file(request):
    if request.method == 'POST':
        print(request.FILES)
        # 获取上传的文件信息
        print(dir(request.FILES))
        # 获取文件对象
        print(request.FILES['upload'], type(request.FILES['upload']))
        # 获取上传文件的名字
        print(request.FILES['upload'].name)
        # 获取上传文件的大小
        print(request.FILES['upload'].size)
        # 获取文件类型
        print(request.FILES['upload'].content_type)

        filename = request.FILES['upload'].name
        # 自己写一些逻辑，比如 只允许上传图类

        with open(filename, 'ab') as f:
            for chunk in request.FILES['upload'].chunks(): # chunks 每循环一次从内存中区一小块
                # 把从内存中读取的块保存到文件中。
                f.write(chunk)

    return render(request, 'upload_file.html')

def request_method(request):
    # 获取主机名
    get_host = request.get_host()
    # 获取带参数的uri
    get_full_path = request.get_full_path()
    # 获取完整url
    build_absolute_uri = request.build_absolute_uri()
    # 判断是否是https请求
    is_secure = request.is_secure()
    # 判断是否是ajax请求
    is_ajax = request.is_ajax()
    dicts = {
        'get_host': get_host,
        'get_full_path': get_full_path,
        'build_absolute_uri': build_absolute_uri,
        'is_secure': is_secure,
        'is_ajax': is_ajax,
    }
    # json.dumps(dicts) 把字典转换成 json字符串
    return HttpResponse(json.dumps(dicts))

def get_response(request):
    # 第一种创建response对象
    # response = Response('我就是想测试响应！')
    # response = Response('<xml><name>sdfsd</name></xml>', content_type='text/xml')

    # 第二种创建response对象
    # 创建一个响应对象
    response = Response()
    # response.write('<p>aaaaaaaaaa</p>')
    # response.write('<p>bbbbbbbbbb</p>')
    # response.write('<p>cccccccccc</p>')

    # 测试图片展示
    # # 设置响应类型
    # response['content-type'] = 'image/png'
    # # 设置响应的状态码
    # response.status_code = 404
    # with open('111.png', 'rb') as f:
    #     # 读取文件内容
    #     fileInfo = f.read()
    # # 设置响应正文
    # response.content = fileInfo

    my_data = ''
    # 测试表格
    # 可以加一些业务逻辑 比如 判断会员是否已经购买当前资源，或会员是否登录

    with open('1902.xlsx', 'rb') as f:
        # 读取文件内容
        my_data = f.read()
    response = Response(my_data, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="foo.xls"'


    return response
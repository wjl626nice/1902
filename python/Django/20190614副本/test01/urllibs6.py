from urllib import request
# 构建请求头
from urllib.request import Request
from urllib.parse import urlencode
# 配置代理ip
from urllib.request import ProxyHandler, build_opener
import random
# 配置代理ip
proxy_header = ProxyHandler({'http':"123.120.197.187:8060"})
opener = build_opener(proxy_header)
# 像浏览器一样对网址发起请求，响应返回给了 result
result = opener.open('http://127.0.0.1:8000/add_books')
try:
    print(result.getheaders())
    # 获取响应主体
    response = result.read().decode('GBK')
    print(response)
except Exception as e:
    print(e.args)

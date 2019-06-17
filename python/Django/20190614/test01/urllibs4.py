from urllib import request
import random


# 像浏览器一样对网址发起请求，响应返回给了 result
result = request.urlopen('http://www.dahepiao.com/')

# 获取响应主体
response = result.read().decode('GBK')
print(response)
print(response.getheaders())
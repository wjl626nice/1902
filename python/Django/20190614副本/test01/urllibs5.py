from urllib import request
# 构建请求头
from urllib.request import Request
from urllib.parse import urlencode
import random

url = 'http://www.dahepiao.com/'
header = {
    'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
}
data = {'username': 'adfsa'}
data = bytes(urlencode(data),'utf-8')
# 构建请求结构体
# 对请求头的添加方法有两种
# seq = Request(url=url, data=data, headers=header, method='GET')
seq = Request(url=url, data=data, method='GET')
seq.add_header('User-Agent',"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1")
# 像浏览器一样对网址发起请求，响应返回给了 result
result = request.urlopen(seq)

print(result.getheaders())
# 获取响应主体
response = result.read().decode('GBK')
print(response)

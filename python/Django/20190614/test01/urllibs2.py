from urllib import request
from urllib.parse import urlencode


kw = input('关键词>>>')

data = {'q': kw}
data = urlencode(data)

# 像浏览器一样对网址发起请求，响应返回给了 result, 如果第二个参数存在则是post请求
result = request.urlopen('https://huaban.com/search/?'+data, timeout=1)
# result = request.urlopen('https://huaban.com/search/?q=卡哇伊')
print(result.getcode())
print(result.read().decode('utf-8'))





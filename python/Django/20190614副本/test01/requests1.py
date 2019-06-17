import requests
# https://2.python-requests.org//zh_CN/latest/user/quickstart.html
# 模拟浏览器发起get请求
req = requests.request('GET', 'http://www.weather.com.cn/data/sk/101010100.html')
# 获取对象类型
print(type(req))
# 获取响应头
print(req.headers)
# 获取状态码
print(req.status_code)
# 获取响应内容的编码
print(req.encoding)
# 可以设置响应的编码类型
req.encoding = 'utf-8'
# 获取响应内容的二进制形式(字节)
print(req.content)
# 获取响应内容的字符串形式
print(req.text)
print(req.json())
from urllib import request
import random

citylist = {'101180303':'原阳', '101181801':'济源', '101180401':'安阳'}
cityids = ['101180303', '101180303', '101180401']
# 从列表中随机取一条数据
cityid = random.choice(cityids)

# 像浏览器一样对网址发起请求，响应返回给了 result
result = request.urlopen('http://www.weather.com.cn/data/sk/'+ cityid +'.html')
# 响应状态码
print(result.getcode())
# 查询响应对象 类型
print(type(result))
# 获取所有响应头
print(result.getheaders())
# 获取响应主体
response = result.read().decode('utf-8')
print(response)
from urllib import request
from urllib.parse import urlencode

# python 模拟 post 需要传字节
txtUserName = input('姓名>>>')
txtUserTel = input('电话>>>')
txtUserQQ = input('qq>>>')
txtTitle = input('标题>>>')
txtContent = input('内容>>>')
txtCode = input('验证码>>>')

data = {'txtUserName': txtUserName,
        'txtUserTel':txtUserTel,
        'txtUserQQ':txtUserQQ,
        'txtTitle':txtTitle,
        'txtContent':txtContent
        }
data = urlencode(data).encode('utf-8')

# 像浏览器一样对网址发起请求，响应返回给了 result, 如果第二个参数存在则是post请求
result = request.urlopen('http://127.0.0.1:8000/add_book', data=data)

print(result.getcode())
print(result.read().decode('utf-8'))





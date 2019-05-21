import hmac, sys  # 和hashlib一样
# 可以设置指定的模块目录
# sys.path.insert(0, '/etx/asdfasdf/asdfasfa')
# print(sys.path)
secret_key = '天王盖地虎'
# 根据秘钥 对内容进行hash(md5)生成hash值。a就是模块hmac内的HMAC类实例化的对象
a = hmac.new(secret_key.encode(), '我是你大哥！'.encode())
b = a.digest()
print(b)


c = hmac.new(secret_key.encode(), '我是你大哥！'.encode())
# 获取摘要（hash值）
d = c.digest()
print(d)
if b == d:
    print('正确')
else:
    print('错误')

print(hmac.compare_digest(b, d))









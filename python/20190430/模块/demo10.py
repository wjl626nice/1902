from b.randomcc import checkCode

print(checkCode())

# 验证码不区分大小写的时候，在服务器端，需要把获取到的数据，统一转成大写/小写
str1 = "FH8g"
print(str1.lower())

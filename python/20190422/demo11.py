# 字典 由键值对形成的数据，没有顺序，取值的时候要使用键，键不能重复,并且不可以更改,键是字符串的时候，要使用 引号
dict = {
    "name": "张三",
    "age": 18,
    "sex": "boy"
}
print(dict)
print(dict["age"])
# 输出所有的键
print(dict.keys())
# 输出所有的值
print(dict.values())

# 新增键值对
dict["money"]= 1000000000
print(dict)
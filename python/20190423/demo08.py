# 字典
'''

字典是另一种可变容器模型
可存储任意类型对象
每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中
无顺序
注意：键要使用 引号 包裹起来
'''

dict1 = {'Alice': '2341', 'Beth': '9102', 'Cecil': 3258}

# 访问字典里的值
print(dict1["Alice"])
key = "Beth"
print(dict1[key])
# 访问不存在的键的时候，会抛出异常
# print(dict["Tom"])

# 修改字典
print(dict1)
dict1["Beth"] = 9527
print(dict1)

# 添加新的键值对
dict1["Tom"] = 89757
print(dict1)

# 删除
# 删除键值对
del dict1["Tom"]
print(dict1)

# 清空字典
# dict1.clear()
# print(dict1)

# 删除字典
# del dict1
# print(dict1)

# 不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
# 键必须不可变   字符串

'''
字典内置函数

len(dict)
计算字典元素个数，即键的总数。

str(dict)
输出字典，以可打印的字符串表示。

type(variable)
返回输入的变量类型，如果变量是字典就返回字典类型。
'''

print(len(dict1))
print(str(dict1))
print(type(dict1))
print(type(str(dict1)))


'''
内置方法：
    
radiansdict.clear()
删除字典内所有元素

radiansdict.copy()
返回一个字典的浅复制
'''

dict1 = {'user': 'runoob', 'num': [1, 2, 3]}

# dict2 = dict1  # 浅拷贝: 引用对象
# dict3 = dict1.copy()  # 浅拷贝：深拷贝父对象（一级目录），子对象（二级目录）不拷贝，还是引用
#
# # 修改 data 数据
# dict1['user'] = 'root'
# dict1['num'].remove(1)
#
# # 输出结果
# print(dict1)
# print(dict2)
# print(dict3)


import copy

# 跟 dict1.copy(）相同
# dict4 = copy.copy(dict1)
#
# dict1['user'] = 'root'
# dict1['num'].remove(1)
#
# print(dict1)
# print(dict4)


# deepcopy 不仅仅拷贝第一层，之后每一层页拷贝
dict5 = copy.deepcopy(dict1)

dict1['user'] = 'root'
dict1['num'].remove(1)

print(dict1)
print(dict5)

'''
radiansdict.fromkeys()
创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
'''
keys1 = ("name", "age", "sex")
dict6 = dict.fromkeys(keys1, "9527")
print(dict6)

'''
key in dict
如果键在字典dict里返回true，否则返回false
'''
print("age" in dict6)


'''
radiansdict.items()
以列表返回可遍历的(键, 值) 元组数组
'''
print(dict6.items())


'''
radiansdict.keys()
返回一个迭代器，可以使用 list() 来转换为列表
'''

print(dict6.keys())

'''
radiansdict.values()
返回一个迭代器，可以使用 list() 来转换为列表
'''
print(dict6.values())


'''
radiansdict.get(key, default=None)
返回指定键的值，如果值不在字典中返回default值,不会抛出异常
'''

print(dict6.get("age"))
print(dict6.get("abc"))

'''
radiansdict.setdefault(key, default=None)
和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
'''
dict6.setdefault("abc", '1234567890')
print(dict6)


'''
radiansdict.update(dict2)
把字典dict2的键/值对更新到dict里
'''
dict7 = {'Name': 'Runoob', 'Age': 7}
dict8 = {'Sex': 'female'}

dict7.update(dict8)
print("更新字典 dict7 : ", dict7)

dict9 = {"Age": 18}
dict7.update(dict9)
print("更新字典 dict7 : ", dict7)

'''
pop(key[,default])
删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
'''
dict7.pop("Age")
print(dict7)
# 假如键书写错误，会抛出异常
dict7.pop("sex")
print(dict7)




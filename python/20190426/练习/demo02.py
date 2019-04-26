# 查找数据中元素，移除每个元素的空格，并查找以 a 或 A 开头 并且以 c 结尾的所有元素。
'''
    li = ["alec", " aric", "Alex", "Tony ", "rain"]
    tu = ("alec", " aric", "Alex", "Tony ", "rain")
    dic = {'k1': "alex", 'k2': ' aric',  "k3": "Alex", "k4": "Tony"}
'''

li = ["alec", " aric", "Alex", "Tony ", "rain"]

newLi = []

for x in li:
    newX = x.strip()
    if (newX[0] == "a" or newX[0] == "A") and newX[-1] == "c":
        newLi.append(newX)

print(newLi)

# def fn(ele):
#     return ele.strip()
#
#
# map1 = map(fn, li)
# print(map1)
#
# print(list(map1))


tu = ("alec", " aric", "Alex", "Tony ", "rain")
newLi2 = []
for y in tu:
    newY = y.strip()
    if (newY[0] == "a" or newY[0] == "A") and newY[-1] == "c":
        newLi2.append(newY)

tu2 = tuple(newLi2)
print(tu2)

dic = {'k1': "alex", 'k2': ' aric', "k3": "Alexc", "k4": "Tony"}

newDic = {}
for k, v in dic.items():
    newV = v.strip()
    if (newV[0] == "a" or newV[0] == "A") and newV[-1] == "c":
        newDic[k] = newV

print(newDic)


def fn2(arg):
    if type(arg) == dict:
        newDic = {}
        for k, v in arg.items():
            newV = v.strip()
            if (newV[0] == "a" or newV[0] == "A") and newV[-1] == "c":
                newDic[k] = newV

        return newDic
    else:
        newLi2 = []
        for y in arg:
            newY = y.strip()
            if (newY[0] == "a" or newY[0] == "A") and newY[-1] == "c":
                newLi2.append(newY)

        if type(arg) == list:
            return newLi2
        else:
            return tuple(newLi2)


print("-------------------------")
dic2 = {'k1': "alex", 'k2': ' aric', "k3": "Alexc", "k4": "Tony"}
print(fn2(dic2))

tu2 = ("alec", " aric", "Alex", "Tony ", "rain")
print(fn2(tu2))

li2 = ["alec", " aric", "Alex", "Tony ", "rain"]
print(fn2(li2))
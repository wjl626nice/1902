# 检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
def fn1(ele):
    if len(ele) > 2:
        return ele[0:2]


print(fn1([1, 2, 4, 5]))


# 检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
def fn2(ele):
    newDict = {}
    for k, v in ele.items():
        if len(v) > 2:
            newDict[k] = v[0:2]

    return newDict


print(fn2({"name": "zhangsan", "age": "18", "sex": "女"}))


# 检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
def fn3(arg):
    newList = []

    for x in range(0, len(arg)):
        if x % 2 != 0:
            newList.append(arg[x])

    return newList


print(fn3([1, 2, 3, 4, 5, 6, 7, 78, 9, 10, "bacd"]))


strs = 'aaa'
# print(strs + 12)
print(strs * 3)
print('bbb' + '12')

def get(aa, bb, cc, ab=44, ac=45, *args, **kwargs):
    print(aa, bb, cc, ab, ac)
    print(args)
    print(kwargs)


# get(1, *[2, 3, 4, 5, 6, 7, 8, 9], aaa=11, bbb=222, ccc=333)
# lists = [2, 3, 5]
# dicts = {'dd': 55, 'ee': 66}
# print(get(2, 3, 4, 5, 6, aa=22, bb=33, cc=44, **dicts))

# abc = {'bbb': 4, 'cc': 3, 'aa': 22}
# print(get(*lists))  # * 会把list拆分给函数中对应的形参
# print(get(**abc))  # * 会把list拆分给函数中对应的形参
# print(get(lists[0], lists[1], lists[2]))


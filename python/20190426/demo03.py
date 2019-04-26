# 迭代


# 判断一个数据是否可迭代
from collections import Iterable

# isinstance(a, b)      a 是否是 b 类型的（可以寻找 b 祖先类）
# print(isinstance('123', Iterable))
# print(isinstance(123, Iterable))
# print(isinstance(['1', '2', '3'], Iterable))

# 后面的多个列表数量要一样
for x, y, z in [('大哥', '二哥', '三哥'), ('大姐', '二姐', '三姐'), {'如花', '小花', '大花'}]:
    print(x)
    print(y)
    print(z)
    print("--------------")
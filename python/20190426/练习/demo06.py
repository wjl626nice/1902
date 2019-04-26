# 计算传入字符串中【数字】、【字母】、【空格] 以及 【其他】的个数
def fn1(s):
    szlen = 0
    zmlen = 0
    kglen = 0
    qtlen = 0
    for x in s:
        if x.isdigit():
            szlen += 1
        elif x.isalpha():
            zmlen += 1
        elif x == " ":
            kglen += 1
        else:
            qtlen += 1

    return szlen, zmlen, kglen, qtlen


print(fn1("123456789fghjkljxcvbjcvhbjk    jlmmKLNj&&%$%gujjlk"))


# 判断用户传入的对象（字符串、列表、元组）长度是否大于5。
def fn2(ele):
    # 三目运算      类似于 js 中     ? :
    return True if len(ele) > 5 else False


print(fn2("1234567"))
print(fn2(["1", "2", "3", "4", "4", "1"]))


# 检查用户传入的对象（字符串、列表、元组）的每一个元素是否含有空内容
def fn3(ele):
    if len(ele) == 0:
        return True

    for x in ele:
        if len(x) == 0:
            return True

    return False


print(fn3(""))
print(fn3(("2345", "12")))
print(fn3(["2345", "12", " "]))

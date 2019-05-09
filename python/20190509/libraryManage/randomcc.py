import random


# 随机字母:
def rndChar():
    list1 = list(range(48, 58)) + list(range(65, 91)) + list(range(97, 123))
    return chr(random.choice(list1))


def checkCode():
    # 输出文字:
    cc = ""
    for t in range(4):
        tempcc = rndChar()
        cc += tempcc
    return cc

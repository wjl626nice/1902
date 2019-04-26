# .抓花生游戏
'''
现在有一堆花生，你 和 npc 轮流地从堆上抓取1-5个花生，谁抓到最后一个，谁就输了！

要求：先输入总花生个数，之后，你 和 npc 依次输入各自抓取的花生个数
'''

import random

total = int(input("游戏开始，请输入总的花生个数:"))

maxNum = 5

while True:
    # 游戏玩家
    numOfP = int(input("请输入你要抓取的花生个数:"))
    if numOfP <= 0 or numOfP > maxNum:
        continue

    total -= numOfP

    # 玩家输
    if total == 0:
        print("game over,你输了")
        break

    print("当前花生总数为：%d" % total)

    # npc玩家

    # if total < 5:
    #     maxNum = total
    # # numOfNpc = random.choice(list[range(1, maxNum + 1)])
    # numOfNpc = random.randrange(1, maxNum + 1)

    if total < 5 and total > 1:
        numOfNpc = total - 1
    elif total == 1:
        numOfNpc = 1
    else:
        numOfNpc = random.randrange(1, 5 + 1)

    print("npc抓取了 % d 个花生" % numOfNpc)

    total -= numOfNpc
    print("当前花生总数为：%d" % total)

    if total < 5:
        maxNum = total

    if total == 0:
        print("你赢了")
        break

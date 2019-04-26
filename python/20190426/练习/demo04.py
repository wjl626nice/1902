# .根据月判断，当前日属于哪两个星座，再根据日 判断具体的星座
'''
要求：用户输入月和日，输出所属星座

     能够循环使用
'''

# month = input("请输入月份:")
# day = input("请输入日:")

# if month == "1":
#     if int(day) in range(1,20):
#         print("摩羯")
#     elif int(day) in range(20,32):
#         print("水瓶座")


list1 = list(range(321, 332)) + list(range(401, 420))
list2 = list(range(420, 431)) + list(range(501, 521))
list3 = list(range(521, 532)) + list(range(601, 622))
list4 = list(range(622, 631)) + list(range(701, 723))
list5 = list(range(723, 732)) + list(range(801, 823))
list6 = list(range(823, 832)) + list(range(901, 923))
list7 = list(range(923, 931)) + list(range(1001, 1024))
list8 = list(range(1024, 1032)) + list(range(1101, 1123))
list9 = list(range(1123, 1131)) + list(range(1201, 1222))
list10 = list(range(1222, 1232)) + list(range(101, 120))
list11 = list(range(120, 132)) + list(range(201, 219))
list12 = list(range(219, 230)) + list(range(301, 321))

dict1 = (
    {"k1": list1, "k2": "白羊座"},
    {"k1": list2, "k2": "金牛座"},
    {"k1": list3, "k2": "双子座"},
    {"k1": list4, "k2": "巨蟹座"},
    {"k1": list5, "k2": "狮子座"},
    {"k1": list6, "k2": "处女座"},
    {"k1": list7, "k2": "天秤座"},
    {"k1": list8, "k2": "天蝎座"},
    {"k1": list9, "k2": "射手座"},
    {"k1": list10, "k2": "摩羯座"},
    {"k1": list11, "k2": "水瓶座"},
    {"k1": list12, "k2": "双鱼座"}
)

month = input("请输入月份:")
day = input("请输入日:")
keyword = month + day.rjust(2, "0")
for d in dict1:
    if int(keyword) in d["k1"]:
        print(d["k2"])

# 用户交互，显示省市县三级联动的选择，数据格式如下，具体数据自己组织
'''
要求：输入省，显示省所有的市，然后输入市，显示所有县(区)

      能够循环使用
'''

dict1 = {'河北': {"石家庄": ["鹿泉", "藁城", "元氏"], "邯郸": ["永年", "涉县", "磁县"]},
         '河南': {'郑州': ['金水区', '二七区', '管城区'], '南阳': ['卧龙区', '高新区', '唐河县']},
         '山西省': {'市区': ['市一区', '市二区', '市三区'], '县区': ['县一区', '县二区', '县三区']}}

while True:
    proKeys = dict1.keys()
    print(proKeys)
    pro = input("请输入省份名称:")
    if pro in proKeys:
        dict2 = dict1[pro]
        cityKeys = dict2.keys()
        print(cityKeys)

        city = input("请输入城市名称:")
        if city in cityKeys:
            list1 = dict2[city]
            print(list1)
        else:
            print("你输入的城市有误")
    else:
        print("你输入的省份有误")

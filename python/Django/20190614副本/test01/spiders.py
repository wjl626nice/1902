import requests
import re
import json

def get_xh_lists(page=0):
    """
    获取指定页的校花数据（名称，链接）
    :param page:
    :return:
    """
    req = requests.request('GET', 'http://www.xiaohuar.com/list-1-'+str(page)+'.html')
    req.encoding = 'gbk'
    html = req.text
    # 校花的名字 链接地址
    data = re.findall('<div class="img">.*?"(.*?)".*?"price">(.*?)</span>', html,
                              re.DOTALL)  # re.DOTALL  点可以代表所有字符
    # print(data, len(data))
    return data


# 第一次采集页面时需要用
req = requests.request('GET', 'http://www.xiaohuar.com/list-1-0.html')
req.encoding = 'gbk'
html = req.text

# 获取校花列表的总页数
page_num = re.findall('<a href=".*?-(\d+).html">尾页</a>',html)[0]
page = 0
xh_url_lists = []

# 循环采集校花数据
while(True):
    # 判断是否超过了要采集的最大页
    if int(page_num) < page:
        break
    xh_url_lists.append(get_xh_lists(page))
    page += 1

with open('xh_url_lists.txt', 'a+') as f:
    # 向文件内保存校花信息列表
    json.dump(xh_url_lists, f)

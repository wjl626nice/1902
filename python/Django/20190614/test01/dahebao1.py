import requests
import re
import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', password="123456",
                 database='abc', charset='utf8')
# 创建游标
cursor = conn.cursor()



def get_list_urls(page_num=1):
    """
    获取每页的标题和url
    :param page_num:
    :return:
    """
    url = 'http://www16.zzu.edu.cn/msgs/vmsgisapi.dll/vmsglist?mtype=x&lan=202&tts=&tops=&pn='+str(page_num)
    result = requests.request('GET', url)
    result.encoding = 'utf-8'
    # 采集每一页的新闻标题和链接
    res = re.findall('<a href="(.*?)" target="_blank">.*?<span class="zzj_f6_c">.*?</span></a>', result.text)
    # print(res,len(res))
    # 让列表的元素位置翻转
    res.reverse()
    return res

def get_article(url):
    """
    根据指定文章地址获取文章信息
    :param url:
    :return:
    """
    result = requests.request('GET', url)
    result.encoding = 'utf-8'
    title = re.findall('<div class="zzj_3">(.*?)</div>', result.text)
    datas = re.findall('<span class="zzj_f2">(.*?)</span>', result.text)
    content = re.findall('<div class="zzj_5">(.*?)</div>', result.text, re.DOTALL)
    # print(title)
    # print(datas)
    # print(content)
    return [title[0], datas[0], datas[1], datas[2], datas[3].strip(), content[0]]

# 首次采集分页总数
url = 'http://www16.zzu.edu.cn/msgs/vmsgisapi.dll/vmsglist?mtype=x&lan=202&tts=&tops=&pn=1'
result = requests.request('GET', url)
result.encoding = 'utf-8'

# print(re.findall('分(\d+)页', result.text))
# 获取总页数
page_num = int(re.findall('分(\d+)页', result.text)[0])

# print(get_list_urls(201))
i = 1  # 正在采集的数据
errorList = [] # 错误列表
while(True):
    if page_num<=0:
        break
    print('\033[1;31;40m正在采集第%d页\r\n' % (page_num,))
    print('*' * 50)
    # 每一页的新闻链接
    urls = get_list_urls(page_num)
    print(urls)
    for url in urls:
        cursor.execute('select id from abc_article where url="'+url+'"')
        # 判断数据库中是否已经存当前要采集的数据
        if(cursor.rowcount): continue
        try:
            # 可能采集时内部正则匹配出错。
            article = get_article(url)
        except Exception:
            errorList.append(url)
            print('\033[7;31m正在采集第{}条新闻：{}失败！\033[1;31;40m'.format(i, url))
            continue
        try:
            article.append(url)
            cursor.execute('insert into abc_article values(null,%s,%s,%s,%s,%s,%s,%s)', article)
            conn.commit()
            print('\033[7;31m正在采集第{}条新闻：{}成功！\033[1;31;40m'.format(i, url))
        except Exception as e:
            print(url)
            print(e.args)
            conn.rollback()
            print('\033[7;31m正在采集第{}条新闻：{}失败！\033[1;31;40m'.format(i, url))
        # 每采集一条新闻 i加一，用来判断采集数是否跟要采集的数量一致。
        i += 1

    print('*' * 50)
    print('\033[0m')
    # 每采集一页 总页数减一
    page_num -= 1


cursor.close()
conn.close()

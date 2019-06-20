from django.shortcuts import render, HttpResponse
import time
import datetime
from manager.models import *

class animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say(self):
        return '会叫！'

    def __str__(self):
        return '<animal 名字：{}>'.format(self.name)

# Create your views here.
def test(request):
    abc = 111
    name = '牛超'
    name_english = 'tom niu'
    age = 23
    name_list = ['亚坤', '哼哼', '洋洋', '沉沉']

    # [('name','萝卜'),('color',[]),('size', 'bigbig')]
    dicts = {'name': '萝卜', 'color': ['green', 'red', 'white'], 'size': 'bigbig'}

    xiaohei = animal('小黑狗', 3)
    xiaonai = animal('小奶狗', 1)
    xiaohuang = animal('小黄狗', 4)

    # 获取时间戳
    timestamps = time.time()
    dt = datetime.datetime.now()
    # print(dt, time.localtime())
    #
    dtt = datetime.datetime.fromtimestamp(timestamps)

    strs = '王长鹏今天<strong style="color:red">请假</strong>了'
    alertstr = '<script>while(1){alert("哈哈哈，重启吧！")}</script>'
    describles = '如果字符串长于指定的字符数，则截断该字符串。截断的字符串将以可翻译的省略号字符（“...”）结尾。'
    words = """
        You can use any number of values in a cycle tag, separated by spaces. Values enclosed in single quotes (') or double quotes (") are treated as string literals, while values without quotes are treated as template variables.
    """
    zhwords = '你真 衰 ！'

    # datetime.datetime.
    starttime = '2019-06-01 15:02'
    # 把字符串时间转成计算机能识别的 datetime时间
    starttime = datetime.datetime.strptime(starttime, '%Y-%m-%d %H:%M')

    endtime = '2019-06-11 18:02'
    endtime = datetime.datetime.strptime(endtime, '%Y-%m-%d %H:%M')
    zhangpengxiang = '张鹏祥'

    names = {'name': "书园", 'get': 'aaa', 'abc': len}

    return render(request, 'test.html', {
        'a': abc,
        "name": name,
        'name_english': name_english,
        'age': age,
        'name_list': name_list,
        'dicts': dicts,
        'xiaonai': xiaonai,
        'dogs': [xiaohei, xiaonai, xiaohuang],
        'body': '<div>是的<h1 style="color:red">发送</h1>到发送到</div>',
        'filesize': 234234523,
        'dt': dt,
        'dtt': dtt,
        'strs': strs,
        'alertstr': alertstr,
        'describles': describles,
        'words': words,
        'zhwords': zhwords,
        'starttime': starttime,
        'endtime': endtime,
        'zhangpengxiang': zhangpengxiang,
        'names': names
    })

def test1(request):
    author = Author.objects.get(id=3)
    print(author)
    print(author.name)
    print(author.bookss.all())
    return HttpResponse('测试！')
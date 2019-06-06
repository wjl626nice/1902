from django.shortcuts import render


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
    })
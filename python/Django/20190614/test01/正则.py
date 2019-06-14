import re

# re属于模块   re.compile(正则) 生成一个正则对象。
# 不管re模块还是正则对象，都具有 match search 方法，但是他们不一样。

"""
 match 默认从字符串的开头查找，也可以指定位置查找。
 search 从字符串中任意位置查找，查找到就返回。
 split  根据正则规则拆分字符串
 sub    把正则匹配到的字符串替换掉
 subn   把正则匹配到的字符串替换掉 并返回元组
 findall 根据正则表达式获取所有的数据
 finditer 根据正则生成一个迭代器
"""

str = 'adfa3d56fadf'

# compile把正则规则编译成正则对象
a = re.compile('a')
# 通过正则对象调用match
a.match(str)

# 通过正则模块直接调用match
result = re.match('a', str)

print(result, dir(result))
# print(result.group())

result = re.match('d', str)
print(result)

result = re.search('d', str)
print(result, result.group())

print('**'*50)

strs = 'adfa3d56fadf'
d = re.compile('d')
result = d.search(strs, 2, 6)
# result.group() 获取匹配的结果
print(result, result.group(), result.start(), result.end())


strs = 'a1b1c'
result = re.split('1', strs)
print(result, type(result))

strs = 'a1b2c32d42e500fb'
# 拆分字符串
result = re.split('\d+', strs)
print(result, type(result))

strs = 'abcd'
result = re.split('ab', strs)
print(result, type(result))

result = re.split('[ab]', strs)  # 先根据a对字符串进行拆分'','bcd' ,第二次根据b拆分'','','cd'
print(result, type(result))

print('*'*50)

strs = 'ab2cdefg3ab61gse'
# 根据正则替换字符串
result = re.sub('a', 'b', strs)   # 把所有a 替换成b
print(result, type(result))
result = re.sub('a', 'b', strs, 1)  #指定替换次数
print(result, type(result))
result = re.sub('\d+', 'H', strs)   # 把所有的数子替换成 H
print(result)

result = re.subn('\d+', 'H', strs)   # 把所有的数子替换成 H 并返回元组  ('abHcdefgHabHgse', 3)  3替换次数
print(result)

strs = 'song瑜hao帅'
print(re.search('[\u4e00-\u9fa5]', strs))

html = """<li><a href="http://tieba.baidu.com/" data-path="f?kw=">贴吧</a></li>
<li><a href="https://zhidao.baidu.com/" data-path="search?ct=17&pn=0&tn=ikaslist&rn=10&lm=0&word=">知道</a></li>
<li><a href="http://music.baidu.com/" data-path="search?fr=news&ie=utf-8&key=">音乐</a></li>
<li><a href="http://image.baidu.com/" data-path="search/index?ct=201326592&cl=2&lm=-1&tn=baiduimage&istype=2&fm=&pv=&z=0&word=">图片</a></li>
<li><a href="http://v.baidu.com/" data-path="v?ct=3019898888&ie=utf-8&s=2&word=">视频</a></li>
<li><a href="http://map.baidu.com/" data-path="?newmap=1&ie=utf-8&s=s%26wd%3D">地图</a></li>
<li><a href="http://wenku.baidu.com/" data-path="search?ie=utf-8&word=">文库</a></li>
"""
print(re.search('[\u4e00-\u9fa5]', html))

result = re.finditer('[\u4e00-\u9fa5]+', html)  # 根据正则生成一个包含匹配结果（正则对象）的迭代器
print(result, type(result))
reg_obj = next(result)
print(reg_obj, reg_obj.group())
reg_obj = next(result)
print(reg_obj, reg_obj.group())

for reg_obj in result:
    print(reg_obj, reg_obj.group())


# 匹配出所有汉字
result = re.findall('[\u4e00-\u9fa5]+', html)
print(result, type(result))


# re.IGNORECASE 忽略大小写
#
result = re.findall('href="(.*)"\s', html, re.M)
print(result, type(result))


#注意 findall优先级问题

result = re.findall('www.(baidu|taobao).com', 'www.baidu.comwww.taobao.com')
print(result, type(result))  # ['baidu', 'taobao']  # 因为findall会优先把大原子匹配的结果返回，如果想返回整体正则匹配的结果呢？取消小括号作用。

result = re.findall('www.(?:baidu|taobao).com', 'www.baidu.comwww.taobao.com')
print(result, type(result)) # ['www.baidu.com', 'www.taobao.com']

# split优先级问题

ret = re.split('[a-z]', '1a2b3c5d6')
print(ret)  # ['1', '2', '3', '5', '6']

ret = re.split('([a-z])', '1a2b3c5d6')
print(ret)  # ['1', 'a', '2', 'b', '3', 'c', '5', 'd', '6']

# 通过split拆分的字符串，根据正则规则中有没有小括号 执行的结果也不一样
# 如果有小括号 会把 被拆分的字符一起放入列表返回。





strs = """
<div class="g-list" data-v-68804d87=""><div class="list-item"><div class="photo"><a href="http://album.zhenai.com/u/1168096219" target="_blank"><img src="https://photo.zastatic.com/images/photo/292025/1168096219/31717638010881598.png?scrop=1&amp;crop=1&amp;w=140&amp;h=140&amp;cpos=north" alt="是不是我太乖"></a></div> <div class="content"><div class="content1"><a href="http://album.zhenai.com/u/1168096219" target="_blank"><span>是不是我太乖</span></a></div> <div class="content2">
                女, 30岁, 河南郑州, 离异, 157cm, 中专, 未填写
            </div> <div class="introduce">喜欢和心爱的一起旅行，简简单单浪漫度过每一天，不需要多有钱，但是经常会有惊喜<br></div></div> <div class="item-btn">私聊TA</div></div><div class="list-item"><div class="photo"><a href="http://album.zhenai.com/u/1833504031" target="_blank"><img src="https://photo.zastatic.com/images/photo/458377/1833504031/11904616440991968.png?scrop=1&amp;crop=1&amp;w=140&amp;h=140&amp;cpos=north" alt="心如止水"></a></div> <div class="content"><div class="content1"><a href="http://album.zhenai.com/u/1833504031" target="_blank"><span>心如止水</span></a></div> <div class="content2">
                女, 23岁, 河南郑州, 离异, 170cm, 大专, 金融
            </div> <div class="introduce">美好的东西一定会经过千锤百炼来到你身边，该来的总会来。<br></div></div> <div class="item-btn">私聊TA</div></div><div class="list-item"><div class="photo"><a href="http://album.zhenai.com/u/1644191323" target="_blank"><img src="https://photo.zastatic.com/images/photo/411048/1644191323/25959019776138913.png?scrop=1&amp;crop=1&amp;w=140&amp;h=140&amp;cpos=north" alt="千寻"></a></div> <div class="content"><div class="content1"><a href="http://album.zhenai.com/u/1644191323" target="_blank"><span>千寻</span></a></div> <div class="content2">
                女, 41岁, 河南郑州, 离异, 168cm, 大专, 待业
            </div> <div class="introduce">南墙我撞了，故事我忘了，你我不爱了！<br>往后余生，只想谈一场不分手的恋爱！<br></div></div> <div class="item-btn">私聊TA</div></div><div class="list-item"><div class="photo"><a href="http://album.zhenai.com/u/1655268625" target="_blank"><img src="https://photo.zastatic.com/images/photo/413818/1655268625/11255779534034001.jpg?scrop=1&amp;crop=1&amp;w=140&amp;h=140&amp;cpos=north" alt="冰冰"></a></div> <div class="content"><div class="content1"><a href="http://album.zhenai.com/u/1655268625" target="_blank"><span>冰冰</span></a></div> <div class="content2">
                女, 27岁, 河南郑州, 未婚, 178cm, 大专, 其他职业
            </div> <div class="introduce">本人郑州上街土著人，所有的资料都是真实的。净身高178cm,所以希望另一半海拔高一点。180cm以下者勿扰。<br></div></div> <div class="item-btn">私聊TA</div></div><div class="list-item"><div class="photo"><a href="http://album.zhenai.com/u/1505402998" target="_blank"><img src="https://photo.zastatic.com/images/photo/376351/1505402998/12208881323399824.jpg?scrop=1&amp;crop=1&amp;w=140&amp;h=140&amp;cpos=north" alt="花开半夏"></a></div> <div class="content"><div class="content1"><a href="http://album.zhenai.com/u/1505402998" target="_blank"><span>花开半夏</span></a></div> <div class="content2">
                女, 31岁, 河南郑州, 未婚, 163cm, 大学本科, 专业顾问
            </div> <div class="introduce">先说明，我身份证年龄比实际年龄大，我89！<br>非诚勿扰！！！那些玩彩票的短线投资什么的不好意思，请远离！！<br>长相对得起观众，带出去不丢人！！为人真诚善良，希望对方也是真实真诚，干净上进的大男孩儿！<br>性格:有韧性，偏外向，热爱生活，喜欢尝试……喜欢各种风土人情，愿以后青山绿水……灯火阑珊……有人懂有</div></div> <div class="item-btn">私聊TA</div></div><div class="list-item"><div class="photo"><a href="http://album.zhenai.com/u/1599651526" target="_blank"><img src="https://photo.zastatic.com/images/photo/399913/1599651526/31979090332105298.png?scrop=1&amp;crop=1&amp;w=140&amp;h=140&amp;cpos=north" alt="李家三丫头"></a></div> <div class="content"><div class="content1"><a href="http://album.zhenai.com/u/1599651526" target="_blank"><span>李家三丫头</span></a></div> <div class="content2">
                女, 35岁, 河南郑州, 离异, 162cm, 大专, 销售主管
            </div> <div class="introduce">经历过后才知道和谁结婚真的不一样，此生绝不将就，我会等那个对的人出现，然后携手一生！<br></div></div> <div class="item-btn">私聊TA</div></div><div class="list-item"><div class="photo"><a href="http://album.zhenai.com/u/1597032657" target="_blank"><img src="https://photo.zastatic.com/images/photo/399259/1597032657/31720474695778344.jpg?scrop=1&amp;crop=1&amp;w=140&amp;h=140&amp;cpos=north" alt="大郭"></a></div> <div class="content"><div class="content1"><a href="http://album.zhenai.com/u/1597032657" target="_blank"><span>大郭</span></a></div> <div class="content2">
                女, 32岁, 河南郑州, 未婚, 160cm, 高中及以下, 合伙人
            </div> <div class="introduce">一个爱研究吃的想结婚的女人。不以结婚为目的的请你绕个道，不要耽误咱们时间。毕竟时间挺珍贵。<br></div></div> <div class="item-btn">私聊TA</div></div><div class="list-item"><div class="photo"><a href="http://album.zhenai.com/u/1846831430" target="_blank"><img src="https://photo.zastatic.com/images/photo/461708/1846831430/25695013406350906.png?scrop=1&amp;crop=1&amp;w=140&amp;h=140&amp;cpos=north" alt="kiko"></a></div> <div class="content"><div class="content1"><a href="http://album.zhenai.com/u/1846831430" target="_blank"><span>kiko</span></a></div> <div class="content2">
                女, 25岁, 河南郑州, 未婚, 165cm, 中专, 其他职业
            </div> <div class="introduce">目前在新加坡，有计划去日本工作，因为自己也没想好要不要回国。身边的同学满满的都结婚了，心里是有一点也想找一个伴，但是也不强求，资料真实，也是奔着结婚的目的，我是一个比较慢热的人，不太会说话，会有一点男孩子气，蛮独立。想找一个家庭观念比较重的人吧，大一点也OK，然后有一些迷之自信的一些人请离远一点<br></div></div> <div class="item-btn">私聊TA</div></div><div class="list-item"><div class="photo"><a href="http://album.zhenai.com/u/1596803700" target="_blank"><img src="https://photo.zastatic.com/images/photo/399201/1596803700/11812152745600760.jpg?scrop=1&amp;crop=1&amp;w=140&amp;h=140&amp;cpos=north" alt="今宵别梦寒"></a></div> <div class="content"><div class="content1"><a href="http://album.zhenai.com/u/1596803700" target="_blank"><span>今宵别梦寒</span></a></div> <div class="content2">
                女, 35岁, 河南郑州, 未婚, 170cm, 大专, 政府机构
            </div> <div class="introduce">只愿得一人心，白首不分离。蓦然回首，你是否就在灯火阑珊处？<br></div></div> <div class="item-btn">私聊TA</div></div><div class="list-item"><div class="photo"><a href="http://album.zhenai.com/u/1062166483" target="_blank"><img src="https://photo.zastatic.com/images/photo/265542/1062166483/25948407526396870.jpg?scrop=1&amp;crop=1&amp;w=140&amp;h=140&amp;cpos=north" alt="琳达"></a></div> <div class="content"><div class="content1"><a href="http://album.zhenai.com/u/1062166483" target="_blank"><span>琳达</span></a></div> <div class="content2">
                女, 33岁, 河南郑州, 未婚, 160cm, 大学本科, 广告客户经理
            </div> <div class="introduce">用一首歌词，表达我对你的思念之情<br>终于作了这个决定，别人怎么说我不理<br>只要你也一样的肯定<br>我愿意天涯海角都随你去<br>我知道一切不容易<br>我的心一直温习说服自己<br>最怕你忽然说要放弃<br>爱真的需要勇气<br>来面对流言蜚语<br>只要你一个眼神肯定<br>我的爱就有意</div></div> <div class="item-btn">私聊TA</div></div><div class="list-item"><div class="photo"><a href="http://album.zhenai.com/u/1736782327" target="_blank"><img src="https://photo.zastatic.com/images/photo/434196/1736782327/493577205740023.jpg?scrop=1&amp;crop=1&amp;w=140&amp;h=140&amp;cpos=north" alt="律师清清"></a></div> <div class="content"><div class="content1"><a href="http://album.zhenai.com/u/1736782327" target="_blank"><span>律师清清</span></a></div> <div class="content2">
                女, 33岁, 河南郑州, 未婚, 160cm, 大学本科, 律师
            </div> <div class="introduce">我的身份证比真实年龄大3岁，目前有三家顾问单位，平时工作太忙，如果找到合适的我愿意放弃自己的一部分工作，多为家庭付出<br></div></div> <div class="item-btn">私聊TA</div></div><div class="list-item"><div class="photo"><a href="http://album.zhenai.com/u/99882228" target="_blank"><img src="https://photo.zastatic.com/images/photo/24971/99882228/25701463642632196.png?scrop=1&amp;crop=1&amp;w=140&amp;h=140&amp;cpos=north" alt="姝姝"></a></div> <div class="content"><div class="content1"><a href="http://album.zhenai.com/u/99882228" target="_blank"><span>姝姝</span></a></div> <div class="content2">
                女, 28岁, 河南郑州, 未婚, 165cm, 大专, 经销商
            </div> <div class="introduce">不需轰轰烈烈，但求平平淡淡一生一世……<br></div></div> <div class="item-btn">私聊TA</div></div><div class="list-item"><div class="photo"><a href="http://album.zhenai.com/u/1386287718" target="_blank"><img src="https://photo.zastatic.com/images/photo/346572/1386287718/30084026503552125.jpg?scrop=1&amp;crop=1&amp;w=140&amp;h=140&amp;cpos=north" alt="明天你好"></a></div> <div class="content"><div class="content1"><a href="http://album.zhenai.com/u/1386287718" target="_blank"><span>明天你好</span></a></div> <div class="content2">
                女, 24岁, 河南郑州, 未婚, 165cm, 大学本科, 销售专员
            </div> <div class="introduce">想找个情投意合的人真难<br></div></div> <div class="item-btn">私聊TA</div></div><div class="list-item"><div class="photo"><a href="http://album.zhenai.com/u/1312763541" target="_blank"><img src="https://photo.zastatic.com/images/photo/328191/1312763541/11232873080867985.jpg?scrop=1&amp;crop=1&amp;w=140&amp;h=140&amp;cpos=north" alt="笑口常开"></a></div> <div class="content"><div class="content1"><a href="http://album.zhenai.com/u/1312763541" target="_blank"><span>笑口常开</span></a></div> <div class="content2">
                女, 33岁, 河南郑州, 离异, 164cm, 高中及以下, 其他职业
            </div> <div class="introduce">我希望可以找到一个有上进心，相互理解，包容，顾家有责任的人另一半。我是一个比较直接不喜欢虚伪的人，不是一个会交集的人，比较独立顾家，悲伤过后让自己更加清楚明白自己想要的，一直在为自己目标努力奋斗，目前的现状都只是暂时的，我相信越努力越幸运。<br></div></div> <div class="item-btn">私聊TA</div></div><div class="list-item"><div class="photo"><a href="http://album.zhenai.com/u/107258971" target="_blank"><img src="https://photo.zastatic.com/images/photo/26815/107258971/30082750942853964.jpg?scrop=1&amp;crop=1&amp;w=140&amp;h=140&amp;cpos=north" alt="童心"></a></div> <div class="content"><div class="content1"><a href="http://album.zhenai.com/u/107258971" target="_blank"><span>童心</span></a></div> <div class="content2">
                女, 53岁, 河南郑州, 离异, 166cm, 大学本科, 计算机/互联网
            </div> <div class="introduce">寻48-61岁优秀的您，最好当过兵幽默风趣，一起健身，旅游，游泳，看新闻，散步，听音乐等等，共度余生美好时光。<br></div></div> <div class="item-btn">私聊TA</div></div><div class="list-item"><div class="photo"><a href="http://album.zhenai.com/u/1225573261" target="_blank"><img src="https://photo.zastatic.com/images/photo/306394/1225573261/10947577028917948.png?scrop=1&amp;crop=1&amp;w=140&amp;h=140&amp;cpos=north" alt="小匣子"></a></div> <div class="content"><div class="content1"><a href="http://album.zhenai.com/u/1225573261" target="_blank"><span>小匣子</span></a></div> <div class="content2">
                女, 27岁, 河南郑州, 离异, 170cm, 大学本科, 医疗/护理
            </div> <div class="introduce">真实的自己，只想遇到真实的另一半，努力的做好自己，过好真正属于自己的生活，不让家人担心了！<br></div></div> <div class="item-btn">私聊TA</div></div><div class="list-item"><div class="photo"><a href="http://album.zhenai.com/u/100893626" target="_blank"><img src="https://photo.zastatic.com/images/photo/25224/100893626/31897189237120004.png?scrop=1&amp;crop=1&amp;w=140&amp;h=140&amp;cpos=north" alt="小雯"></a></div> <div class="content"><div class="content1"><a href="http://album.zhenai.com/u/100893626" target="_blank"><span>小雯</span></a></div> <div class="content2">
                女, 29岁, 河南郑州, 离异, 164cm, 大学本科, 讲师/助教
            </div> <div class="introduce">真诚相亲，非诚勿扰！系统消息不回复，谢谢！<br></div></div> <div class="item-btn">私聊TA</div></div><div class="list-item"><div class="photo"><a href="http://album.zhenai.com/u/1311759570" target="_blank"><img src="https://photo.zastatic.com/images/photo/327940/1311759570/15456124289555355.jpg?scrop=1&amp;crop=1&amp;w=140&amp;h=140&amp;cpos=north" alt="爱吃鱼的猫"></a></div> <div class="content"><div class="content1"><a href="http://album.zhenai.com/u/1311759570" target="_blank"><span>爱吃鱼的猫</span></a></div> <div class="content2">
                女, 30岁, 河南郑州, 未婚, 168cm, 大专, 传媒/艺术
            </div> <div class="introduce">出淤泥而不染，濯清涟而不妖！<br>只可远观而不可亵玩焉！<br></div></div> <div class="item-btn">私聊TA</div></div><div class="list-item"><div class="photo"><a href="http://album.zhenai.com/u/1828359910" target="_blank"><img src="https://photo.zastatic.com/images/photo/457090/1828359910/322989338526119.jpg?scrop=1&amp;crop=1&amp;w=140&amp;h=140&amp;cpos=north" alt="平凡女孩"></a></div> <div class="content"><div class="content1"><a href="http://album.zhenai.com/u/1828359910" target="_blank"><span>平凡女孩</span></a></div> <div class="content2">
                女, 27岁, 河南郑州, 离异, 168cm, 高中及以下, 销售
            </div> <div class="introduce">L吧流齐玲齐咦久，，能看出这是什么嘛？因结婚太早，没有互相了解，导致俩人婚后性格不合，离异，想找个能够互相理解的另一半，<br></div></div> <div class="item-btn">私聊TA</div></div><div class="list-item"><div class="photo"><a href="http://album.zhenai.com/u/86429015" target="_blank"><img src="https://photo.zastatic.com/images/photo/21608/86429015/31533826535241916.jpg?scrop=1&amp;crop=1&amp;w=140&amp;h=140&amp;cpos=north" alt="Lucky"></a></div> <div class="content"><div class="content1"><a href="http://album.zhenai.com/u/86429015" target="_blank"><span>Lucky</span></a></div> <div class="content2">
                女, 26岁, 河南郑州, 未婚, 162cm, 大专, 客服专员
            </div> <div class="introduce">只要你是真心的，并且能够包容、为对方着想，不是大男子主义，我是都可以接受的。<br></div></div> <div class="item-btn">私聊TA</div></div> <div class="f-pager"><ul class="m-page"><li class="paging-item paging-item--current"><a href="http://city.zhenai.com/zhengzhou/nv/1">1</a> <!----></li><li class="paging-item"><a href="http://city.zhenai.com/zhengzhou/nv/2">2</a> <!----></li><li class="paging-item"><a href="http://city.zhenai.com/zhengzhou/nv/3">3</a> <!----></li><li class="paging-item"><!----> <a>...</a></li><li class="paging-item"><a href="http://city.zhenai.com/zhengzhou/nv/2">下一页</a> <!----></li></ul></div></div>
"""







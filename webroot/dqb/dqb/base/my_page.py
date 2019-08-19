from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def mypage(page_num,obj,one_size=10):
    # 指定每页显示数据条数
    paginator = Paginator(obj, one_size)
    try:
        page = page_num
    except:
        page = 1
    try:
        obj = paginator.page(page)
    except PageNotAnInteger:
        obj = paginator.page(1)
    except EmptyPage:
        obj = []
    # page_list当前页数据，page_sum总页数,page_count信息总条数
    return {'page_list':obj,'page_sum':paginator.num_pages,'page_count':paginator.count}




 # 分页
def Pagination(request,lister,n):  #lister:对象列表  n:每页信息条数
    paginator = Paginator(lister,2)  # 这里的list必须是一个集合对象,1代表把所有的书分页，一页有1个
    #信息总条数
    total = paginator.count
    #最大页数
    count = paginator.num_pages
    #当前页数
    num = request.GET.get('page',n)  # 'page'代表在当前路径后面添加'page'用于分页(http://127.0.0.1:9630/article/page/?page=2);1代表初始页面为第一页
    try:
        num = int(num)
    except:
        num = 1
    if num <= count and num >= 1:
        num = num
    else:
        if num < 1:
            num = 1
        elif num > count:
            num = count
    #当前页内容
    list = paginator.page(num)  # 显示第一页的内容
    return num,list
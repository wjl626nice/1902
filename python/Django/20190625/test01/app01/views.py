from django.shortcuts import render,HttpResponse

from app01.models import *
# Create your views here.
def books(request):
    # 获取当前页
    page = int(request.GET.get('page', 1))
    # 每页要显示的数据
    per_page_count = 10

    # 计算取数据时的开始位置
    start_pos = (page - 1) * per_page_count
    # 计算取数据的结束位置
    end_pos = page * per_page_count

    # 获取数据的总数
    book_count = Books.objects.count()
    # 书的总数 除以 每页显示的数
    page_count, m = divmod(book_count, per_page_count)  # divmod 返回两个元素的元组， 第一个参数是商 第二个参数是余数
    if m:
        # 当余数不为空时 总页数加1
        page_count += 1

    # 规定页面中显示几个分页
    page_show_count = 10
    # 计算当前页码两侧的平均页码
    avg_page_count = page_show_count // 2

    # 页码开始循环的位置
    start_page_show = page - avg_page_count

    # 页码结束循环的位置
    end_page_show = page + avg_page_count

    # 控制页码开始不能出现负数
    if start_page_show <= 0:
        start_page_show = 1
    # 控制页码结束不能超过总页数
    if end_page_show > page_count:
        end_page_show = page_count + 1
        start_page_show -= avg_page_count - 1

    # 首页
    page_html = """<nav aria-label="Page navigation">
      <ul class="pagination">
        <li>
          <a href="/app01/books/" aria-label="Previous">
            <span aria-hidden="true">首页</span>
          </a>
        </li>
    """
    # 上一页
    if page == 1:
        page_html += """
                <li class="disabled">
                  <a href="#" aria-label="Previous">
                    <span aria-hidden="true">上一页</span>
                  </a>
                </li>
            """
    else:
        page_html += """
                    <li>
                      <a href="/app01/books/?page={}" aria-label="Previous">
                        <span aria-hidden="true">上一页</span>
                      </a>
                    </li>
                """.format(page - 1)

    # 中间的页码
    for p in range(start_page_show, end_page_show):
        p = str(p)
        if str(page) == p:
            page_html += '<li class="active"><a href="#">'+p+'</a></li>'
        else:
            page_html += '<li><a href="/app01/books/?page='+p+'">'+p+'</a></li>'

    # 下一页
    if page_count == page:
        page_html += """
                    <li class="disabled">
                      <a href="#" aria-label="Previous">
                        <span aria-hidden="true">下一页</span>
                      </a>
                    </li>
              """
    else:
        page_html += """
                        <li>
                          <a href="/app01/books/?page=%d" aria-label="Previous">
                            <span aria-hidden="true">下一页</span>
                          </a>
                        </li>
                  """ % (page + 1,)
    # 尾页
    page_html += """
               <li>
                 <a href="/app01/books/?page={}" aria-label="Previous">
                   <span aria-hidden="true">尾页</span>
                 </a>
               </li>
               </ul>
            </nav>
           """.format(page_count)

    books = Books.objects.values('id', 'books_name', 'stock', 'sales_num')[start_pos:end_pos]
    print(books)
    # return HttpResponse('分页' + str(page))
    return render(request, 'books.html', {"books": books, 'page_html': page_html})
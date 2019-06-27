class Page:
    def __init__(self, page, page_count, page_url, per_page=10, current_page_count=10):
        """
        初始化分页的所有参数
        :param page:
        :param page_count:
        :param page_url:
        :param per_page:
        :param current_page_count:
        """
        # 获取当前页
        self.page = page
        # 每页要显示的数据
        self.per_page_count = per_page

        # 获取数据的总数
        self.page_count = page_count

        # 设置点击页码跳转的url
        self.page_url = page_url

        # 规定页面中显示几个分页
        page_show_count = current_page_count
        # 计算当前页码两侧的平均页码
        avg_page_count = page_show_count // 2

        # 页码开始循环的位置
        self.start_page_show = page - avg_page_count

        # 页码结束循环的位置
        self.end_page_show = page + avg_page_count

        # 控制页码开始不能出现负数
        if self.start_page_show <= 0:
            self.start_page_show = 1
            self.end_page_show = page_show_count + 1

        # 控制页码结束不能超过总页数
        if self.end_page_show > page_count:
            self.end_page_show = page_count + 1
            self.start_page_show = page_count - page_show_count + 1
            # 控制有人恶意输入很大的页码
            self.page = page_count

        # 计算取数据时的开始位置
        self.start_pos = (page - 1) * per_page
        # 计算取数据的结束位置
        self.end_pos = page * per_page

    def get_page_show(self):
        """
        根据初始化的参数拼接page分页
        :return:
        """
        # 首页
        page_html = """<nav aria-label="Page navigation">
              <ul class="pagination">
                <li>
                  <a href="{}" aria-label="Previous">
                    <span aria-hidden="true">首页</span>
                  </a>
                </li>
            """.format(self.page_url,)
        # 上一页
        if self.page == 1:
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
                              <a href="{}?page={}" aria-label="Previous">
                                <span aria-hidden="true">上一页</span>
                              </a>
                            </li>
                        """.format(self.page_url, self.page - 1)

        # 中间的页码
        for p in range(self.start_page_show, self.end_page_show):
            p = str(p)
            if str(self.page) == p:
                page_html += '<li class="active"><a href="#">' + p + '</a></li>'
            else:
                page_html += '<li><a href="'+self.page_url+'?page=' + p + '">' + p + '</a></li>'

        # 下一页
        if self.page_count == self.page:
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
                                  <a href="%s?page=%d" aria-label="Previous">
                                    <span aria-hidden="true">下一页</span>
                                  </a>
                                </li>
                          """ % (self.page_url, self.page + 1)
        # 尾页
        page_html += """
                       <li>
                         <a href="{}?page={}" aria-label="Previous">
                           <span aria-hidden="true">尾页</span>
                         </a>
                       </li>
                       </ul>
                    </nav>
                   """.format(self.page_url, self.page_count)

        return page_html
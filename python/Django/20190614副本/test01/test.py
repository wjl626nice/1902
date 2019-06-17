import re
str = """
<div class="img">
					<a href="http://www.xiaohuar.com/p-1-2066.html" target="_blank"><img width="210" alt="上海旅游高等专科学校校花徐谦" src="/d/file/20190613/smalla6a1b2ab88fe4f4e0daa27344ed1542f1560419513.jpg"></a>
					<span class="price">徐谦</span>
					<div class="btns" style="display: none;">
						<a href="http://www.xiaohuar.com/" class="img_album_btn">上海旅游高等专科学校</a>
					</div>
				</div>
"""

res = re.findall('<div class="img">.*?"(.*?)".*?"price">(.*?)</span>', str, re.DOTALL)  # re.DOTALL  点可以代表所有字符
print(res)
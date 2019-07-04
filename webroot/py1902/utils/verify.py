import random
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO
from django.conf import settings
import os
import base64

# 字体路径
FONT_PATH = os.path.join(settings.BASE_DIR, 'static', 'font', 'Yahei.ttf')  # 字体
# 显示几个验证码
LEN_VERIFY = 4

def get_verify():
    verify_len = LEN_VERIFY
    weight = 108
    hight = 41
    # 大写字母，小写字母，数字
    txt_list = [48, 49, 50, 51, 52, 53, 54, 55, 56, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,81,82, 83, 84, 85, 86, 87, 88, 89, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110,111,112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]
    # 画布
    image = Image.new('RGBA', (weight, hight), (255, 255, 255))
    # 字体对象
    font = ImageFont.truetype(FONT_PATH, 20)
    draw = ImageDraw.Draw(image)
    # 填充背景
    for x in range(weight):
        for y in range(hight):
            draw.point((x, y), fill=(200, 200, 200))

    # 生成随机验证码
    verify = ''
    for t in range(verify_len):
        # chr 从十进制转换对应的字符
        text = chr(txt_list[random.randint(0, len(txt_list) - 1)])
        # 在图片上显示的字符
        verify += text
        # 向画布上绘制 验证码
        draw.text(((weight // verify_len) * t + 7, 10), text, font=font,
	    fill=(random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)))
    # 实例化 字节io（输入 输出）对象
    img_buffer = BytesIO()
    # 把内存中的画布保存成一个png图片
    image.save(img_buffer, 'PNG')
    base = img_buffer.getvalue()
    return base, verify
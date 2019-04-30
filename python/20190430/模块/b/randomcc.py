from PIL import Image, ImageDraw, ImageFont, ImageFilter

import random


# 随机字母:
def rndChar():
    list1 = list(range(48, 58)) + list(range(65, 91)) + list(range(97, 123))
    return chr(random.choice(list1))


# 随机颜色1:
def rndColor():
    return (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))


# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


def checkCode():
    # 240 x 60:
    width = 60 * 4
    height = 60
    image = Image.new('RGB', (width, height), (255, 255, 255))
    # 创建Font对象:
    font = ImageFont.truetype('Arial.ttf', 36)
    # 创建Draw对象:
    draw = ImageDraw.Draw(image)
    # 填充每个像素:
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=rndColor())
    # 输出文字:
    cc = ""
    for t in range(4):
        tempcc = rndChar()
        cc += tempcc
        draw.text((60 * t + 10, 10), tempcc, font=font, fill=rndColor2())
    # 模糊:
    image = image.filter(ImageFilter.BLUR)
    image.save('code.jpg', 'jpeg')

    return cc

# print(checkCode())

# 旋转幕布
# https://www.cnblogs.com/meelo/p/4298579.html
# def rotate(self):
#     rot = self.image.rotate(random.randint(-10,10),expand=0) #默认为0，表示剪裁掉伸到画板外面的部分
#     fff = Image.new('RGBA',rot.size,(255,)*4)
#     self.image = Image.composite(rot,fff,rot)
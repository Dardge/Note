from django.shortcuts import render
from PIL import Image, ImageFont, ImageDraw
from django.http import HttpResponse, Http404
import random


# Create your views here.
def verify(request):
    return render(request, 'index.html')


def rmdRGB():
    """
    普通函数，返回一个颜色的随机数
    :return:
    """
    c1 = random.randrange(0, 255)
    c2 = random.randrange(0, 255)
    c3 = random.randrange(0, 255)
    return c1, c2, c3


def verify_code(request):
    # 创建画布
    bgcolor = '#997670'
    width = 100
    height = 25
    im = Image.new('RGB', (width, height), bgcolor)
    # 创建画笔
    draw = ImageDraw.Draw(im)
    # 画内容
    # 画干扰线
    # line((xy),fill=color)
    for i in range(8):
        x1 = random.randrange(0, width)
        x2 = random.randrange(0, width)
        y1 = random.randrange(0, height)
        y2 = random.randrange(0, height)
        # 因为画布指定模式为RGB颜色表示为(255,0,0)
        draw.line((x1, y1, x2, y2), fill=rmdRGB())
    # 画小圆点
    for i in range(100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    # 字体  去掉有歧义的 如 0o 1lL
    str_list = '23456789abcdefghigkmnpqrstuvwxyzABCDEFGHIGKMNPQRSTUVWXYZ'
    # 保存要写的验证码
    rand_str = ''
    for s in range(4):
        rand_str += str_list[random.randrange(0, len(str_list))]
    # 构造字体颜色
    font_colors = ['red', 'orange', 'yellow', 'green', 'lightblue', 'blue', 'purple']

    # 指定字体（操作系统兼容）
    import sys
    if sys.platform == 'win32':
        font = ImageFont.truetype(r'C:\Windows\Fonts\Arial.ttf', 23)
    elif sys.platform == 'darwin':
        font = ImageFont.truetype('/Libra/Fonts/Arial.ttf', 23)
    elif sys.platform == 'linux':
        font = ImageFont.truetype('/usr/share/fonts/truetype/fonts-japanese/Arial.ttf', 23)
    else:
        raise Http404('暂不支持此操作系统')

    # draw.text((5,2),rand_str[0],fill=random.sample(font_colors,1)[0])
    draw.text((5, 2), rand_str[0], fill=random.choice(font_colors), font=font)
    draw.text((25, 2), rand_str[1], fill=random.choice(font_colors), font=font)
    draw.text((45, 2), rand_str[2], fill=random.choice(font_colors), font=font)
    draw.text((65, 2), rand_str[3], fill=random.choice(font_colors), font=font)

    # 结束
    del draw
    # 储存验证码session
    request.session['verifycode'] = rand_str
    print('verifycode：' + rand_str)
    # 将内容保存成一个图片返回
    import io
    # 获得一个缓存区
    buf = io.BytesIO()
    # 将图片保存到缓存区 格式为png
    im.save(buf, 'png')
    # 将缓存区中的内容返回给前端，把缓存区的所有数据读取给前端
    return HttpResponse(buf.getvalue(), 'images/png')

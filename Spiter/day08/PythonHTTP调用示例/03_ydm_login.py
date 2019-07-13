from selenium import webdriver
from ydmapi import *
# 处理图片
from PIL import Image

options = webdriver.ChromeOptions()
options.add_argument('windows-size=1900x3000')
browser = webdriver.Chrome(options=options)


# 获取网站首页截图
def get_screen_shot():
    browser.get('http://www.yundama.com')
    browser.save_screenshot('index.png')

# 从首页截图中截取验证码图片
def get_caphe():
    # 定位验证码元素的位置(x y坐标)
    location = browser.find_element_by_xpath(
        '//*[@id="verifyImg"]'
    ).location
    # 大小(宽度和高度)
    size = browser.find_element_by_xpath(
        '//*[@id="verifyImg"]'
    ).size
    # 左上角x坐标
    left = location['x']
    # 左上角y坐标
    top = location['y']
    # 右下角x坐标
    right = location['x']  + size['width']
    # 右下角y坐标
    bottom = location['y'] + size['height']

    # 截图验证码图片(crop()):对图片进行剪切,参数为元组
    img = Image.open('index.png').crop((left,top,right,bottom))
    # 保存截取后的图片
    img.save('yzm.png')

    # 调用在线打码平台进行识别
    result = get_result('yzm.png')

    return result

if __name__ == '__main__':
    get_screen_shot()
    result = get_caphe()
    print('识别结果为:',result)























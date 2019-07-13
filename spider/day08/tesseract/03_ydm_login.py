from selenium import webdriver
# from .ydmapi import *
from PIL import Image
import pytesseract

# 创建ChromeOptions对象
options = webdriver.ChromeOptions()
# 添加无界面参数hesdless
# options.add_argument('--headless')
options.add_argument('--window-size=1920,3000')
# 创建浏览器对象
browser = webdriver.Chrome(executable_path='D:\Google\Chrome\Application\chromedriver.exe', options=options)


# # 添加无界面
# browser.i = 0


# option=webdriver.FirefoxOptions()
# option.add_argument()


# 获取网站首页截图
def get_screen_shot():
    browser.get('http://www.yundama.com')
    browser.save_screenshot('index.png')


def get_caphe():
    # 定位验证码元素的位置(x,y坐标)
    location = browser.find_element_by_xpath('//*[@id="verifyImg"]').location
    # 大小(宽度和高度)
    size = browser.find_element_by_xpath('//*[@id="verifyImg"]').size
    print(location, size)
    # 左上角x坐标，
    left = location['x']
    # 左上角y坐标
    top = location['y']
    # 右下角x坐标
    right = location['x'] + size['width']
    # 右下角y坐标
    bottom = location['y'] + size['height']

    # 截图验证码图片(crop()):对图片进行截切，参数为元祖
    img = Image.open('index.png').crop((left, top, right, bottom))
    # 保存截取后的图片
    img.save('yzm.png')

    # 直接调用在线打码平台进行识别
    # result = get_result('yzm.png')
    img = Image.open('yzm.png')
    result = pytesseract.image_to_string(img)
    return result


if __name__ == '__main__':
    get_screen_shot()
    result = get_caphe()
    print('识别结果为：', result)

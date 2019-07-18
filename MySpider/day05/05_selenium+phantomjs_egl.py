from selenium import webdriver
import time

# 1.创建浏览器对象
browser = webdriver.Chrome(executable_path='D:\Google\Chrome\Application\chromedriver.exe')

# 2.输入网址
browser.get('http://www.baidu.com/')

# # 3.获取截图
# browser.save_screenshot('baidu.png')


browser.save_screenshot('666.png')

text = browser.find_element_by_xpath('//*[@id="kw"]')

text.send_keys('赵丽颖')
time.sleep(3)

button = browser.find_element_by_xpath('//*[@id="su"]')

button.click()

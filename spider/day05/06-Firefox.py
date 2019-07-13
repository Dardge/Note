from selenium import webdriver

browser = webdriver.Firefox()

browser.get('http://www.baidu.com/')

browser.save_screenshot('666.png')

text = browser.find_element_by_xpath('//*[@id="kw"]')

text.send_keys('赵丽颖')

button = browser.find_element_by_xpath('//*[@id="su"]')

button.click()

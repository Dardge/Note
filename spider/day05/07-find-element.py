from selenium import webdriver

brower = webdriver.Firefox()
brower.get('https://www.qiushibaike.com/text/')

# 单元素查找
one = brower.find_element_by_class_name('content')
print(one.text)

many = brower.find_elements_by_xpath('//div[@class="content"]/span')
for item in many:
    print(item.text)

from selenium import webdriver
import time


class JdSpider(object):
    def __init__(self):
        self.url = 'https://www.jd.com/'
        # 创建ChromeOptions对象
        options = webdriver.FirefoxOptions()
        # 添加无界面参数hesdless
        options.add_argument('--headless')
        # 创建浏览器对象
        self.browser = webdriver.Firefox(options=options)
        # 添加无界面
        self.i = 0


    # 打开京东，输入搜索内容，点击搜索
    def get_page(self):
        self.browser.get(self.url)
        self.browser.find_element_by_xpath('//*[@id="key"]').send_keys('爬虫书籍')
        self.browser.find_element_by_xpath('//*[@class="button"]').click()
        time.sleep(2)

    # 提取商品信息
    def parse_page(self):
        # 执行js脚本，把进度条拉到最底部
        self.browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        # 留出时间加载网页新的商品
        time.sleep(3)
        li_list = self.browser.find_elements_by_xpath('//ul[@class="gl-warp clearfix"]/li')
        # li_list:[li节点1，li节点1，..，li节点30]
        print(len(li_list))
        for li in li_list:
            pruduct_list = li.text.split('\n')
            if pruduct_list[0] == '单价':
                price = pruduct_list[2]
                name = pruduct_list[3]
                comment = pruduct_list[4]
                market = pruduct_list[5]
            else:
                pruduct_list = li.text.split('\n')
                price = pruduct_list[0]
                name = pruduct_list[1]
                comment = pruduct_list[2]
                market = pruduct_list[3]
            print(price, name, comment, market)
            self.i += 1
            print('*' * 30)
        print(self.i)

    def main(self):
        self.get_page()
        while True:
            self.parse_page()
            # 判断是否应该点击下一页
            if self.browser.page_source.find('pn-next disabled') == -1:
                self.browser.find_element_by_class_name('pn-next').click()
                time.sleep(2)
            else:
                break


if __name__ == '__main__':
    spider = JdSpider()
    spider.main()
    spider.browser.quit()

import requests
from lxml import etree

class NoteSpider(object):
    def __init__(self):
        self.baseurl = 'http://code.tarena.com.cn/'
        self.headers = {'User-Agent' : 'Mozilla/5.0'}
        self.auth = ('tarenacode','code_2013')
        self.proxies = {
            'http':'http://1.1.1.1:8888',
            'https':'https://1.1.1.1:8888'
        }

    # 获取一级页面
    def get_one_page(self):
        html = requests.get(
            url=self.baseurl,
            headers=self.headers,
            auth=self.auth,
            timeout=5
        ).text
        # 解析提取数据
        parse_html = etree.HTML(html)
        code_list = parse_html.xpath('//a/@href')
        # code_list: ['../','ACCCode/','AIDCode/']
        print(code_list)
        for code in code_list:
            if not code == '../':
                print(self.baseurl + code)


if __name__ == '__main__':
    spider = NoteSpider()
    spider.get_one_page()







import requests
from lxml import etree
from fake_useragent import UserAgent
import random

class Spider(object):
    def __init__(self):
        self.url = 'https://www.xicidaili.com/nn/'
        # 用来存放所有的代理
        self.proxies_list = []

    # 获取随机ua
    def get_random_ua(self):
        ua = UserAgent()
        ua = ua.random
        print(ua)
        return ua

    # 从西刺代理网站获取IP
    def get_ip_list(self):
        # 请求
        html = requests.get(
            self.url,
            headers={
                'User-Agent':self.get_random_ua()
            }
        ).text
        # 解析
        parse_html = etree.HTML(html)
        tr_list = parse_html.xpath(
                                '//tbody/tr')
        # tr_list: [<element tr>]
        for tr in tr_list[1:]:
            ip = tr.xpath('./td[2]/text()')
            port = tr.xpath('./td[3]/text()')
            proxies = {
                'http' : 'http://{}:{}'.format(ip,port),
                'https': 'https://{}:{}'.format(ip,port)
            }
            self.proxies_list.append(proxies)


if __name__ == '__main__':
    spider = Spider()
    spider.get_ip_list()
    print(spider.proxies_list)












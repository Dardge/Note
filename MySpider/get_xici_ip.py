import random, requests, time, headers
from lxml import etree
from fake_useragent import UserAgent


class Spider(object):
    def __init__(self):
        self.url = 'https://www.xicidaili.com/?tdsourcetag=s_pctim_aiomsg'
        self.proxies_list = []

    # 获取随机的ua
    def get_random_ua(self):
        ua = UserAgent()
        print(ua.random)
        return ua.random

    # 从西刺代理获取IP
    def get_ip_list(self):
        html = requests.get(self.url, headers={'User-Agent': self.get_random_ua()}).text
        parse_html = etree.HTML(html)
        tr_list = parse_html.xpath('//table/tr')
        for tr in tr_list[1:]:
            ip = tr.xpath('./td[2]/text()')
            port = tr.xpath('./td[3]/text()')
            if len(ip) == 1 and len(port) == 1:
                proxies = {
                    'http': 'http://{}:{}'.format(ip[0], port[0]),
                    'https': 'https://{}:{}'.format(ip[0], port[0])
                }
                self.proxies_list.append(proxies)

    def save_text(self):
        with open('ip_list.py', 'a') as f:
            f.write(str(self.proxies_list))

    def main(self):
        self.get_ip_list()
        print(self.proxies_list)
        # self.save_text()

    def get_proxies(self):
        return self.proxies_list


if __name__ == '__main__':
    spider = Spider()
    spider.main()

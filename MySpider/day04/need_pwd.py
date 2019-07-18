import requests, headers, getip, random
from lxml import etree


class NoteSpider(object):
    def __init__(self):
        self.url = 'http://code.tarena.com.cn/AIDCode/aid1902/15_Spider/day01/spider_day01_note.zip'
        self.headers = headers.IE9
        self.auth = ('tarenacode', 'code_2013')
        self.ip_list = getip.get_ip()

    def get_one_page(self):
        while True:
            if not self.ip_list:
                self.ip_list = getip.get_ip()
            ip = random.choice(self.ip_list)
            proxies = {
                'http': 'http://{}'.format(ip),
                'https': 'https://{}'.format(ip)
            }
            try:
                # html = requests.get(url=self.url, proxies=proxies, headers=self.headers, auth=self.auth, timeout=5).content
                html = requests.get(url=self.url, auth=self.auth).content
                # 解析提取数据
                # parse_html = etree.HTML(html)
                # code_list = parse_html.xpath('//pre/a/@href')

                break
            except Exception as e:
                print(e)
                self.ip_list.remove(ip)
                print('{}已删除'.format(ip))
                continue
        with open('abc.zip', 'w') as f:
            f.write(str(html))

    def main(self):
        self.get_one_page()


if __name__ == '__main__':
    spider = NoteSpider()
    spider.main()

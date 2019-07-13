import requests, time, random, headers
from lxml import etree


class Xiushi(object):
    def __init__(self):
        self.baseurl = 'https://www.qiushibaike.com/text/'
        self.headers = headers.IE9

    def get_ulink(self, params):
        html = requests.get(self.baseurl, params=params, headers=self.headers).text
        parse_html = etree.HTML(html)
        ulink_list01 = parse_html.xpath('//a[@class="contentHerf"]/@href')
        # nickname_list = parse_html.xpath('')
        ulink_list = ['https://www.qiushibaike.com' + item for item in ulink_list01]
        pl_number = parse_html.xpath('//span[@class="stats-comments"]/a/i[@class="number"]/text()')
        print('评论数:', pl_number)
        print(len(pl_number))
        print(ulink_list)
        print(len(ulink_list))
        self.get_link(ulink_list)
        time.sleep(random.random())

    def get_link(self, ulink_list):
        for url in ulink_list:
            html = requests.get(url, headers=self.headers).text
            parse_list = etree.HTML(html)
            uname = parse_list.xpath('//span[@class="side-user-name"]/text()')
            content = parse_list.xpath('//div[@class="content"]/text()')
            haoxiao_number = parse_list.xpath('//span[@class="stats-vote"]/i/text()')
            content_str = ''
            for item in content:
                content_str += item
            data = (uname, content_str, haoxiao_number)
            print(data)
            time.sleep(random.random())

    def main(self):
        for page in range(1):
            params = {
                'page': str(page + 1)
            }
            self.get_ulink(params)


if __name__ == '__main__':
    spider = Xiushi()
    spider.main()

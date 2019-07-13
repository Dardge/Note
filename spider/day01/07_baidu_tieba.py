from urllib import request, parse
from headers import headers
import urllib
import time


class BaiduSpider(object):
    def __init__(self):
        self.headers = headers
        self.baseurl = 'https://tieba.baidu.com/f?{}'

    # 获取页面
    def get_page(self, url):
        req = urllib.request.Request(url, headers=self.headers)
        response = urllib.request.urlopen(req)
        html = response.read().decode('utf-8')
        return html

    # 解析页面
    def pare_page(self):
        pass

    # 保存数据
    def write_page(self, filename, html):
        with open(filename, 'w', encoding='gb18030') as f:
            f.write(html)

    # 主函数
    def main(self):
        name = input('请输入贴吧名：')
        start = int(input('请输入起始页：'))
        end = int(input('请输入终止页：'))
        # 发请求保存数据
        for page in range(start, end + 1):
            # 编码拼接URL地址
            pn = (page - 1) * 50
            query_string = {
                'kw': name,
                'pn': str(pn)
            }
            result = parse.urlencode(query_string)
            url = self.baseurl.format(result)
            # 发送请求保存数据
            html = self.get_page(url)
            filename = '{}-第-{}页.html'.format(name, page)
            self.write_page(filename, html)
            print('第%d页爬取成功' % page)
            time.sleep(1)


if __name__ == '__main__':
    spider = BaiduSpider()
    spider.main()

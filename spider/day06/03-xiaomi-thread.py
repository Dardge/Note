import requests, time
import json
from threading import Thread
from queue import Queue
from multiprocessing import Process
from lxml import etree


class XiaoMi(object):
    def __init__(self):
        self.url = 'http://app.mi.com/categotyAllListApi?page={}&categoryId=2&pageSize=30'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
        # 创建队列
        self.q = Queue()
        self.q2 = Queue()
        self.data_list = []
        self.list = []

    # URL进入队列
    def url_in(self):
        for page in range(67):
            url = self.url.format(page)
            # 入队列
            self.q.put(url)

    # 线程事件函数：获取队列中URL，发请求解析处理数据
    def get_data(self):
        while True:
            # 获取URL
            if not self.q.empty():
                url = self.q.get()
                html = requests.get(url, headers=self.headers).text
                data = json.loads(html)
                for item in data['data']:
                    name = item['displayName']
                    href = item['packageName']
                    link = 'http://app.mi.com/details?id=' + href
                    self.q2.put(link)
                    one_data = [name, link]
                    self.data_list.append(one_data)
                    print(one_data)

                    # d = {
                    #     '应用名称': name,
                    #     '链接': link
                    # }
                    # with open('xiaomi.json', 'a') as f:
                    #     json.dump(d, f, ensure_ascii=False)
            else:
                break

    def download_link(self):
        while True:
            if not self.q2.empty():
                url = self.q2.get()
                html2 = requests.get(url, headers=self.headers).text
                parse_html = etree.HTML(html2)
                download_link = parse_html.xpath('/html/body/div[6]/div[1]/div[2]/div[1]/div/div[2]/a/@href')
                self.list.append(download_link)
                print(download_link)
            else:
                break

    def main(self):
        # 入队列
        self.url_in()
        t_list = []
        # 创建多个线程并启动线程
        for i in range(10):
            t = Thread(target=self.get_data)
            t.start()
            t_list.append(t)

        # time.sleep(0.1)
        # for i in range(50):
        #     t2 = Thread(target=self.download_link)
        #     t2.start()
        #     t_list.append(t2)

        # # 创建多个进程
        # for i in range(10):
        #     p = Process(target=self.get_data)
        #     p.start()
        #     t_list.append(p)

        # 回收线程
        for t in t_list:
            t.join()
        print(len(self.data_list))
        print(len(self.list))


if __name__ == '__main__':
    start = time.time()
    spider = XiaoMi()
    spider.main()
    end = time.time()
    print('执行时间：%.2f' % (end - start))

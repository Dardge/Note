import requests, random, headers, proxies
from lxml import etree
from queue import Queue
from threading import Thread


class Xici(object):
    def __init__(self):
        self.url = 'https://www.xicidaili.com/nn/{}'
        self.headers = headers.safari5_MAC
        self.ip_list = proxies.ip_list
        self.usable_proxies_list = []
        self.proxies_list = []
        self.q = Queue()
        self.r = Queue()
        self.t_list = []

    def page_url_to_queue(self):
        for page in range(2):
            url = self.url.format(page + 1)
            self.q.put(url)

    def parse_html(self):
        while True:
            if not self.q.empty():
                url = self.q.get()
                while True:
                    if not self.ip_list:
                        print('IP池空了！')
                        return
                    proxies = self.ip_list.pop(random.randint(0, len(self.ip_list)))
                    try:
                        html = requests.get(url=url, proxies=proxies, headers=self.headers).text
                        self.usable_proxies_list.append(proxies)
                        tr_list = etree.HTML(html).xpath('//*[@id="ip_list"]//tr')
                        for tr in tr_list[1:]:
                            ip = tr.xpath('./td[2]/text()')[0].strip()
                            port = tr.xpath('./td[3]/text()')[0].strip()
                            if ip and port:
                                proxies1 = {
                                    'http': 'http://{}:{}'.format(ip, port),
                                    'https': 'https://{}:{}'.format(ip, port)
                                }
                                t = Thread(target=self.save_ip, args=(proxies1,))
                                t.start()
                                self.t_list.append(t)
                        break
                    except Exception:
                        print("{}----{}已移除".format(url[-1:], proxies))
                        continue
            else:
                break

    def save_ip(self, proxies):
        with open('proxies.txt', 'a') as f:
            f.write(str(proxies))
        print('{}保存成功'.format(proxies))

    def save_usable_proxies(self):
        for proxies in self.usable_proxies_list:
            print(proxies, '=============================================')
            with open('usable-proxies.txt', 'a') as f:
                f.write(str(proxies))
        print('本次使用的可用proxies保存成功')

    def main(self):
        self.page_url_to_queue()
        for i in range(2):
            t = Thread(target=self.parse_html)
            t.start()
            self.t_list.append(t)

        for t in self.t_list:
            t.join()

        self.save_usable_proxies()


if __name__ == '__main__':
    spider = Xici()
    spider.main()

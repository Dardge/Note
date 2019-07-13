import requests, json, time
from fake_useragent import UserAgent
from threading import Thread
from queue import Queue


class TencentSpider(object):
    def __init__(self):
        self.headers = {'User-Agent': self.get_random_ua()}
        self.one_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?pageIndex={}&pageSize=10'
        self.two_url = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId?postId={}'
        self.q = Queue()

    def get_random_ua(self):
        ua = UserAgent()
        print(ua.random)
        return ua.random

    def url_in(self):
        for pageindex in range(11):
            url = self.one_url.format(pageindex)
            self.q.put(url)

    def parse_one_page(self):
        while True:
            if not self.q.empty():
                url = self.q.get()
                res = requests.get(url, headers=self.headers)
                html = json.loads(res.text)
                for job in html['Data']['Posts']:
                    job_name = job['RecruitPostName']
                    post_id = job['PostId']
                    job_duty, job_requirement = self.parse_two_page(self.two_url.format(post_id))
                    print(job_name, job_duty, job_requirement,end='\n')
            else:
                break

    def parse_two_page(self, url2):
        html = requests.get(url2, headers=self.headers).json()
        job_duty = html['Data']['Responsibility']
        job_requirement = html['Data']['Requirement']
        return job_duty, job_requirement

    def main(self):
        self.url_in()
        t_list = []
        for i in range(50):
            t = Thread(target=self.parse_one_page)
            t.start()
            t_list.append(t)

        for t in t_list:
            t.join()


if __name__ == '__main__':
    start = time.time()
    spider = TencentSpider()
    spider.main()
    end = time.time()
    print("执行时间：%.2f" % (end - start))

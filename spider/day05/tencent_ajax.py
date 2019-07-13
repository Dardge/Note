import requests, json
from fake_useragent import UserAgent


class TencentSpider(object):
    def __init__(self):
        self.headers = {'User-Agent': self.get_random_ua()}
        self.one_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?pageIndex={}&pageSize=10'
        self.two_url = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId?postId={}'

    def get_random_ua(self):
        ua = UserAgent()
        return ua.random

    def get_page(self, url):
        res = requests.get(url, headers=self.headers)
        html = json.loads(res.text)
        return html

    def parse_one_page(self, html):
        for job in html['Data']['Posts']:
            job_name = job['RecruitPostName']
            post_id = job['PostId']
            job_duty, job_requirement = self.parse_two_page(self.two_url.format(post_id))
            print('$$$$$$$$$$$$', job_name, '=========', job_duty, '************', job_requirement)

    def parse_two_page(self, two_url):
        html = self.get_page(two_url)
        job_duty = html['Data']['Responsibility']
        job_requirement = html['Data']['Requirement']
        return job_duty, job_requirement

    def main(self):
        for pageindex in range(2, 3):
            url = self.one_url.format(pageindex)
            html = self.get_page(url)
            self.parse_one_page(html)


if __name__ == '__main__':
    spider = TencentSpider()
    spider.main()

import requests, json, time, random, ip_list
from fake_useragent import UserAgent
import string


class BiliBili(object):
    def __init__(self):
        self.url = 'http://api.vc.bilibili.com/board/v1/ranking/top?'

    def get_json(self):
        for offset in range(1, 22, 10):
            params = {
                'page_size': '10',
                'offset': str(offset),
                'tag': '小视频',
                'type': 'tag_general_week',
                'platform': 'pc'
            }
            res = requests.get(self.url, params=params, headers={'User-Agent': self.get_random_ua()})
            html = json.loads(res.text)
            self.parse_page(html)

    def get_random_ua(self):
        ua = UserAgent()
        return ua.random

    def get_random_proxies(self):
        pass

    def parse_page(self, html):
        for it in html['data']['items']:
            url = it['item']['video_playurl']
            print(url)
            name = it['item']['description'].strip()
            str = string.punctuation + string.whitespace
            for char in name:
                if char in str:
                    name = name.replace(char, '')
            # 文件名不能超过255个字符(ubuntu中)
            if len(name) >= 50:
                name = name[:51]
            print(name)
            video = requests.get(url, headers={'User-Agent': self.get_random_ua()}).content
            with open('{}.mp4'.format(name), 'wb') as f:
                f.write(video)
            time.sleep(random.random())

    def main(self):
        self.get_json()


if __name__ == '__main__':
    spider = BiliBili()
    spider.main()

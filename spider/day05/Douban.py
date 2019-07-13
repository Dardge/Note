import requests, ip_list, json
from fake_useragent import UserAgent


class DouBan(object):
    def __init__(self):
        self.url = 'https://movie.douban.com/j/chart/top_list'
        # self.headers = {'User-Agent': ''}

    # 获取随机的ua
    def get_random_ua(self):
        ua = UserAgent()
        # print(ua.random)
        return ua.random

    def get_page(self, params):
        resp = requests.get(self.url, params=params, headers={'User-Agent': self.get_random_ua()}, verify=False)
        # resp = requests.get(self.url, headers=self.headers, verify=False)
        # html = resp.json()
        html = json.loads(resp.text)
        self.parse_page(html)

    # 解析家保存数据
    def parse_page(self, html):
        # html:[{},{},{}]
        for film in html:
            # 名称
            name = film['title']
            # 评分
            score = film['score']
            print({'name': name, 'score': score})
        # print(html)

    def main(self):
        menu = '''1.剧情
2.\033[31m动作\033[0m
3.喜剧
请选择（\033[31m1\033[0m/\033[31m2\033[0m/\033[31m3\033[0m）
 '''
        c = input(menu)
        ty_dict = {'1': '11', '3': '24', '2': '5'}

        n = input("请输入电影数量：")
        # 定义查询参数
        params = {
            'type': c,
            'interval_id': '100:90',
            'action': '',
            'start': '0',
            'limit': n
        }
        self.get_page(params)


if __name__ == '__main__':
    d = DouBan()
    d.main()

from urllib import request
import re, headers, pymysql, time, random, pymongo, csv


class FilmSkySpider(object):
    def __init__(self):
        self.baseurl = 'https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'
        self.headers = headers.IE9
        self.mysql_db = pymysql.connect('localhost', 'root', '666666', 'skymovie', charset='utf8')
        self.cursor = self.mysql_db.cursor()
        self.mongo_conn = pymongo.MongoClient('localhost', 27017)
        self.mongo_db = self.mongo_conn['skymovie']
        self.myset = self.mongo_db['movie_link']

    def get_html(self, url):
        req = request.Request(url, headers=self.headers)
        resp = request.urlopen(req)
        html = resp.read().decode('gb18030', 'ignore')
        return html

    def get_tow_page(self, link):
        html = self.get_html(link)
        # 解析
        pattern = re.compile('<td style="WORD-WRAP: .*?<a href="(.*?)">', re.S)
        return pattern.findall(html)

    # 解析一级页面
    def parse_one_page(self, html):
        pattern = re.compile('<table width="100%".*?<a href="(.*?)" class="ulink">(.*?)</a>', re.S)
        film_list = pattern.findall(html)
        # print(film_list)
        data_list = []
        for file in film_list:
            name = file[1].strip()
            link = 'https://www.dytt8.net' + file[0].strip()
            download_link = self.get_tow_page(link)
            # print(download_link)
            L = [name, download_link[0]]
            data_list.append(L)
            # print(L)
        print(data_list)
        # self.save_mysql(data_list)
        # self.save_mongo(data_list)
        self.save_csv(data_list)

    def save_mysql(self, data_list):
        sql = 'insert into movie_link(name ,link) values(%s,%s)'
        self.cursor.executemany(sql, data_list)
        self.mysql_db.commit()

    def save_mongo(self, data_list):
        data_set = [{'电影名': item[0], '磁力链接': item[1]} for item in data_list]
        self.myset.insert_many(data_set)

    def save_csv(self, data_list):
        with open('电影天堂.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['电影名', '磁力链接'])
            writer.writerows(data_list)

    def main(self):
        for page in range(1):
            url = self.baseurl.format((page + 1))
            html = self.get_html(url)
            self.parse_one_page(html)
            print('第%d页' % (page + 1) + url)
            time.sleep(random.random())
        self.cursor.close()
        self.mysql_db.close()


if __name__ == '__main__':
    spider = FilmSkySpider()
    spider.main()

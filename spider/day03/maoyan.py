import requests, time, csv, headers, random, pymongo, pymysql
from lxml import etree


class Movie(object):
    def __init__(self):
        self.baseurl = 'https://maoyan.com/board/4?offset={}'
        self.headers = headers.safari5_Windows
        # 创建3个对象
        # self.conn = pymongo.MongoClient('localhost', 27017)
        # self.db = self.conn['maoyan']
        # self.myset = self.db['filmaet']
        # self.mysql_db = pymysql.connect('localhost', 'root', '666666', 'maoyandb', charset='utf8')
        # self.cursor = self.mysql_db.cursor()

    def get_page(self, url):
        response = requests.get(url, headers=self.headers)
        response.encoding = 'utf-8'
        html = response.text
        return html

    def save_html(self, filename, html):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html)

    # 使用writerows()方法
    def save_csv(self, data):
        filename = '电影信息.csv'
        with open(filename, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['电影名', '主演', '上映时间'])
            L = []
            for i in range(len(data)):
                tup = (data[i][0].strip(), data[i][1].strip(), data[i][2].strip())
                L.append(tup)
            writer.writerows(L)

    def save_text(self, data):
        filename = '电影信息.txt'
        with open(filename, 'w', encoding='utf-8') as f:
            for i in range(len(data)):
                movie = '%d.电影名：《%s  主演：%s  上映时间：%s%s' % (
                    i + 1, data[i][0] + '》\n\t', data[i][1].strip() + '\n\t', data[i][2].strip() + '\n\t', '\n')
                f.write(movie)

    def save_mongo(self, file_list):
        for i in range(len(file_list)):
            file_dict = {
                '名称': file_list[i][0].strip(),
                '主演': file_list[i][1].strip(),
                '时间': file_list[i][2].strip()
            }
            # 插入数据
            self.myset.insert_one(file_dict)

    def save_mysql(self, file_list):
        sql = 'insert into filmset values (%s,%s,%s)'
        data_list = []
        for i in range(len(file_list)):
            L = [file_list[i][0].strip(), file_list[i][1].strip(), file_list[i][2].strip()[:10]]
            data_list.append(L)
        # self.cursor.executemany(sql, data_list)
        # self.mysql_db.commit()

    def main(self):
        movie_list = []
        for page in range(10):
            url = self.baseurl.format(page + 1)
            html = self.get_page(url)
            parse_html = etree.HTML(html)
            r_list = parse_html.xpath('//*[@id="app"]')
            for r in r_list:
                name_list = r.xpath('.//div/div/div[1]/dl//div/div/div[1]/p[1]/a/text()')
                star_list = [item.strip()[3:] for item in r.xpath('.//div/div/div[1]//div/div[1]/p[2]/text()')]
                time_list = [item.strip()[5:15] for item in r.xpath('.//div/div/div[1]//div/div/div[1]/p[3]/text()')]
            print('第%d页' % (page + 1))
            data = [(name_list[i], star_list[i].strip(), time_list[i].strip()) for i in range(len(name_list)) if
                    len(name_list) == len(star_list) == len(time_list)]
            for item in data:
                movie_list.append(item)
            print(data)
            print(len(name_list))
            time.sleep(random.random())
        print(movie_list)
        print(len(movie_list))
        # self.save_csv(movie_list)
        # self.save_text(movie_list)
        # self.save_mongo(movie_list)
        # self.save_mysql(movie_list)
        # self.cursor.close()
        # self.mysql_db.close()


if __name__ == '__main__':
    m = Movie()
    m.main()

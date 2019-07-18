from urllib import parse, request
import urllib, re, time, csv, headers, random, pymongo, pymysql


class Movie(object):
    def __init__(self):
        self.baseurl = 'https://maoyan.com/board/4?{}'
        self.headers = headers.safari5_Windows
        # 创建3个对象
        self.conn = pymongo.MongoClient('localhost', 27017)
        self.db = self.conn['maoyan']
        self.myset = self.db['filmaet']
        self.mysql_db = pymysql.connect('localhost', 'root', '666666', 'maoyandb', charset='utf8')
        self.cursor = self.mysql_db.cursor()

    def get_page(self, url):
        req = urllib.request.Request(url, headers=self.headers)
        resp = urllib.request.urlopen(req)
        html = resp.read().decode()
        return html

    def save_html(self, filename, html):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html)

    # # 使用writerow()方法
    # def save_csv(self, data):
    #     filename = '电影信息.csv'
    #     with open(filename, 'w') as f:
    #         writer = csv.writer(f)
    #         writer.writerow(['电影名', '主演', '上映时间'])
    #         for i in range(len(data)):
    #             writer.writerow(
    #                 [data[i][0].strip(), data[i][1].strip(), data[i][2].strip()])

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
        self.cursor.executemany(sql, data_list)
        self.mysql_db.commit()

    def main(self):
        movie_list = []
        for page in range(10):
            query_list = {
                'offset': page
            }
            result = parse.urlencode(query_list)
            url = self.baseurl.format(result)
            html = self.get_page(url)
            self.save_html('猫眼电影-第%s页.html' % (page + 1), html)
            pattern = re.compile('item-main">.*?}">(.*?)</a>.*?主演：(.*?)</p>.*?上映时间：(.*?)</p>', re.S)
            data = pattern.findall(html)
            print('第%d页' % (page + 1))
            for r in data:
                # print(r[0], r[1].strip(), r[2].strip())
                movie_list.append(r)
            time.sleep(random.random())
        # self.save_csv(movie_list)
        # self.save_text(movie_list)
        # self.save_mongo(movie_list)
        # self.save_mysql(movie_list)
        self.cursor.close()
        self.mysql_db.close()


if __name__ == '__main__':
    m = Movie()
    m.main()

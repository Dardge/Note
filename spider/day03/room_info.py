import requests, time, csv, headers, pymongo, pymysql, random
from lxml import etree


class RoomInfo(object):
    def __init__(self):
        self.base_url = 'https://ty.lianjia.com/ershoufang/pg'
        self.headers = headers.safari5_Windows
        self.mysql_db = pymysql.connect('localhost', 'root', '666666', 'room', charset='utf8')
        self.cursor = self.mysql_db.cursor()
        self.conn = pymongo.MongoClient('localhost', 27017)
        self.mongo_db = self.conn['room']
        self.myset = self.mongo_db['room_info']

    def get_html(self, url):
        response = requests.get(url, headers=self.headers)
        response.encoding = 'utf-8'
        html = response.text
        return html

    def parse_page(self, html):
        parse_html = etree.HTML(html)
        li_list = parse_html.xpath('//*[@id="content"]')
        title_list = li_list[0].xpath('.//div[1]/ul/li/div[1]/div[1]/a/text()')
        price_list = li_list[0].xpath('.//div[1]/ul/li/div[1]/div[6]/div[1]/span/text()')
        one_page_list = [(title_list[i], price_list[i] + '万') for i in range(len(title_list)) if
                         len(title_list) == len(price_list)]
        print(one_page_list)
        print(len(one_page_list))
        return one_page_list

    def save_mongo(self, data_list):
        tar_list = [{'title': item[0], 'price': item[1]} for item in data_list]
        self.myset.insert_many(tar_list)

    def save_mysql(self, data_list):
        sql = 'insert into room_info(title,price) values (%s,%s)'
        self.cursor.executemany(sql, data_list)
        self.mysql_db.commit()

    def main(self):
        data_list = []
        for page in range(2):
            url = self.base_url + str(page + 1)
            html = self.get_html(url)
            for item in self.parse_page(html):
                data_list.append(item)
            time.sleep(random.random())
        try:
            # self.save_mongo(data_list)
            # self.save_mysql(data_list)
            pass
        except Exception as e:
            print(e)
        print(data_list)
        print(len(data_list))
        self.cursor.close()
        self.mysql_db.close()


if __name__ == '__main__':
    spider = RoomInfo()
    spider.main()

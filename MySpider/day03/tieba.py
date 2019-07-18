from lxml import etree
import requests, headers, time, random, pymongo, pymysql


class Tieba(object):
    def __init__(self):
        self.baseurl = 'http://tieba.baidu.com/f?'
        self.headers = headers.IE9

    def get_html(self, url):
        res = requests.get(url, headers=self.headers)
        res.encoding = 'utf-8'
        html = res.text
        parse_html = etree.HTML(html)
        return parse_html

    def get_src(self, href_list):
        data_list = []
        for href in href_list:
            url = 'http://tieba.baidu.com' + href
            html = requests.get(url, headers=self.headers).text
            parse_html = etree.HTML(html)
            img_src_list = parse_html.xpath(
                '//div[@class="d_post_content_main d_post_content_firstfloor"]/div/cc/div[2]/img/@src|'
                '//div[@class="video_src_wrapper"]/embed/@data-video')
            list01 = (url, img_src_list)
            print(list01)
            data_list.append(list01)
            time.sleep(random.random())
        self.save_mysql(data_list)

    def prase_page(self):
        for page in range(1):
            params = {
                'kw': '校花',
                'pn': str(page * 50)
            }
            res = requests.get(self.baseurl, params=params, headers=self.headers)
            res.encoding = 'utf-8'
            html = res.text
            parse_html = etree.HTML(html)
            second_page_href_list = parse_html.xpath('//div[@class="t_con cleafix"]/div[2]/div/div/a/@href')
            self.get_src(second_page_href_list)
            time.sleep(random.random())

    def save_mysql(self, data_list):
        # 数据处理
        insert_list = []
        for item in data_list:
            if len(item[1]) > 0:
                for i in range(len(item[1])):
                    image = requests.get(item[1][i], headers=self.headers).content
                    one_data = (item[0], image)
                    insert_list.append(one_data)
                    # print(one_data)
        print(insert_list)
        print(len(insert_list))

        # 存入数据库
        db = pymysql.connect('localhost', 'root', '666666', 'tieba', charset='utf8')
        cursor = db.cursor()
        sql = 'insert into picture (ulink,images) values (%s,_binary%s)'
        try:
            cursor.executemany(sql, insert_list)
            db.commit()
        except Exception as e:
            print(e)
        cursor.close()
        db.close()

    def main(self):
        self.prase_page()


if __name__ == '__main__':
    spider = Tieba()
    spider.main()

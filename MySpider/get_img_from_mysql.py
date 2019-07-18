import pymysql


class MySQL(object):
    def __init__(self, database):
        self.db = pymysql.connect('localhost', 'root', '666666', database, charset='utf8', use_unicode=True)
        self.cursor = self.db.cursor()

    def get_info(self, sql):
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            print('数据库操作出错：', e)

    def insert_info(self, sql, data_list):
        try:
            self.cursor.executemany(sql, data_list)
            self.db.commit()
        except Exception as e:
            print('数据库操作出错：', e)


if __name__ == '__main__':
    # sql = 'select images from picture where id=62'
    a = MySQL('maoyan')
    # img_list = a.get_info(sql)
    # print(img_list)
    # for row in img_list:
    #     img = row[0]
    #     print(type(img))
    #     with open('123.jpg', 'wb') as f:
    #         f.write(row[0])

    # sql2 = 'insert into picture(images) values (_binary%s)'
    # fp = open("/code/图库/123.jpg", 'rb')
    # with open('/code/图库/123.jpg', 'rb')as f:
    #     img = f.read()
    # data_list = [(img,), ]
    # a.insert_info(sql2, data_list)
    sql = 'select * from movie_info where id in {}'.format(str((1, 2)))
    b = a.get_info(sql)
    print(b)

    a.cursor.close()
    a.db.close()

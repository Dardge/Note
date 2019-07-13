import pymongo, pymysql

# filmset = 'filmset'
# conn = pymongo.MongoClient('localhost', 27017)
# db = conn['maoyandb']
# myset = db['filmset']
# myset = db.filmset
# myset.insert_one({'name': 'Tiechui'})
# myset.insert_many([{'name', '周芷若'}, {'name', '赵敏'}])


# db = pymysql.connect('localhost', 'root', '666666', 'maoyandb', charset='utf8')
# cursor = db.cursor()
# # 执行数据库插入
# sql = 'insert into filmset values (%s,%s,%s)'
# data_list = [
#     ['大话西游', '周星驰', '1994'],
#     ['喜剧之王', '周星驰', '2000']
# ]
# cursor.executemany(sql, data_list)
# db.commit()
# cursor.close()
# db.close()

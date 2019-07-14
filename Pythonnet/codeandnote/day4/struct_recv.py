from socket import *
import struct
import pymysql 

# 创建数据库游标对象
db = pymysql.connect('localhost','root',\
    '123456','Test')
cursor = db.cursor()

s = socket(AF_INET,SOCK_DGRAM) 
s.bind(('0.0.0.0',8888))

# 确定数据格式(1,b'zhangsan',8,90.5)
st = struct.Struct('i32sif')

while True:
    data,addr = s.recvfrom(1024)
    # 解析数据
    data = st.unpack(data)
    id = data[0]
    name = data[1].decode()
    age = data[2]
    score = data[3]
    print(id,name,age,score)
    # 插入输入库
    sql = "insert into stu values \
        (%d,'%s',%d,%f)"%(id,name,age,score) 
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)

s.close()
db.close()



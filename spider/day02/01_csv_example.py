import csv

with open('test.csv', 'w') as f:
    # 初始化写入对象
    writer = csv.writer(f)
    # 写入数据
    writer.writerow(['大旭', '36'])
    writer.writerows([('大盖伦', '25'), ('QTX', '30')])

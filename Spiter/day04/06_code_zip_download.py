import requests

url = 'http://code.tarena.com.cn/AIDCode/aid1902/15_Spider/day01/spider_day01_note.zip'
auth = ('tarenacode','code_2013')

html = requests.get(url,auth=auth).content
filename = url.split('/')[-1]
with open(filename,'wb') as f:
    f.write(html)












import urllib.request
from urllib import parse

# url = 'https://www.baidu.com/'
# 定义常用变量
url = 'http://httpbin.org/get'
headers = {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'}

# 构建请求对象(重构User-Agent)
request = urllib.request.Request(url, headers=headers)
# 向网站发起请求，得到响应对象
# response = urllib.request.urlopen(url, timeout=1)
response = urllib.request.urlopen(request, timeout=1)
# 获取相应对象内容(html源码)
html = response.read().decode('utf-8')  # bytes数据类型
print(html)
print(response.geturl())  # https://www.sina.com.cn/
print(response.getcode())  # 200
string = {'wd': '赵丽颖'}
s = parse.urlencode(string)
print(s)

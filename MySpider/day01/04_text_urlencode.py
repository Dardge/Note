from urllib import request
from urllib import parse
import urllib
from headers import headers

# 获取url(先编码，再拼接)
baseurl = 'https://www.baidu.com/s?'
query_string = {
    'wd': '赵丽颖',
    'pn': '10',
}
result = parse.urlencode(query_string)
word = input('请输入要搜索的内容：')
result2 = parse.urlencode({'wd': word})
# url = baseurl + result
# url = 'https://www.baidu.com/s?%s' % result
url = 'https://www.baidu.com/s?{}'.format(result2)

# 创建请求头
headers = headers
request = request.Request(url, headers=headers)
# 发起请求获取内容
response = urllib.request.urlopen(request, timeout=1)
html = response.read().decode('utf-8')
# print(html)
print(response.geturl())

# 保存到本地
filename = '{}.html'.format(word)
with open(filename, 'w', encoding='gb18030') as f:
    f.write(html)

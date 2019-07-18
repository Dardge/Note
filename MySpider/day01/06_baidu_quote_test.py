import urllib.request
from headers import headers

# 对字符串编码
word = input("请输入您要搜索的内容：")
# query_string = parse._encode_result(word)
url = 'https://www.baidu.com/s?wd={}'.format(word)
# 创建请求头
headers = headers
request = urllib.request.Request(url, headers=headers)
# 请求
response = urllib.request.urlopen(request)
html = response.read().decode()
print(response.geturl())

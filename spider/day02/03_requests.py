import requests, headers

url = 'https://www.baidu.com.cn/'
res = requests.get(url, headers=headers.Firefox4_MAC)
res.encoding = 'utf-8'
print(res.text)  # 字符串
print(res.encoding)  # utf-8
print(res.content)  # 字节流
print(res.url)  # 返回实际数据的URL地址
print(res.status_code)  # HTTP响应码

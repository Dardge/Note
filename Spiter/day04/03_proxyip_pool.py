from getip import *
import requests
import random

url = 'http://httpbin.org/get'
headers = {'User-Agent' : 'Mozilla/5.0'}
# 获取代理ip的列表['1.1.1.1:8888','']
ip_list = get_ip()

while True:
    proxy_ip = random.choice(ip_list)
    proxies = {
        'http':'http://{}'.format(proxy_ip),
        'https':'https://{}'.format(proxy_ip)
    }
    print(proxies)
    try:
        html = requests.get(url,proxies=proxies,headers=headers).text
        print(html)
        break
    except:
        # 先移除IP
        ip_list.remove(proxy_ip)
        print('{}已经移除'.format(proxy_ip))
        continue












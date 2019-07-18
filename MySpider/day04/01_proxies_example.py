import requests, headers, getip, random
from get_xici_ip import *

# ip_list = getip.get_ip()
proxies_list = Spider().get_proxies()
url = 'http://httpbin.org/get'
while True:
    if not proxies_list:
        print('**********')
        proxies_list = Spider().get_proxies()

    # ip = random.choice(ip_list)
    proxies = random.choice(proxies_list)
    try:
        html = requests.get(url, proxies=proxies, headers=headers.IE9).text
        print(html)
        break
    except:
        # 先移除IP
        proxies_list.remove(proxies)
        print('{}已移除'.format(proxies))
        continue

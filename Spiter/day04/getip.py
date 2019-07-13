import requests
import random

def get_ip():
    url = 'http://dev.kdlapi.com/api/getproxy/?orderid=946143124432413&num=100&protocol=2&method=2&an_an=1&an_ha=1&sep=1'
    headers = {
        'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)'
    }

    html = requests.get(url,headers=headers).text
    ip_list = html.split('\r\n')

    return ip_list

if __name__ == '__main__':
    ip = get_ip()
    print(ip)

from fake_useragent import UserAgent

ua = UserAgent()
print(ua.random)



















import requests

url = 'http://httpbin.org/get'
headers = { 'User-Agent' : 'Mozilla/5.0' }
proxies = {
    'http' : 'http://58.65.128.234:40344',
    'https': 'https://58.65.128.234:40344'
}

html = requests.get(
    url=url,
    proxies=proxies,
    headers=headers
).text

print(html)













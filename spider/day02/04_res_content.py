import requests, headers

url = 'https://ss0.bdstatic.com/94oJfD_bAAcT8t7mm9GUKT' \
      '-xh_/timg?images&quality=100&size=b4000_4000&sec=1561191815&di=229ca9e0c30d5366815a29904a' \
      '0110a4&src=http://b-ssl.duitang.com/uploads/item/201709/09/20170909142847_uYc5M.jpeg'
html = requests.get(url, headers=headers.Opera11_Windows).content  # bites数据类型

with open('杨颖.png', 'wb') as f:
    f.write(html)

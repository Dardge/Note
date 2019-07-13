import requests
from lxml import etree

# 先POST（把用户名和密码post到一个地址
post_url = 'http://www.renren.com/PLogin.do'
post_data = {
    'email': '',
    'password': ''
}

headers = {

}

session = requests.sessions()
session.post(
    url=post_url,
    data=post_data,
    headers=headers
)
# 1.再get（访问需要登陆后才能访问的页面
url = ''
html = session.get(url, headers=headers).text

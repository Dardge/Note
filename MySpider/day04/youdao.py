import requests, random, time
from hashlib import md5


def get_salt_sign_ts(e):
    ts = str(int(time.time() * 1000))
    salt = ts + str(random.randint(0, 10))
    string = "fanyideskweb" + e + salt + "@6f#X3=cCuncYssPsuRUE"
    # 创建md5的加密对象
    s = md5()
    # 进行加密,参数必须为bytes类型
    s.update(string.encode())
    sign = s.hexdigest()
    return salt, sign, ts


def attack_yd(word):
    # 获取salt,sign,ts的值
    salt, sign, ts = get_salt_sign_ts(word)
    # F12扎到的Request URL的地址
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Length": "257",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "td_cookie=18446744072531373120; OUTFOX_SEARCH_USER_ID=-2032502428@10.169.0.84; JSESSIONID=aaa5X3YUuiAgx-7lHXnUw; OUTFOX_SEARCH_USER_ID_NCOO=2133583715.6922483; ___rl__test__cookies=1561452381577",
        "Host": "fanyi.youdao.com",
        "Origin": "http://fanyi.youdao.com",
        # 从哪里过来的
        "Referer": "http://fanyi.youdao.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
    }
    data = {
        "i": word,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": salt,
        "sign": sign,
        "ts": ts,
        "bv": "015fc184d636e7721670f9f2ddb71146",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTlME",
    }
    html = requests.post(url, data=data, headers=headers).json()
    print(html['translateResult'][0][0]['tgt'])


if __name__ == '__main__':
    word = input("请输入：")
    attack_yd(word)

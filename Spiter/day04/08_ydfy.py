import requests
import time
from hashlib import md5
import random

# 获取相关加密算法结果
def get_salt_sign_ts(word):
    # ts
    ts = str(int(time.time() * 1000))
    # salt
    salt = ts +  str(random.randint(0,9))
    # sign
    string = "fanyideskweb" + word + salt +\
                      "@6f#X3=cCuncYssPsuRUE"
    s = md5()
    s.update(string.encode())
    sign = s.hexdigest()
    return salt,sign,ts

# 引用有道翻译
def attack_yd(word):
    # 获取salt,sign,ts的值
    salt,sign,ts = get_salt_sign_ts(word)
    # F12抓到的Request URL的地址
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

    headers = {
        # cookie
        "Cookie": "OUTFOX_SEARCH_USER_ID=-753429634@10.108.160.17; JSESSIONID=aaaULe5n_rFYA4n1tMnUw; OUTFOX_SEARCH_USER_ID_NCOO=1644007711.3741386; ___rl__test__cookies=1561452293484",
        # 从哪里过来的
        "Referer": "http://fanyi.youdao.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
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
        "bv": "b396e111b686137a6ec711ea651ad37c",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTlME",
    }

    # 发请求
    html = requests.post(
        url,data=data,headers=headers).json()
    print(html)

if __name__ == '__main__':
    word = input('请输入要翻译的单词:')
    attack_yd(word)









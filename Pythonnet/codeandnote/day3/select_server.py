# 重要

from select import select
from socket import *

# 创建套接字作为关注的IO 
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 8800))
s.listen(5)

# 添加到关注列表
rlist = [s]
wlist = []
xlist = []

while True:
    # 监控IO
    rs, ws, xs = select(rlist, wlist, xlist)
    for r in rs:
        # s就绪说明有客户端连接
        if r is s:
            c, addr = r.accept()
            print("Connect from", addr)
            # 将客户端套接字加入关注列表
            rlist.append(c)
        # 如果是c就绪则表示对应的客户端发送消息
        else:
            data = r.recv(1024)
            if not data:
                rlist.remove(r)
                r.close()
                continue
            print(data.decode())
            # r.send(b'OK')
            # 当r放入wlist中表示希望主动处理
            wlist.append(r)

    for w in ws:
        w.send(b'OK')
        wlist.remove(w)

    for x in xs:
        pass

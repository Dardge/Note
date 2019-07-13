from select import select 
from socket import * 
import sys 
from time import ctime 

# 日志文件
f = open('log.txt','a')

s = socket()
s.bind(('0.0.0.0',8888))
s.listen(3)

rlist = [s,sys.stdin]
wlist = []
xlist = []

while True:
    rs,ws,xs = select(rlist,wlist,xlist)
    for r in rs:
        if r is s:
            c,addr = r.accept()
            rlist.append(c)
        elif r is sys.stdin:
            name = 'Server'
            time = ctime()
            msg = r.readline()
            f.write('%s  %s  %s\n'%(name,time,msg))
            f.flush() #清缓存
        else:
            addr = r.getpeername()
            time = ctime()
            msg = r.recv(1024).decode()
            f.write('%s  %s  %s\n'%(addr,time,msg))
            f.flush()
f.close()
s.close()
        
        
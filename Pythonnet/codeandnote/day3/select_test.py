from select import select
from socket import * 

f = open('p.jpeg')
s = socket()
s.bind(('127.0.0.1',8800))
s.listen(3)

print("监控IO")
rs,ws,xs = select([s],[],[f],3)
print(rs)
print(ws)
print(xs)
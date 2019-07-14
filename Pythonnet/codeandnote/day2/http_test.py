from socket import * 

# 创建tcp套接字
s = socket()
s.bind(('0.0.0.0',8000))
s.listen(5)

c,addr = s.accept()
print("Connect from",addr)
data = c.recv(4096)
print(data)

c.send(b'Hello world')

c.close()
s.close()

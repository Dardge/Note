from socket import * 

# 创建tcp套接字
s = socket()
s.bind(('0.0.0.0',8001))
s.listen(5)

c,addr = s.accept()
print("Connect from",addr)
data = c.recv(4096)
print(data)

data = '''HTTP/1.1 200 OK
Content-Type: text/html

Hello world
'''
c.send(data.encode())

c.close()
s.close()

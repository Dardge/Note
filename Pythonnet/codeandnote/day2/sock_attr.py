# sock_attr.py
# 套接字属性演示  理解

from socket import *

# 创建套接字对象
s = socket() 

# 设置端口立即重用
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,True)

print(s.family)  # 地址类型
print(s.type) # 套接字类型

s.bind(('0.0.0.0',8888))
print(s.getsockname()) #绑定地址
print(s.fileno())  # 文件描述符

s.listen(3)
c,addr = s.accept()
print(c.getpeername()) # 获取c连接的客户端地址

c.recv(1024)
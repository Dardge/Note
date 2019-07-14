#　tcp_server.py

import socket 

#　TCP创建套接字
sockfd = socket.socket(socket.AF_INET,\
    socket.SOCK_STREAM)

#　绑定地址
sockfd.bind(('0.0.0.0',8888))

#　设置监听
sockfd.listen(3)

#　等待客户端连接
print("Waiting for connect ....")
connfd,addr = sockfd.accept()
print("Connect from",addr) #　客户端地址

# 消息收发
data = connfd.recv(1024)
print("Receive message:",data.decode())

n = connfd.send(b"Receive your message")
print("Send %d bytes"%n)

# 关套接字
connfd.close()
sockfd.close()







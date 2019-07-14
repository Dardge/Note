from socket import *
from time import sleep,ctime 

# 创建tcp套接字
sockfd = socket()
sockfd.bind(('127.0.0.1',8800))
sockfd.listen(3)

# 设置非阻塞状态
# sockfd.setblocking(False)

# 设置超时时间
sockfd.settimeout(3)

while True:
    print("Waiting for connect")
    try:
        connfd,addr = sockfd.accept()
    except BlockingIOError:
        sleep(2)
        print("%s connect error"%ctime())
        continue 
    except timeout:
        print("timeout....")
    else:
        print("Connect from",addr)
        data = connfd.recv(1024)
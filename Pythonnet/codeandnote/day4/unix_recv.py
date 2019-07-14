from socket import * 
import os 

# 本地套接字文件
sock_file = './sock'

# 判断文件存在
if os.path.exists(sock_file):
    os.remove(sock_file) # 删除文件

# 创建本地套接字
sockfd = socket(AF_UNIX,SOCK_STREAM)

# 绑定文件
sockfd.bind(sock_file)

sockfd.listen(3)
while True:
    c,addr = sockfd.accept()
    while True:
        data = c.recv(1024)
        if not data:
            break 
        print(data.decode())
    c.close()
sockfd.close()



# broadcast_send.py  了解

from socket import * 
from time import sleep 

# 目标地址
dest = ('172.40.91.112',9999)

s = socket(AF_INET,SOCK_DGRAM) 

# 设置可以发送接收广播
s.setsockopt(SOL_SOCKET,SO_BROADCAST,True)

data = '''
*********************
   4.4 清明前
   四月未拂杨柳絮
   春风十里不如你  
*********************
'''

while True:
    sleep(2)
    s.sendto(data.encode(),dest)







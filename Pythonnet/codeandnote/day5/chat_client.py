from socket import *
import os,sys 

# 服务器地址
ADDR = ('127.0.0.1',8888)

def udp_client():
    return socket(AF_INET,SOCK_DGRAM)

def login(s):
    while True:
        name = input("请输入姓名:")
        msg = "L " + name # L表示请求类型
        # 给服务器发送
        s.sendto(msg.encode(),ADDR)
        # 等待回复
        data,addr = s.recvfrom(1024)
        if data.decode() == 'OK':
            print("您已进入聊天室")
            break 
        else:
            print(data.decode())
    return name 

def send_msg(s,name):
    while True:
        try:
            text = input("发言:")
        except KeyboardInterrupt:
            text = "quit"
        if text.strip() == 'quit':
            msg = 'Q ' + name
            s.sendto(msg.encode(),ADDR)
            sys.exit("退出聊天室")
        msg = "C %s %s"%(name,text)
        s.sendto(msg.encode(),ADDR) 

def recv_msg(s):
    while True:
        data,addr = s.recvfrom(2048)
        # 收到服务器EXIT则退出
        if data.decode() == 'EXIT':
            sys.exit()
        print(data.decode()+'\n发言:',end='')

def chat(s,name):
    # 创建进程
    pid = os.fork()
    if pid < 0:
        sys.exit("Error!")
    elif pid == 0:
        send_msg(s,name)
    else:
        recv_msg(s)

def main():
    s = udp_client()
    name = login(s)
    chat(s,name)

main()
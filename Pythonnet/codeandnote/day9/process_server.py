from socket import *
from multiprocessing import Process
import signal

# 服务端地址
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST, PORT)


def handle(connfd):
    print("Connect from:", connfd.getpeername())
    while True:
        data = connfd.recv(1024)
        if not data:
            break
        print(data.decode())
        connfd.send(b'OK')
    connfd.close()

# 创建监听套接字
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)
s.bind(ADDR)
s.listen(3)

# 处理僵尸进程
signal.signal(signal.SIGCHLD, signal.SIG_IGN)

# 循环等待客户端连接
while True:
    try:
        c, addr = s.accept()
    except KeyboardInterrupt:
        s.close()
        break
    except Exception as e:
        print(e)
        continue

    # 创建新的进程处理客户端
    p = Process(target=handle, args=(c,))
    p.daemon = True  # 子进程会随主进程退出
    p.start()

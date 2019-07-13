import os 
from time import sleep 

pid = os.fork()

if pid < 0:
    print("Error")
elif pid == 0:
    sleep(3)
    print("Child %d process exit"%os.getpid())
    os._exit(2)
else:
    # pid,status = os.wait()
    # 非阻塞模式
    pid,status = os.waitpid(-1,os.WNOHANG)
    print("pid:",pid)
    # 获取子进程退出
    print("status:",os.WEXITSTATUS(status))
    while True:
        sleep(100)
# 二级子进程处理僵尸
import os 
from time import sleep 

def f1():
    sleep(3)
    print('旭哥爱保健')

def f2():
    sleep(4)
    print("波波有故事")

pid = os.fork()

if pid < 0:
    print("Error")
elif pid == 0:
    p = os.fork() # 创建二级子进程
    if p == 0:
        f1()
    else:
        os._exit(0)  # 一级子进程退出
else:
    os.wait() # 回收一级子进程
    f2()



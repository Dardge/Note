from multiprocessing import Semaphore,Process 
from time import sleep 
import os 

# 创建信号量
sem = Semaphore(3)

# 系统中最多有3个进程同时执行该事件
def fun():
    sem.acquire() # 消耗信号量
    print("%d执行事件"%os.getpid())
    sleep(3)
    print("%d执行完毕"%os.getpid())
    sem.release() # 增加信号量

jobs = []
for i in range(5):
    p = Process(target = fun)
    jobs.append(p)
    p.start()

for i in jobs:
    i.join()

print(sem.get_value())


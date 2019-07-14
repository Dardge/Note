# pipe.py

from multiprocessing import Process,Pipe 
import time,os 

# 创建管道
fd1,fd2 = Pipe(False)

def fun(name):
    time.sleep(3)
    # 写入管道
    fd2.send({name:os.getpid()})

jobs = [] 
for i in range(5):
    p = Process(target=fun,args=(i,))
    jobs.append(p)
    p.start()

for i in  range(5):
    # 读取管道
    data = fd1.recv()
    print(data)

for i in jobs:
    i.join()
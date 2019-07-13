#queue_0.py 
from multiprocessing import Queue,Process 
from time import sleep 

# 创建消息队列
q = Queue(3)

def fun1():
    for i in range(3):
        sleep(1)
        q.put((1,3))

def fun2():
    for i in range(4):
        try:
            a,b = q.get(timeout = 3)
        except:
            return
        print("sum = ",a + b) 

p1 = Process(target = fun1)
p2 = Process(target = fun2)
p1.start()
p2.start()
p1.join()
p2.join()

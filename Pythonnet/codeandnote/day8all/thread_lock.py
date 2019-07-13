# thread_lock.py

from threading import Thread,Lock 

a = b = 0
lock = Lock()  # 创建锁

def value():
    while True:
        lock.acquire()  # 加锁
        if a != b:
            print("a = %d,b = %d"%(a,b))
        lock.release()  # 解锁

t = Thread(target=value)
t.start()
while True:
    with lock:
        a += 1
        b += 1

t.join()


from multiprocessing import Process 
from time import sleep,ctime 

def fun():
    for i in range(3):
        sleep(2)
        print(ctime()) 

p = Process(target = fun,name = "Tedu")

p.daemon = True

p.start()
print("Name:",p.name)
print("PID：",p.pid)
print("alive:",p.is_alive())

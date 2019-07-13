from threading import Thread 
from time import sleep 

def fun():
    sleep(3)
    print("线程属性测试")

t = Thread(target=fun,name = "Tarena")

# 线程名称
t.setName("Tedu")
print("Thread name:",t.name)
print("Thread name:",t.getName())

# 设置daemon值
t.setDaemon(True)

t.start()
print("is alive:",t.is_alive())





from threading import Thread,Event 
from time import sleep 

s = None # 用于通信
e = Event()  # 创建event对象

def 杨子荣():
    sleep(0.1)
    print("杨子荣拜山头")
    global s 
    s = "天王盖地虎"
    e.set()

f = Thread(target=杨子荣)
f.start()

# 验证口令
print("说出口令就是自己人！！！")
e.wait() # 添加阻塞
if s == '天王盖地虎':
    print("确认过眼神，你是对的人")
else:
    print("打死他")

f.join()


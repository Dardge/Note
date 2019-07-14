from multiprocessing import Process 
import time 

# 自定义进程类
class ClockProcess(Process):
    def __init__(self,value):
        self.value = value 
        super().__init__()
    
    # 重写run方法
    def run(self):
        for i in range(5):
            print("The time is %s"%time.ctime())
            time.sleep(self.value)

# 创建进程对象
p = ClockProcess(2)
p.start()
p.join()
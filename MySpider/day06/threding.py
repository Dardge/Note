from queue import Queue
from threading import Thread

q = Queue()
url1 = ''
url2 = ''
url3 = ''
q.put(url1)
# q.empty()  # 判断队列是否为空。True/False
q.get(block=True, timeout=2)  # 2秒钟没有获取到值就抛出异常
if not q.empty():
    q.get()  # 当队列为空时，阻塞

t = Thread(target=函数名)  # 创建线程对象
t.start()  # 启动线程
t.join()  # 阻塞等待回收线程

from multiprocessing import Process,Array 

# 创建共享内存

# shm = Array('i',[1,2,3,4])
# shm = Array('i',5) # 开辟空间大小
shm = Array('c',b"Hello") # 字节串

def fun():
    for i in shm:
        print(i)
    shm[0] = b'h' 
    
p = Process(target = fun)
p.start()
p.join()

for i in shm:
    print(i,end = ' ')

print(shm.value) # 打印字符串







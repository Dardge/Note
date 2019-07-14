from multiprocessing import Process 
import os 

filename = "./test.jpg"
# 获取文件大小
size = os.path.getsize(filename)

f = open(filename,'rb')

# 复制上半部分
def top():
    # f = open(filename,'rb')
    n = size // 2 
    with open('top.jpg','wb') as fw:
        fw.write(f.read(n))
    # f.close()

# 复制下半部分
def bot():
    # f = open(filename,'rb')
    f.seek(size//2,0) # 移动文件偏移量
    with open('bot.jpg','wb') as fw:
        fw.write(f.read())
    # f.close()

t = Process(target = top)
b = Process(target = bot)
b.start()
t.start()
t.join()
b.join()
f.close()




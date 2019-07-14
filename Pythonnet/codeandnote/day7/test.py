# 计算密集
def count(x,y):
    c = 0 
    while c < 7000000:
        x += 1
        y += 1
        c += 1 

# IO密集
def io():
    write()
    read()

def write():
    f = open('test','w')
    for i in range(1700000):
        f.write("hello world\n")

def read():
    f = open('test')
    f.readlines()


# 定义函数：在控制台打印矩形   11:45
def print_rect(r_count,c_count,char):
    for r in range(r_count):
        # 内层循环控制列
        for c in range(c_count):
            print(char,end = "")
        print() # 换行


re = print_rect(3,2,"#")
print(re)


print_rect(5,6,"*")



"""
    文件操作
"""
# 创建一个文件
# 写入hello.
"""
my_file = None
try:
    # open("路径","操作模式",encoding="utf-8")
    my_file = open("my_file01.txt","w",encoding="utf-8")
    # my_file.write("hello\n")
    # my_file.write("你好")
    my_file.write("好吗你？")
finally:
    # 如果文件不是空 则关闭
    if my_file!=None:
        my_file.close()
"""


# with open("my_file01.txt","w",encoding="utf-8") as my_file:
# my_file.write("好吗你？")
# # my_file.close()  当程序执行到with代码块以外，一定会执行close()


# 创建文件夹：
import os
# 不是文件夹或者不存在该文件夹，返回false
# print(os.path.isdir("file_demo"))

# 如果不是文件夹
if not os.path.isdir("file_demo"):
    # 创建文件夹(支持多个)os.makedirs("file_demo/a/b/c")
    os.makedirs("file_demo")

# 操作文件：
with open("file_demo/my_file01.txt","w",encoding="utf-8") as my_file:
    my_file.write("好吗你？")
    # my_file.close()  当程序执行到with代码块以外，一定会执行close()





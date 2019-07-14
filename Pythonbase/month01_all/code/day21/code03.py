"""
    文件操作模式
"""
# 1. w  只写 ： 如果文件不存在，则创建。每次都从头写入（清空之前的内容）。
# with open("file_demo/my_file02.txt","w",encoding="utf-8") as my_file:
#     my_file.write("写入文字\n")
#     str_list=["a\n","b\n","c\n"]
#     my_file.writelines(str_list)

# 2. a 追加:如果文件不存在，则创建。每次都从末尾写入
# with open("file_demo/my_file02.txt","a",encoding="utf-8") as my_file:
#     my_file.write("写入文字\n")
#     str_list=["a\n","b\n","c\n"]
#     my_file.writelines(str_list)

# 3. 只读
with open("file_demo/my_file02.txt","r",encoding="utf-8") as my_file:
    # 读取所有内容
    # print(my_file.read())
    # 读取指定数量的字符
    # print(my_file.read(6))
    # 读取一行
    # print(my_file.readline())
    # 迭代读取
    for line in my_file:
        print(line)







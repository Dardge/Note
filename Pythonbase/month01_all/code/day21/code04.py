"""
    文件二进制操作
"""

# 字节串：存储字节
b01 = b"a" # 97
print(type(b01)) # bytes

# 对二进制文件进行读写操作
with open("MVC.jpg","r+b") as my_file:
    #1. 获取文件操作位置
    print(my_file.tell())# 返回需要操作的位置 0
    #2. 读取文件字节
    temp_bytes = my_file.read()
    #3. 设置文件操作位置
    my_file.seek(0)
    print(my_file.tell()) # 0
    # 反转
    temp_bytes = temp_bytes[::-1]
    #4. 写入字节
    my_file.write(temp_bytes)


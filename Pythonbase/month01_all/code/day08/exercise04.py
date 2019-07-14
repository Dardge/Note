"""
    练习：定义函数，判断字符串中，中文的个数。
        0x4E00  <=  ord(字符) <= 0x9FA5
"""
def get_chinese_char_count(str_target):
    count = 0
    for char in str_target:
        if 0x4E00  <=  ord(char) <= 0x9FA5:
            count+=1
    return count

print(get_chinese_char_count("ajf中文jfkk123qtx分数"))


"""
    字符串字面值
"""

str01 = 'a"b"c'
str01 = "a'b'c"
str01 = """a
            b
                c"""

#　转义符
str02 = "a\"b\"cd"
str02 = "ab\ncd"
str02 = "a\tbc"
str02 ="a\\b\\c\\d.txt"
# r 原始字符：字符串中木有转义符
str02 =r"a\b\c\d.txt"
str02 ="""
   sdfh\"""sadf
"""
print(str02)


#　格式化字符串
# 字符串中嵌套变量
name = "悟空"
sex = "男"
age = 2000
re1 = "他的名字叫："+name+"，性别是："+sex+",年龄是："+str(age)+"．"
re2 = "他的名字叫：%s，性别是：%s,年龄是%d."%(name,sex,age)

print(re1,re2)

str03 = "整数是%4d"%(32) # 整数是  32
str03 = "整数是%04d"%(32) # 整数是0032
str03 = "小数是%.2f"%(1.23456) # 1.23
str03 = "小数是%.2f"%(1.23956) # 小数是1.24
print(str03)














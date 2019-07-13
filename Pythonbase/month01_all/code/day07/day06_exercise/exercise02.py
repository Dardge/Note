"""
作业2：在控制台中获取一段文字，
打印这个文字中出现的字符以及次数。
[(字符,出现次数,编码值)]
{字符:次数}
"""

# 思路：逐一判断字符，计算次数。
#       如果没有统计过，加入到容器。
# 		     统计过， 增加计数
str_input = "asadsfhaasdnwfskdnfln"
result = {}
for item in str_input:
    if item not in result:
        result[item] = 1
    else:
        result[item] += 1

for key in result:
    print("字符:%s---次数:%d"%(key,result[key]))

print()

for item in result.items():
    # (key,vlaue)
    print("字符:%s---次数:%d"%(item[0],item[1]))
# 10:25 上课


















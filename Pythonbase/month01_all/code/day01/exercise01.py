"""
   汇率转换器 
   XXXＥrror
"""

# 1. 获取数据
str_usd = input("请输入美元：")
# 2. 逻辑计算
rmb = int(str_usd) * 6.6935
# 3.　显示结果
result = "人民币：" + str(rmb)
print(result)
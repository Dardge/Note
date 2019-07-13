"""
    一张纸的厚度是0.01毫米
	请问对折多次，可以超过珠穆朗玛峰8844.43米
"""


thickness = 0.01 / 1000
count = 0
while thickness <= 8844.43:
    thickness *= 2
    count += 1
print(count)








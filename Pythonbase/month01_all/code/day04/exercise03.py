"""
    在控制台中打印时间
    120秒显示为：02:00
	  119           01:59
	  …..
      0             00:00
"""

for second in range(120,-1,-1):
    message = "%02d:%02d"%(second // 60,second % 60)
    print(message)

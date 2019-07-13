from hashlib import md5

string = 'elephant'

# 创建md5加密对象
s = md5()
# 进行加密,参数必须为bytes数据类型
s.update(string.encode())
# 获取十六进制加密结果
result = s.hexdigest()

print(result)














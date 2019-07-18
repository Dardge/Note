import re

html = '''
<html>
    <div><p>成也风云</p></div>
    <div><p>败也风云</p></div>
</html>
'''

# 贪婪匹配
pattern = re.compile(r'<div><p>(.*)</p></div>', re.S)
r_list = pattern.findall(html)
print(r_list)

# 非贪婪匹配
pattern = re.compile(r'<div><p>(.*?)</p></div>', re.S)
r_list2 = pattern.findall(html)
print(r_list2)

print(re.compile(r'(\w+)\s+(\w+)', re.S).findall('A B C D'))

html2 = '''
<div class="animal">
	    <p class="name">
			<a title="Tiger"></a>
	    </p>
	    <p class="content">
			Two tigers two tigers run fast
	    </p>
	</div>
	
	<div class="animal">
	    <p class="name">
			<a title="Rabbit"></a>
	    </p>
	
	    <p class="content">
			Small white rabbit white and white
	    </p>
	</div>
'''
title = re.compile(r'title="(.*?)".*?content">(.*?)<', re.S)
# title = re.compile(r'title="(.*?)"', re.S)
f = re.compile(r'"content">(.*?)<', re.S)
title = title.findall(html2)
f = f.findall(html2)
# print(title)
# for i in range(len(title)):
#     print(title[i], f[i])

for r in title:
    print('动物名称：', r[0].strip())
    print('动物描述：', r[1].strip())

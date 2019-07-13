﻿from lxml import etree

html = """
<div class="wrapper">
	<i class="iconfont icon-back" id="back"></i>
	<a href="/" id="channel">新浪社会</a>
	<ul id="nav">
		<li><a href="http://domestic.firefox.sina.com/" title="国内">国内</a></li>
		<li><a href="http://world.firefox.sina.com/" title="国际">国际</a></li>
		<li><a href="http://mil.firefox.sina.com/" title="军事">军事</a></li>
		<li><a href="http://photo.firefox.sina.com/" title="图片">图片</a></li>
		<li><a href="http://society.firefox.sina.com/" title="社会">社会</a></li>
		<li><a href="http://ent.firefox.sina.com/" title="娱乐">娱乐</a></li>
		<li><a href="http://tech.firefox.sina.com/" title="科技">科技</a></li>
		<li><a href="http://sports.firefox.sina.com/" title="体育">体育</a></li>
		<li><a href="http://finance.firefox.sina.com/" title="财经">财经</a></li>
		<li><a href="http://auto.firefox.sina.com/" title="汽车">汽车</a></li>
	</ul>
	<i class="iconfont icon-liebiao" id="menu"></i>
</div>
"""
parse_html = etree.HTML(html)
# 匹配规则  ==================================
# text_xpath = '//ul[@id="nav"]//a/text()'
# href_xpath = '//ul[@id="nav"]//a/@href'
# text_list = parse_html.xpath(text_xpath)
# href_list = parse_html.xpath(href_xpath)

# xpath高级  ==================================
r_list = parse_html.xpath('//ul[@id="nav"]')  # 节点对象列表
for r in r_list:
    text_list = r.xpath('.//a/text()')
    href_list = r.xpath('.//a/@href')
data_list = [(text_list[i], href_list[i]) for i in range(len(text_list))]
print(data_list)
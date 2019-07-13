# **Day06回顾**

## **京东爬虫**



- 执行JS脚本,把进度条拉到最下面

```python
1、js脚本
browser.execute_script(
'window.scrollTo(0,document.body.scrollHeight)'
)
2、利用节点对象的text属性获取当前节点及后代节点的文本内容,想办法处理数据
```

- 设置无界面模式（chromedriver | firefox）

```python
options = webdriver.ChromeOptions()
options.add_argument('--headless')

browser = webdriver.Chrome(options=options)
browser.get(url)
```

## **多线程爬虫**

- 使用流程

```python
# 1、URL队列
q.put(url)
# 2、线程事件函数
while True:
    if not url_queue.empty():
        ...get()、请求、解析
    else:
        break
# 创建并启动线程
t_list = []
for i in range(5):
    t = Thread(target=parse_page)
    t_list.append(t)
    t.start()
# 阻塞等待回收线程
for i in t_list:
    i.join()
```

## **json模块**



- json转python

```python
变量名 = json.loads(res.text)
```

- python转json（保存为json文件）

```python
# 保存所抓取数据为json数据
with open(filename,'a') as f:
	json.dump(字典/列表/元组,f,ensure_ascii=False)
```

## **scrapy框架**

- 五大组件

```python
引擎（Engine）
爬虫程序（Spider）
调度器（Scheduler）
下载器（Downloader）
管道文件（Pipeline）
# 两个中间件
下载器中间件（Downloader Middlewares）
蜘蛛中间件（Spider Middlewares）
```

- 工作流程

```python
1、Engine向Spider索要URL,交给Scheduler入队列
2、Scheduler处理后出队列,通过Downloader Middlewares交给Downloader去下载
3、Downloader得到响应后,通过Spider Middlewares交给Spider
4、Spider数据提取：
   1、数据交给Pipeline处理
   2、需要跟进URL,继续交给Scheduler入队列，依次循环
```

- 常用命令

```python
# 创建爬虫项目
scrapy startproject 项目名

# 创建爬虫文件
cd 项目文件夹
scrapy genspider 爬虫名 域名

# 运行爬虫
scrapy crawl 爬虫名
```

- scrapy项目目录结构

```python
Baidu
├── Baidu               # 项目目录
│   ├── items.py        # 定义数据结构
│   ├── middlewares.py  # 中间件
│   ├── pipelines.py    # 数据处理
│   ├── settings.py     # 全局配置
│   └── spiders
│       ├── baidu.py    # 爬虫文件
└── scrapy.cfg          # 项目基本配置文件
```

- 
  settings.py全局配置

```python
1、USER_AGENT = 'Mozilla/5.0'
2、ROBOTSTXT_OBEY = False
3、CONCURRENT_REQUESTS = 32
4、DOWNLOAD_DELAY = 1
5、DEFAULT_REQUEST_HEADERS={}
6、ITEM_PIPELINES={'项目目录名.pipelines.类名':300}
```

***************************************************
# **Day07笔记**

## **scrapy框架**

- 创建爬虫项目步骤

```python
1、新建项目 ：scrapy startproject 项目名
2、cd 项目文件夹
3、新建爬虫文件 ：scrapy genspider 文件名 域名
4、明确目标(items.py)
5、写爬虫程序(文件名.py)
6、管道文件(pipelines.py)
7、全局配置(settings.py)
8、运行爬虫 ：scrapy crawl 爬虫名
```

- pycharm运行爬虫项目

```python
1、创建begin.py(和scrapy.cfg文件同目录)
2、begin.py中内容：
	from scrapy import cmdline
	cmdline.execute('scrapy crawl maoyan'.split())
```

## **小试牛刀**

- 目标

```python
打开百度首页，把 '百度一下，你就知道' 抓取下来，从终端输出
xpath表达式: '/html/head/title/text()'
```

- 实现步骤

1. **创建项目Baidu 和 爬虫文件baidu**

```python
1、scrapy startproject Baidu
2、cd Baidu
3、scrapy genspider baidu www.baidu.com
```

2. **编写爬虫文件baidu.py，xpath提取数据**

```python
# -*- coding: utf-8 -*-
import scrapy

class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        result = response.xpath('/html/head/title/text()').extract_first()
        print('*'*50)
        print(result)
        print('*'*50)

```

3. **全局配置settings.py**

```python
USER_AGENT = 'Mozilla/5.0'
ROBOTSTXT_OBEY = False
DEFAULT_REQUEST_HEADERS = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language': 'en',
}
ITEM_PIPELINES = {
    '项目目录名.pipelines.类名':300,
}
```

4. **创建begin.py（和scrapy.cfg同目录）**

```python
from scrapy import cmdline

cmdline.execute('scrapy crawl baidu'.split())
```

5. **启动爬虫**

```
直接运行 begin.py 文件即可
```

**思考运行过程**



## **猫眼电影案例**

- 目标

```python
URL: 百度搜索 -> 猫眼电影 -> 榜单 -> top100榜
     https://maoyan.com/board/4?offset=???
内容: 电影名称、电影主演、上映时间
```

- 实现步骤

1. **创建项目和爬虫文件**

```python
# 创建爬虫项目
scrapy startproject Maoyan
# 创建爬虫文件
cd Maoyan
scrapy genspider maoyan maoyan.com
```

2. **定义要爬取的数据结构（items.py）**

```python
name = scrapy.Field()
star = scrapy.Field()
time = scrapy.Field()
```

3. **编写爬虫文件（maoyan.py）**

```python
1、基准xpath,匹配每个电影信息节点对象列表
	dd_list = response.xpath('//dl[@class="board-wrapper"]/dd')
2、for dd in dd_list:
	电影名称 = dd.xpath('./a/@title')
	电影主演 = dd.xpath('.//p[@class="star"]/text()')
	上映时间 = dd.xpath('.//p[@class="releasetime"]/text()')
```

   代码实现一

```python
from ..items import MaoyanItem

def parse(self,response):
    # 基准xpath
    dd_list = response.xpath('xxxx')
    for dd in dd_list:
        item = MaoyanItem()
        item['name'] = dd.xpath('xxx').extract_first()
        item['star'] = dd.xpath('xxx').extract_first()
        item['time'] = dd.xpath('xxx').extract_first()
        # 把 item 交给管道文件的 process_item() 处理
        yield item
```

   代码实现二

```python

```

   代码实现三

```python
# 重写scrapy.Spider类的 start_requests()方法
```

3. **定义管道文件（pipelines.py）**

```python
def process_item(self,item,spider):
    xxxx xxxx 
    return item
```

5. **全局配置文件（settings.py）**

```python
ITEM_PIPELINES = {
    'Maoyan.pipelines.MaoyanPipeline':300
}
```

6. **创建并运行文件（begin.py）**

```python
from scrapy import cmdline
cmdline.execute('scrapy crawl maoyan'.split())
```

## **知识点汇总**

- 节点对象.xpath('')

```pythpn
1、列表,元素为选择器 [<selector data='A'>]
2、列表.extract() ：序列化列表中所有选择器为Unicode字符串 ['A','B','C']
3、列表.extract_first() 或者 get() :获取列表中第1个序列化的元素(字符串) : 'A'
```

- pipelines.py中必须有1个函数叫process_item

```python
def process_item(self,item,spider):
	return item ( * 此处必须返回item,把item数据提供给下一个管道去使用)
```

- 日志变量及日志级别(settings.py)

```python
# 日志相关变量
LOG_LEVEL = ''
LOG_FILE = '文件名.log'

# 日志级别
5 CRITICAL ：严重错误
4 ERROR    ：普通错误
3 WARNING  ：警告
2 INFO     ：一般信息
1 DEBUG    ：调试信息
# 注意: 只显示当前级别的日志和比当前级别日志更严重的
```

- 管道文件使用

```python
1、在爬虫文件中为items.py中类做实例化，用爬下来的数据给对象赋值
	from ..items import MaoyanItem
	item = MaoyanItem()
2、管道文件（pipelines.py）
3、开启管道（settings.py）
	ITEM_PIPELINES = { '项目目录名.pipelines.类名':优先级 }
```

## **数据持久化存储(MongoDB和MySQL)**

### **实现步骤**

```python
1、在setting.py中定义相关变量
2、pipelines.py中导入settings模块
  from .settings import *
  class MaoyanMongoPipeline(object):
	  def open_spider(self,spider):
		  # 爬虫开始执行1次,用于数据库连接
      def process_item(self,item,spider):
          ... ...
          return item
	  def close_spider(self,spider):
		  # 爬虫结束时执行1次,用于断开数据库连接
3、settings.py中添加此管道
	ITEM_PIPELINES = {'':200}

# 注意 ：process_item() 函数中一定要 return item ***
```

## **保存为csv、json文件**

- 命令格式

```python
scrapy crawl maoyan -o maoyan.csv
scrapy crawl maoyan -o maoyan.json
# 设置导出编码(settings.py)
FEED_EXPORT_ENCODING = 'utf-8'
```

## **盗墓笔记小说抓取案例（三级页面）**

-   目标

```python
# 抓取目标网站中盗墓笔记1-8中所有章节的所有小说的具体内容，保存到本地文件
1、网址 ：http://www.daomubiji.com/
```

- 准备工作xpath

```python
1、一级页面xpath（此处响应做了处理）：//ul[@class="sub-menu"]/li/a/@href
2、二级页面xpath：/html/body/section/div[2]/div/article
  基准xpath ：//article
3、三级页面xpath：
小说内容 = '\n'.join(response.xpath('//article[@class="article-content"]//p/text()').extract())
# ['段落1','段落2','段落3']
```

- 项目实现

1. **创建项目及爬虫文件**

```python
创建项目 ：Daomu
创建爬虫 ：daomu  www.daomubiji.com
```

2. 定义要爬取的数据结构（把数据交给管道）

```python
import scrapy

class DaomuItem(scrapy.Item):
    # 卷名
    juan_name = scrapy.Field()
    # 章节数
    zh_num = scrapy.Field()
    # 章节名
    zh_name = scrapy.Field()
    # 章节链接
    zh_link = scrapy.Field()
    # 小说内容
    zh_content = scrapy.Field()
```

3. **爬虫文件实现数据抓取**

```python

```

4. **管道文件实现数据处理**

   

```python

```

## **图片管道(360图片抓取案例)**

- 目标 

```python
www.so.com -> 图片 -> 美女
```

- 抓取网络数据包

```python
2、F12抓包,抓取到json地址 和 查询参数(QueryString)
      url = images.format(str(sn))
      ch: beauty
      sn: 90
      listtype: new
      temp: 1
```

- 项目实现

1. 创建爬虫项目和爬虫文件

   ```
   
   ```

2. 定义要爬取的数据结构

```

```

3. 爬虫文件实现图片链接抓取

```python

```

4. **管道文件（pipelines.py）**

```python

```

5. **设置settings.py**

   ```
   
   ```

6. **创建bigin.py运行爬虫**

   ```
   
   ```

## **今日作业**

```python
1、把今天内容过一遍
2、Daomu错误调一下(看规律,做条件判断)
3、腾讯招聘尝试改写为scrapy（重写start_requests()方法）
  # response.text ：获取页面响应内容
```















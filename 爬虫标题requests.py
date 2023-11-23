#coding:utf-8
'''
爬虫：爬取文档标题等格式统一的文本内容
'''

import requests          #HTTP请求库
from lxml import html    #处理html代码

url = 'https://qiwsir.github.io/' #需要爬的网址

page = requests.get(url).content.decode('utf-8')  #获取网页内容部分，用utf-8编码显示中文

sel = html.fromstring(page)    #获取的page转换成html
title = sel.xpath('//article/h2/a/text()')   #使用xpath方法从标签固定位置挑选内容
print(title)
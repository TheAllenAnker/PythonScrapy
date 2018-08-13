# Author: Allen Anker
# Created by Allen Anker on 13/08/2018
from lxml import etree
text = '''
<div>
<ul>
<li class="item-0"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>
</ul>
</div>
'''
html = etree.HTML(text)
result = etree.tostring(html)
print(result.decode('utf-8'))
print('===================')

html = etree.parse('./test.html', etree.HTMLParser())
result = etree.tostring(html)
print(result.decode('utf-8'))
print('====================')

result = html.xpath('//*')
print(result)
print('====================')

result = html.xpath('//li')
print(result)
print(result[0])
print('====================')

result = html.xpath('//li/a')
print(result)
print('====================')

result = html.xpath('//ul//a')
print(result)
print('====================')

result = html.xpath('//a[@href="link4.html"]/../@class')
print(result)
print('====================')

result = html.xpath('//a[@href="link4.html"]/parent::*/@class')
print(result)
print('====================')

result = html.xpath('//li[@class="item-0"]//text()')
print(result)
result = html.xpath('//li/a/@href')
print(result)
print('====================')

result = html.xpath('//li[1]/a/text()')
print(result)
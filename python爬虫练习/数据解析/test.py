import requests
from lxml import etree

url = 'http://www.shicimingju.com/book/sanguoyanyi/1.html'
data = requests.get(url=url).text
tree = etree.HTML(data)
data_list = tree.xpath('//p//text()')
print(type(data_list[0]))
a = str(data_list[0])
print(type(a))
print(data_list)
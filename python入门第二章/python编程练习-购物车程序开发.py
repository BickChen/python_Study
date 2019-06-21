# -*- coding:utf-8 -*-

"""
实现功能要求：
1、启动程序后，让用户输入工资，然后进入循环，打印商品列表和编号

2、允许用户根据商品编号选择商品

3、用户选择商品后，检测余额是否够，够就直接扣款，并加入购物车， 不够就提醒余额不足

4、可随时退出，退出时，打印已购买商品和余额
"""

goods = [
{"name": "电脑", "price": 1999},
{"name": "鼠标", "price": 10},
{"name": "游艇", "price": 20},
{"name": "美女", "price": 998},
]
goods_01 = []
wages = input("请输入您的工资:").strip()
if wages.isdigit():
    wages = int(wages)
for i in goods:
    print("编号：%d 商品名称: %s 商品价格： %d"%(goods.index(i),i["name"],i["price"]))

while True:
    number = input("请输入你要购买的商品编号:").strip()
    if number.isdigit():
        number = int(number)
    else:
        print("没有这个商品编号！")
        continue
    if goods[number]["price"] <= wages:
        wages = wages - goods[number]["price"]
        goods_01.append(goods[number])
        print("恭喜您，购买成功！")
    else:
        print("您的余额已不足")
    determine = input("您是否要退出 Y/N:")
    if determine is "Y" or determine is "y":
        break
    else:
        continue
for i in goods_01:
    print("您购买了%s，价格：%d元"%(i["name"],i["price"]))
print("您剩余%s元"%(wages))
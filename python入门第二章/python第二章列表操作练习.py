# -*- coding:utf-8 -*-
"""
针对列表names=['金角大王', '黑姑娘', 'rain', 'eva', '狗蛋', '银角大王', 'eva','鸡头']进入以下操作
1.通过names.index()的方法返回第2个eva的索引值
2.把以上的列表通过切片的形式实现反转
3.打印列表中所有下标为奇数的值
4.通过names.index()方法找到第2个eva值 ，并将其改成EVA
"""
names=['金角大王', '黑姑娘', 'rain', 'eva', '狗蛋', '银角大王', 'eva','鸡头']
#1.通过names.index()的方法返回第2个eva的索引值
names_01 = names[:names.index("eva")+1]
names_02 = names[names.index("eva")+1:]
print(len(names_01)+names_02.index("eva"))

#2.把以上的列表通过切片的形式实现反转
print(names[::-1])

#3.打印列表中所有下标为奇数的值
print(names[1::2])

#4.通过names.index()方法找到第2个eva值 ，并将其改成EVA
names_01 = names[:names.index("eva")+1]
names_02 = names[names.index("eva")+1:]
number = len(names_01)+names_02.index("eva")
names[number] = "EVA"
print(names)
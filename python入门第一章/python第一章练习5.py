# -*- coding:utf-8 -*-

"""
使用while,完成以下图形的输出:
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""

second = 1
a = 9
"""
改进思路：
    1.把a行数变量更改为用户输入
    2.判断a行数变量是否为奇数
    3.如为奇数取a行数中间值为if判断条件：a <= a的中间值
"""
while a != 0:
    print("* " * second)
    if a <= 5:
        second -=1
    elif a > 5:
        second +=1
    a -=1

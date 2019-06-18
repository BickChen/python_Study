# -*- coding:utf-8 -*-

"""
a. 使用 while 循环实现输出 1,2,3,4,5, 7,8,9, 11,12
b. 使用while 循环输出100-50，从大到小，如100，99，98…，到50时再从0循环输出到50，然后结束
c. 使用 while 循环实现输出 1-100 内的所有奇数
d. 使用 while 循环实现输出 1-100 内的所有偶数
e. 使用while循环实现输出2-3+4-5+6…+100 的和
"""
#a.使用 while 循环实现输出 1,2,3,4,5, 7,8,9, 11,12
"""
number = 1
while number != 13:
    if number == 6:
        pass
    elif number == 10:
        pass
    else:
        print(number)
    number +=1
    
"""
#另一种写法
"""
for i in range(1,13):
    if i == 6:
        pass
    elif i == 10:
        pass
    else:
        print(i)
"""

#b.使用while 循环输出100-50，从大到小，如100，99，98…，到50时再从0循环输出到50，然后结束
"""
number_1 = 100
number_2 = 0
while True:
    if number_1 >= 50 :
        print(number_1)
        number_1 -=1
    else:
        if number_2 <= 50:
            print(number_2)
            number_2 +=1
        else:
            break
"""

#c.使用 while 循环实现输出 1-100 内的所有奇数
"""
number = 0
while number != 101:
    number +=1
    if number%2 == 1:
        print(number)
    elif number == 100:
        break
"""

#d.使用 while 循环实现输出 1-100 内的所有偶数
"""
number = 0
while number != 101:
    number +=1
    if number%2 == 0:
        print(number)
    elif number == 100:
        break
"""

#e. 使用while循环实现输出2-3+4-5+6…+100 的和
number = 2
all_and = 0

while number <= 100:
    if number % 2 == 0:
        all_and += number
    elif number % 2 == 1:
        all_and -= number
    number += 1

print("输出和为：%s." % all_and)
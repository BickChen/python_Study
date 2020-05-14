"""
a. 使用 while 循环实现输出 1,2,3,4,5, 7,8,9, 11,12
"""

# a = 1
# while a <= 12:
#     if a == 6 or a == 10:
#         a +=1
#         continue
#     print(a)
#     a +=1

# for i in range(1, 13):
#     if i == 6 or i == 10:
#         pass
#     else:
#         print(i)

# 最优方案
# a = 1
# while a <= 12:
#     print(a)
#     a +=2 if a == 5 or a == 9 else 1

"""
使用while 循环输出100-50，从大到小，如100，99，98…，到50时再从0循环输出到50，然后结束
"""

# counts = 100
# counts_2 = 0
#
# while counts >= 50:
#     print(counts)
#     counts -=1
# while counts_2 <= 50:
#     print(counts_2)
#     counts_2 += 1

# 最优解
# counts = 100
# while counts > -2:
#     if counts >= 50:
#         print(counts)
#     else:
#         print(49 - counts)
#     counts -=1

"""
使用 while 循环实现输出 1-100 内的所有奇数
使用 while 循环实现输出 1-100 内的所有偶数
"""

# 奇数显示最优解
# counts = 1
# while counts <= 100:
#     print(counts)
#     counts +=2 if counts%2 != 0 else 1

# 偶数显示最优解
# counts = 2
# while counts <= 100:
#     print(counts)
#     counts += 2 if counts % 2 == 0 else 1

"""
使用while循环实现输出2-3+4-5+6…+100 的和
"""

# 最优解
# counts = 2
# age = 0
# while counts <= 100:
#     age +=counts if counts%2 == 0 else -counts
#     counts += 1
# print(age)


"""
输入一年份，判断该年份是否是闰年并输出结果
"""

# age = input("请输入一个年份：")
# if age.isdigit():
#     age = int(age)
#     if (age % 4 == 0 and age % 100 != 0) or age % 400 == 0:
#         print("您输入的是一个闰年")
#     else:
#         print("您输入的是一个平年")
# else:
#     print("您输入的不是一个年份！")

"""
假设一年期定期利率为3.25%，计算一下需要过多少年，一万元的一年定期存款连本带息能翻番？
"""

# money = 10000
# target = 20000
# age = 0
# while money < target:
#     money = money + money * 0.12
#     age +=1
# print("第%d年，10000元可以变成%d元"%(age, money))

"""
使用while,完成以下图形的输出
"""

# a = input("请输入一个数字：")
# b = 1
# if a.isdigit():
#     a = int(a)
#     n = a * 2 -1
#     while n != 0:
#         print("*" * b)
#         b += 1 if n > a else -1
#         n -=1
# else:
#     print("你输入的不是一个数字！")






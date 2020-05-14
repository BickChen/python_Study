# a = 2
# b = 2.22
# c = '小猿圈'
#
# print(type(a))
# print(type(b))
# print(type(c))

"""
写代码
实现用户输入用户名和密码,当用户名为 seven 且 密码为 123 时,显示登陆成功,否则登陆失败!
实现用户输入用户名和密码,当用户名为 seven 且 密码为 123 时,显示登陆成功,否则登陆失败,失败时允许重复输入三次
实现用户输入用户名和密码,当用户名为 seven 或 alex 且 密码为 123 时,显示登陆成功,否则登陆失败,失败时允许重复输入三次
"""

# name1 = 'seven'
# name2 = 'alex'
# passwd = '123'
# input_times = 1
# while True:
#     name = str(input("请输入用户名："))
#     name_passwd = str(input("请输入用户密码："))
#     if (name == name1 or name == name2) and name_passwd == passwd:
#         print("登陆成功！")
#         break
#     elif input_times >= 3:
#         print("您的用户已锁定！")
#         break
#     else:
#         input_times +=1
#         times = str(3-input_times+1)
#         print("用户名密码错误，请重新输入,剩余输入次数%s"%times)
#         continue

"""
写代码
a. 使用 while 循环实现输出 1,2,3,4,5, 7,8,9, 11,12
b. 使用while 循环输出100-50，从大到小，如100，99，98…，到50时再从0循环输出到50，然后结束
c. 使用 while 循环实现输出 1-100 内的所有奇数
d. 使用 while 循环实现输出 1-100 内的所有偶数
e. 使用while循环实现输出2-3+4-5+6…+100 的和
"""

# times = 1
#
# while True:
#     if times == 6 or times == 10:
#         times +=1
#         continue
#     elif times >= 12:
#         break
#     else:
#         print(times)
#         times +=1


# times_1 = 100
# times_2 = 0
# while True:
#     if times_1 >= 50:
#         print(times_1)
#         times_1 -=1
#     elif times_1 == 49 and times_2 <= 50:
#         print(times_2)
#         times_2 +=1
#     else:
#         break

# times = 1
# while True:
#     times += 1
#     if times % 2 == 1:
#         continue
#     elif times >= 101:
#         break
#     else:
#         print(times)

# times = 2
# age = 0
# while True:
#     if times > 100:
#         break
#     elif times % 2 == 0:
#         age +=times
#     elif times % 2 ==1:
#         age -=times
#     times +=1
# print(age)

"""
等待用户输入名字、地点、爱好，根据用户的名字和爱好进行任意显示
"""

# name = str(input("name: "))
# place = str(input("Place: "))
# hobby = str(input("Hobby: "))
#
# print("""敬爱可爱的%s
# 最喜欢的城市是：%s
# 爱好是：%s"""%(name, place, hobby))

# date = int(input("请输入一个年份："))
#
# if date % 4 == 0 and date % 100 != 1:
#     print("%d 是一个闰年"%date)
# elif date % 400 == 0:
#     print("%d 是一个闰年"%date)
# else:
#     print("%d 不是一个闰年"%date)

"""
假设一年期定期利率为3.25%，计算一下需要过多少年，一万元的一年定期存款连本带息能翻番？
"""

# money = 10000
# year = 0
# while True:
#     money_data = money
#     money *=0.0325
#     money +=money_data
#     year +=1
#     if money >= 20000:
#         print("10000元，定期存%d年可以升值到%d元"%(year, money))
#         break

# a = 1
# b = 9
#
# while b != 0:
#     print(" * " * a)
#     if b > 5:
#         a +=1
#     else:
#         a -=1
#     b -=1

# data = 100
# data_bak = data
# data_times = 10
# while data_times != 0:
#     data = data // 2
#     data_bak +=data
#     data_times -=1
#
# print("共经过了%d米"%data_bak)


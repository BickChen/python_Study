"""
1、简述编译型与解释型语言的区别，且分别列出你知道的哪些语言属于编译型，哪些属于解释型。
编译型语言：代码可以编译为二进制文件，编译后无需在服务器上安装环境可直接运行，例如：C、C++、C#
解释型语言：代码不能编译为二进制文件，如需运行代码要安装配置相应的解释器环境，例如：python

2、python单行注释为#号，多行注释为三引号。

3、布尔值有True和False, 代表结果为真或假。

4、声明变量应注意变量名称和python内置的函数名重复，变量名称应有意义，变量名称不应该存在空格。

5、id(变量名)可查看内存中变量的地址

6、and 代表条件全部满足才能执行下面代码块的代码
   or  代表条件满足一个即可执行下面代码块的代码
   not 代表条件不成立才能执行下面代码块的代码

7、查看变量类型的代码为type(变量名)

"""

# name = 'alex'
# print(id(name))

# username = input("username: ")
# password = input("password: ")
# if username == 'seven' and password == '123':
#     print('登陆成功')
# else:
#     print('没有此用户！')

# num = 0
# while num < 3:
#     username = input("username: ")
#     password = input("password: ")
#     if (username == "seven" or username == 'alex') and password == '123':
#         print('登陆成功')
#         break
#     else:
#         print('用户名或密码不对，请重新输入！')
#     num += 1

# num = 0
# while num < 12:
#     num += 1
#     if num == 6 or num == 10:
#         continue
#     else:
#         print(num)

# num = 100
# while True:
#     num -= 1
#     if num == 50:
#         print(num)
#         num -= 50
#         while num <= 50:
#             print(num)
#             num += 1
#         break
#     else:
#         print(num)

# num = 100
# while num != 0:
#     if num % 2 != 1:
#         print(num)
#     num -=1

# num = 2
# a = 0
# while num <= 100:
#     if num % 2 != 1:
#         a +=num
#     else:
#         a -=num
#     num +=1
# print(a)

# n1 = 123
# n2 = n1
# n1 = 333
# print(n1, n2)

"""
n2 指向的是123这个值在内存中的地址
"""

# year = int(input("year: "))
# if (year % 4 == 0 and year % 100 != 1) or year % 400 == 0:
#     print("您输入的是一个闰年！")
# else:
#     print("您输入的是一个平年！")

# money = 10000
# target = money * 2
# year = 0
# while money <= target:
#     interest = money * 0.0325
#     year += 1
#     print("第%d年的利息为：%d"%(year, interest))
#     money += interest
#     print("第%d年，本金变成：%d"%(year, money))

input_num = 9
num_1 = input_num // 2 + 1
num_2 = 1
while num_1 > 0:
    if input_num != num_1:
        print('*' * num_2)
        num_2 +=1
        input_num -=1
    else:
        print('*' * num_1)
        num_1 -=1
        input_num -=1

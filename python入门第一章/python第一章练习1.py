# -*- coding:utf-8 -*-

"""
实现用户输入用户名和密码,当用户名为 seven 或 alex 且 密码为 123 时,显示登陆成功,否则登陆失败,失败时允许重复输入三次
"""

import sys
user_name = "seven"
user_name1 = "alex"
user_passwd = "123"
i = 0
while i < 3 :
    name = input("请输入用户名：")
    if name == user_name or name == user_name1:
        j = 0
        while j < 3:
            passwd = input("请输入密码：")
            if user_passwd == passwd:
                print("登录成功")
                sys.exit(0)
            else:
                size = 3 - j
                print("登录失败,剩余次数%s"%(size -1))
            j +=1
        else:
            sys.exit(0)
    else:
        sice = 3 - i
        print("用户名错误，剩余次数%s"%(sice -1))
        i +=1
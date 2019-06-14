# -*- coding:utf-8 -*-

import sys

i = 0
while i < 3:
    name = input("请输入用户名：")

    lock_file = open('account_lock','r+')
    lock_list = lock_file.readlines()
    for lock_line in lock_list:
        lock_line = lock_line.strip('\n')
        if name == lock_line:
            sys.exit("您的用户%s 已被锁定，退出"%(name))

    name_file = open('accout','r')
    name_list = name_file.readlines()

    for name_line in name_list:
        (user,passwd) = name_line.strip('\n').split()
        if name == user:
            j = 0
            while j < 3:
                name_passwd = input("请输入密码：")
                if name_passwd == passwd:
                    sys.exit('您的账号%s 已成功登录'%(name))
                elif j != 2:
                    print("用户 %s 密码错误，请重新输入，还有 %d 次机会" % (name, 3 - j))
                j +=1
            else:
                lock_file.write(name + '\n')
                print("您的用户%s 密码输入错误次数已超过3次被锁定"%(name))
                sys.exit(0)
    else:
        if i != 2:
            print('用户名%s 不存在，请重新输入，还有 %d 次机会' % (name, 3 - i))
    i += 1
else:
    sys.exit("用户 %s 不存在,退出" % (name))

lock_file.close()
user_file.close()
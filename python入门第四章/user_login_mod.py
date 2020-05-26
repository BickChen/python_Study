"""
写一个用户登录验证程序，文件名account.json，内容如下
{“expire_date”: “2021-01-01”, “id”: 1234, “status”: 0, “pay_day”: 22, “password”: “abc”}
根据用户输入的用户名&密码，找到对应的json文件，把数据加载出来进行验证
用户名为json文件名，密码为 password。
判断是否过期，与expire_date进行对比。
登陆成功后，打印“登陆成功”，三次登陆失败，status值改为1，并且锁定账号。
"""

import json, time, modular_mod

# 生成用户数据文件
# name_data = {"expire_date": "2021-01-01", "id": 1234, "status": 0, "pay_day": 22, "password": "abc"}
# file = open('user_data/Yasin', 'w')
# json.dump(name_data, file)


user_data = modular_mod.file_info('payment/user_data')
frequency = 1
while True:

    user_name = input("请输入用户名：")
    user_passwd = input("请输入密码：")

    if user_name in user_data:
        file = open(user_data[user_name])
        user_info = json.load(file)
        file.close()
        if user_info['status'] == 0:
            if time.time() < time.mktime(time.strptime(user_info['expire_date'], "%Y-%m-%d")):
                if user_passwd == user_info['password']:
                    print('登陆成功')
                    break
                else:
                    if frequency == 3:
                        user_info['status'] = 1
                        file = open(user_data[user_name],'w')
                        json.dump(user_info, file)
                        file.close()
                        print("密码错误3次，用户已锁定")
                        break
                    frequency +=1
                    print(frequency)
                    continue
            else:
                print('您的密码已过期')
                break
        else:
            print("您的用户已锁定")
            break
    else:
        print("用户不存在")
        break
import json, hashlib, modular_mod, time
print('成功')
#user_data = modular_mod.file_info('user_data')

"""
加密用户文件密码
"""
# for i in user_data:
#     file = open(user_data[i])
#     user_info = json.load(file)
#     file.close()
#     md5_mod = hashlib.md5(user_info["password"].encode("utf-8"))
#     user_info["password"] = md5_mod.hexdigest()
#     file = open(user_data[i], 'w')
#     json.dump(user_info, file)
# print(user_data)
def user_verification(funck):
    def inner():
        user_data = modular_mod.file_info('D:\\python_Study\\python入门第四章\\user_data')
        frequency = 1
        while frequency < 4:
            user_name = input("请输入用户名：")
            user_passwd = input("请输入密码：")

            if user_name in user_data:
                file = open(user_data[user_name])
                user_info = json.load(file)
                file.close()
                if user_info['status'] == 0:
                    if time.time() < time.mktime(time.strptime(user_info['expire_date'], "%Y-%m-%d")):
                        user_passwd = hashlib.md5(user_passwd.encode('utf-8'))
                        user_passwd = user_passwd.hexdigest()
                        if user_passwd == user_info['password']:
                            print('登陆成功')
                            frequency += 4
                            return funck()
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
    return inner
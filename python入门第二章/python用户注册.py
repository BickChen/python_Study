name = input("用户名：")
name = name + '\n'
name_passwd = str(input("密码："))
name_passwd = name_passwd + '\n'
name_file = "用户登录账号.txt"
name_open_file = open(name_file,'a+')
name_open_file.write(name)
name_open_file.writelines(name_passwd)

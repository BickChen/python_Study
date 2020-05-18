
old_file = 'username'
new_file = 'locking'
frequency = 0
while frequency < 3:
    user = input("USER: ")
    passwd = input("PASSWD: ")
    frequency +=1
    f = open(old_file, 'r', encoding='UTF-8')
    f_new = open(new_file, 'r', encoding='UTF-8')
    for line in f_new:
        line = line.strip()
        if line == user:
            print('您的账号已锁定！')
            frequency +=4
            break
    f_new.seek(0)
    f_new.close()

    if frequency > 3:
        break

    for line in f:
        line = line.split()
        if line[0] == user and line[1] == passwd:
            print('登陆成功')
            frequency +=4
            break
    f.seek(0)
    f.close()
    if frequency > 3:
        break


    if frequency < 3:
        print("您输入的用户名密码不对！您还有%d次机会"%(3-frequency))
        continue
    else:
        print("您的账户已锁定！")
        f_new = open(new_file, 'a')
        f_new.write(user+'\n')
        f_new.close()


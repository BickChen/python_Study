

while True:
    gules = 0
    blue = 0
    list01 = []
    while gules < 6:
        n = int(input("\033[4;31;0mselect red ball:\033[0m"))
        age_n = n in list01
        if age_n == True:
            print("你输入的数字重复了！")
            continue
        else:
            if n >= 1 and n < 33:
                list01.append(n)
                gules += 1
            else:
                print("你输入的数字已超过可用范围1-32！")
                continue
    while blue < 2:
        n = int(input("\033[4;34;0mselect red ball:\033[0m"))
        age_n = n in list01
        if age_n == True:
            print("你输入的数字重复了！")
            continue
        else:
            if n >= 1 and n < 33:
                list01.append(n)
                blue += 1
            else:
                print("你输入的数字已超过可用范围1-32！")
                continue
    print(list01)
    break
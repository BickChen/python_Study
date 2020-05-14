
list_01 = []
frequency = 0
while True:
    if len(list_01) < 6:
        n = input("\033[1;31m请输入红色球号码:\033[0m").strip()
        if type(n) != int:
            n = int(n)
        determine = n in list_01
        if determine == True:
            print("您输入的数字重复了，请重新输入！")
            continue
        elif n >= 1 and n < 33:
            list_01.append(n)
            continue
        else:
            print("只能输入1-32范围内的值，请重新输入！")
            continue
    elif len(list_01) >= 8:
        break
    else:
        n = input("\033[1;34m请输入蓝色球号码:\033[0m").strip()
        if type(n) != int:
            n = int(n)
        determine = n in list_01
        if determine == True:
            print("您输入的数字重复了，请重新输入！")
            continue
        elif n >= 1 and n < 33:
            list_01.append(n)
            continue
        else:
            print("只能输入1-32范围内的值，请重新输入！")
            continue
print(list_01)




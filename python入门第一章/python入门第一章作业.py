# -*- coding:utf-8 -*-

"""
先让用户依次选择6个红球，再选择2个蓝球，最后统一打印用户选择的球号。

确保用户不能选择重复的，选择的数不能超出范围。备注：数字范围为1-32
"""

"""
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
        n = int(input("\033[4;34;0mselect blue ball:\033[0m"))
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
"""

"""以下为根据李露老师建议优化"""

list_01 = []
while True:
    if len(list_01) < 6:
        n = input("\033[4;31;0mselect red ball:\033[0m").strip()
        if n.isdigit():
            n = int(n)
        determine = n in list_01
        if determine == True:
            print("你输入的数字重复了！")
            continue
        if n >= 1 and n < 33:
            list_01.append(n)
        else:
            print("你输入的数字已超过可用范围1-32！")
            continue
    elif len(list_01) == 8:
            break
    else:
        n = input("\033[4;34;0mselect blue ball:\033[0m").strip()
        if n.isdigit():
            n = int(n)
        determine = n in list_01
        if determine == True:
            print("你输入的数字重复了！")
            continue
        if n >= 1 and n < 33:
            list_01.append(n)
        else:
            print("你输入的数字已超过可用范围1-32！")
            continue
print(list_01)
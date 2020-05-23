"""
写一个摇骰子游戏，要求用户压大小，赔率一赔一。
要求：三个骰子，每个骰子的值从1-6，摇大小，每次打印摇出来3个骰子的值。

"""

import random

def recharge(old_chip):
    chip = input("请充值筹码>>>：")
    if chip.isdigit() and int(chip) != 0:
        chip = int(chip)
        chip = old_chip + chip
        return chip
    else:
        print("您输入的不是一个正确的数字！")

def win(dice,old_chip,user_info_chip,value):
    print("骰子为：%d %d %d 总数为：%d  %s" % (dice[0], dice[1], dice[2], sum(dice), value))
    print("恭喜您赢了")
    old_chip += user_info_chip
    print("您的筹码现在为：%d" % old_chip)
    return old_chip

def transport(dice,old_chip,user_info_chip,value):
    print("骰子为：%d %d %d 总数为：%d  %s" % (dice[0], dice[1], dice[2], sum(dice), value))
    print("很遗憾你输了")
    old_chip -= user_info_chip
    print("您的筹码现在为：%d" % old_chip)
    return old_chip

old_chip = 0
old_chip = recharge(old_chip)
frequency = 1
while old_chip != 0:
    dice = list((random.randint(1, 6) for i in range(3)))
    user_info = input("第%d轮游戏开始，请输入您要压那边（大/小）："%frequency)
    user_info_chip = input("请输入您压多少筹码：")
    if user_info_chip.isdigit() and int(user_info_chip) <= old_chip:
        user_info_chip = int(user_info_chip)
        if user_info == "大":
            if sum(dice) > 9:
                old_chip = win(dice,old_chip,user_info_chip,'大')
            else:
                old_chip = transport(dice,old_chip,user_info_chip,'小')
        elif user_info == '小':
            if sum(dice) < 9:
                old_chip = win(dice, old_chip, user_info_chip,'小')
            else:
                old_chip = transport(dice, old_chip, user_info_chip, '大')
        else:
            print("您输入的不是一个正常的值，此轮游戏将不接受您的筹码")
    else:
        print("你个傻逼，你没有这么多的筹码")
    if old_chip == 0:
        old_chip = recharge(old_chip)
        print("充值成功，您现在的筹码为：%d"%old_chip)
    frequency +=1




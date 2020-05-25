"""
请用代码实现：利用下划线将列表的每一个元素拼接成字符串，li＝["alex", "eric", "rain"]
"""

# li = ['alex', 'eric', 'rain']
# name_test = ""
# for i in li:
#     name = i + '_'
#     name_test +=name
# name_test = name_test[:-1]
# print(name_test)

"""
查找列表中元素，移除每个元素的空格，并查找以a或A开头并且以c结尾的所有元素
"""

#li = ["alec", " aric", "Alex", "Tony", "rain"]
#tu = ("alec", " aric", "Alex", "Tony", "rain")
#dic = {'k1': "alex", 'k2': ' aric', "k3": "Alex", "k4": "Tony"}

#查找列表的值
# for i in li:
#     i = i.strip()
#     if (i[0] == 'A' or i[0] == 'a') and i[-1] == 'c':
#         print(i)

#查找元组的值
# list_test = []
# for i in tu:
#     i = i.strip()
#     list_test.append(i)
#     if (i[0] == 'A' or i[0] == 'a') and i[-1] == 'c':
#         print(i)
# tu = set(list_test)
# print(tu)

#查找字典的值
# for i in dic:
#     v = dic[i]
#     v = v.strip()
#     if (v[0] == 'A' or v[0] == 'a') and v[-1] == 'c':
#         print(v)
#     dic[i] = v

"""
写代码，有如下列表，按照要求实现每一个功能
"""

# li = ["alec", "eric", "Tony", "rain"]

# #计算列表长度并输出
# print(len(li))
#
# #列表中追加元素"seven"，并输出添加后的列表
# li.append("seven")
# print(li)
#
# #请在列表的第1个位置插入元素"Tony"，并输出添加后的列表
#
# li.insert(0, "Tony")
# print(li)
#
# #请修改列表第2个位置的元素为"Kelly"，并输出修改后的列表
#
# li.insert(1, "Kelly")
# print(li)
#
# #请删除列表中的元素"eric"，并输出修改后的列表
#
# li.remove("eric")
# print(li)
#
# #请删除列表中的第2个元素，并输出删除的元素的值和删除元素后的列表
#
# name = li.pop(1)
# print(name)
# print(li)
#
# #请删除列表中的第3个元素，并输出删除元素后的列表
#
# li.pop(2)
# print(li)
#
# #请删除列表中的第2至4个元素，并输出删除元素后的列表
#
# li_bak = li[1:4]
# for i in li_bak:
#     li.remove(i)
# print(li)

#请将列表所有的元素反转，并输出反转后的列表

# li.reverse()
# print(li)
# li = li[::-1]
# print(li)
#
# 请使用for、len、range输出列表的索引
# for i in range(len(li)):
#     print(i, li[i])

# #请使用enumrate输出列表元素和序号（序号从100开始）
#
# for index, val in enumerate(li):
#     print(val, index)
#
# #请使用for循环输出列表的所有元素
#
# for i in li:
#     print(i)

"""
写代码，有如下列表，按照要求实现每一个功能
"""

# li = ["hello", 'seven', ["mon", ["h", "kelly"], 'all'], 123, 446]
#
# #请根据索引输出"Kelly"
#
# print(li[2][1][1])
#
# #请使用索引找到"all"元素并将其修改为"ALL"，如：li[0][1][9]…
# print(li[2][2])
# li[2][2] = 'ALL'
# print(li[2][2])

"""
有如下变量，请实现要求的功能
"""

# tu = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11,22,33)}, 44])

# 元组数据类型每个元素不可更改，它保存的是每个元素的内存地址
# 第一个元素"alex"不可修改，因为该元素为字符串，字符串为不可变类型
# tu变量中K2 对应的值是列表类型，可以被修改

# tu[1][2]["k2"].append("Seven")
# print(tu)

# tu变量中k3对应的是元组数据类型，不可变

"""
6、转换
将字符串s = "alex"转换成列表
将字符串s = "alex"转换成元祖
将列表li = ["alex", "seven"]转换成元组
将元组tu = ("Alex", "seven")转换成列表
将列表li = ["alex", "seven"]转换成字典且字典的key按照10开始向后递增
"""

# s = "alex"
# s = list(s)
# print(s)
#
# s = "alex"
# s = tuple(s)
# print(s)
#
# li = ["alex", 'seven']
# li = tuple(li)
# print(li)
#
# tu = li
# tu = list(tu)
# print(tu)

# li = ['alex', 'seven']
# li = {}.fromkeys(range(10,20),li)
# print(li)

"""
有如下值集合[11,22,33,44,55,66,77,88,99,90]，将所有大于66的值保存至字典的第一个key中，将小于66的值保存至第二个key的值中。
"""
#
# li = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
# dic = {'k1':[], 'k2':[]}
# for i in li:
#     if i > 66:
#         dic['k1'].append(i)
#     elif i < 66:
#         dic['k2'].append(i)
# print(dic)

"""
在不改变列表数据结构的情况下找最大值li = [1,3,2,7,6,23,41,243,33,85,56]。
"""
# li = [1, 3, 2, 7, 6, 23, 41, 243, 33, 85, 56]
# li_puls = 0
# for i in li:
#         li_puls = i if i > li_puls else li_puls
# print(li_puls)

# li_puls = max(li)
# print(li_puls)

"""
在不改变列表中数据排列结构的前提下，找出以下列表中最接近最大值和最小值的平均值 的数
"""
# li = [-100, 1, 3, 2, 7, 6, 120, 121, 140, 23, 411, 99, 243, 33, 85, 56]
# li_relult = []
# li_puls = (max(li) + min(li)) // 2
# for i in li:
#     n = i - li_puls
#     n = abs(n)
#     li_relult.append(n)
# print(li_puls)      #验证结果
# print(li[li_relult.index(min(li_relult))])

"""
利用for循环和range输出9 * 9乘法表 。
"""

# for i in range(1,10):
#     print("%d * %d = "%(i, i), i*i)

# for i in range(1,10):
#     for k in range(1,10):
#         print("%d * %d = " % (i, k), i * k)

"""
求100以内的素数和
"""


# num = 0
# for i in range(2,100):
#    for j in range(2,i):
#       if(i%j==0):
#          break
#    else:
#        num +=i
# print(num)


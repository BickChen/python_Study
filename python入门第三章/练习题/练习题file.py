"""
用map来处理字符串列表,把列表中所有人都变成sb,比方alex_sb
"""
# name = ['alex', 'wupeiqi', 'yuanhao', 'nezha']
# name = list(map(lambda x:x + '_sb', name))
# print(name)

"""
用filter函数处理数字列表，将列表中所有的偶数筛选出来
"""
# def is_odd(x):
#     return x % 2 == 0
#
# num = [1, 3, 5, 6, 7, 8]
# for i in filter(is_odd, num):
#     print(i)

"""
如下，每个小字典的name对应股票名字，shares对应多少股，price对应股票的价格
"""

# portfolio = [
#     {"name": "IBM", "shares": 100, "price": 91.1},
#     {"name": "AAPL", "shares": 50, "price": 543.22},
#     {"name": "FB", "shares": 200, "price": 21.09},
#     {"name": "HPQ", "shares": 35, "price": 31.75},
#     {"name": "YHOO", "shares": 45, "price": 16.35},
#     {"name": "ACME", "shares": 75, "price": 115.65}
# ]

# 通过哪个内置函数可以计算购买每支股票的总价
# for i in map(lambda x:x['shares'] * x['price'], portfolio):
#     print(i)

# 用filter过滤出，单价大于100的股票有哪些

# print(list(filter(lambda x: x['shares'] > 100, portfolio)))

#有列表 li = ["alex", "egon", "smith", "pizza", "alen"], 请将以字母“a”开头的元素的首字母改为大写字母；
#
# li = ["alex", "egon", "smith", "pizza", "alen"]
# li = list(map(lambda x: x.capitalize(), li))
# print(li)

"""
有列表 li = [‘alex’, ‘egon’, ‘smith’, ‘pizza’, ‘alen’], 请以列表中每个元素的第二个字母倒序排序；
"""

# li = ["alex", "egon", "smith", "pizza", "alen"]
#
# li = list(sorted(li, key=lambda s: s[1], reverse= True))
# print(li)

"""
有名为poetry.txt的文件，其内容如下，请删除第三行；
"""

# import os
#
# f = open('poetry', 'r', encoding='utf-8')
# new_f = open('poetry.new', 'w', encoding='utf-8')
# file = filter(lambda x: '晴川历历汉阳树，芳草萋萋鹦鹉洲。' not in x , f)
# for i in file:
#     new_f.write(i)
# f.close()
# new_f.close()
# os.replace('poetry.new', 'poetry')

"""
有名为username.txt的文件，其内容格式如下，写一个程序，判断该文件中是否存在”alex”, 如果没有，则将字符串”alex”添加到该文件末尾，否则提示用户该用户已存在；
"""

# file = open('username', 'a+', encoding='utf-8')
# file.seek(0)
# user_judge = False
# for line in file:
#     line = line.strip()
#     if line == 'alex':
#         user_judge = True
# print(user_judge)
# if user_judge is False:
#     file.write('alex \n')
#     file.close()
#     print("用户已存在")

"""
写一个计算每个程序执行时间的装饰器；
"""
# import time
#
# def py_time(func):
#     def inner():
#         time_start = time.time()
#         func()
#         time_stop = time.time()
#         print("程序运行时间为：", time_stop-time_start, '秒')
#     return inner
#
# @py_time
# def alex():
#     time.sleep(5)
#     print("等待5秒")
#
# alex()




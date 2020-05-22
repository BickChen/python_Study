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

portfolio = [
    {"name": "IBM", "shares": 100, "price": 91.1},
    {"name": "AAPL", "shares": 50, "price": 543.22},
    {"name": "FB", "shares": 200, "price": 21.09},
    {"name": "HPQ", "shares": 35, "price": 31.75},
    {"name": "YHOO", "shares": 45, "price": 16.35},
    {"name": "ACME", "shares": 75, "price": 115.65}
]


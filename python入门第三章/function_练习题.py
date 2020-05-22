"""
写函数，计算传入数字参数的和。（动态传参）
"""

# def result(*args):
#     a = 0
#     for i in args:
#         if type(i) is int:
#             a +=i
#         else:
#             pass
#     return a
# print(result(1,2,3,4,5,6,7))
# print(result(1,'a',2,3,4,5,6,7))

"""
写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件的批量修改操作
"""
# import os
#
# def file_modify(file_name,old_str,new_str):
#     new_file_name = file_name + '.new'
#     f = open(file_name,'r')
#     f_2 = open(new_file_name, 'w')
#     for i in f:
#         if old_str in i:
#             i = i.replace(old_str, new_str)
#             f_2.write(i)
#         else:
#             f_2.write(i)
#     f.close()
#     f_2.close()
#     os.replace(new_file_name, file_name)
# file_modify('users','Alex','Yasin')

"""
函数，检查用户传入的对象（字符串、列表、元组）的每一个元素是否含有空内容。
"""

# def remove_spaces(object):
#     if not object:
#         print("您输入的对象有空内容")
#     elif all(object) is False:
#         print("您输入的对象有空内容")
#     else:
#         print("您输入的对象没有空内容")
#
# name = None
# name_list = [1,2,3,4]
# name_tuple = (1,2,3,4)
# remove_spaces(name)
# remove_spaces(name_list)
# remove_spaces(name_tuple)

"""
写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容（对value的值进行截断），
并将新内容返回给调用者，注意传入的数据可以是字符、list、dict
"""

# def truncation(object):
#     if type(object) is str:
#         if len(object) > 2:
#             return object[:2]
#         else:
#             return object
#     elif type(object) is list:
#         subscript = 0
#         for i in object:
#             if len(i) > 2:
#                 i = i[:2]
#                 object[subscript] = i
#             subscript +=1
#         return object
#     elif type(object) is dict:
#         for i in object:
#             if len(object[i]) > 2:
#                 object[i] = object[i][:2]
#         return object
#     else:
#         print("此类型无法处理")
#         return object
#
# old_str = 'abc'
# old_list = ['abc']
# old_dict = {'k1':'abc'}
# old_set = {1,2,3}
# list_value = [old_list,old_dict,old_set]
# old_str = truncation(old_str)
# for i in list_value:
#     i = truncation(i)
#     print(i)
# print(old_str,old_list,old_dict)

#解释闭包的概念

"""
写函数，返回一个扑克牌列表，里面有52项，每一项是一个元组
"""

# def poker():
#     poker_list = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
#     decor_list = ['方片', '红桃', '梅花', '黑桃']
#     deck = []
#     for decor in decor_list:
#         for i_poker in poker_list:
#             tuple_group = (decor, i_poker)
#             deck.append(tuple_group)
#     return deck
# deck = poker()
# print(deck)

"""
写函数，传入n个数，返回字典{"max":最大值,"min":最小值}
"""

# def minmax(*args):
#     dic = {'max':max(args),'min':min(args)}
#     return dic
# print(minmax(1,2,3,4,5,6,7,8,9))

"""
写函数，专门计算图形的面积
其中嵌套函数，计算圆的面积，正方形的面积和长方形的面积
调用函数area("圆形",圆半径) 返回圆的面积
调用函数area("正方形",边长) 返回正方形的面积
调用函数area("长方形",长，宽) 返回长方形的面积
"""

# def area(*args):
#
#     def circular(args):
#         if args[1].isdigit():
#             circular_area = 3.14 * (int(args[1])**2)
#             print("%s 面积等于 %d"%(args[0],circular_area))
#             return circular_area
#         else:
#             print("您输入%s的数值不是一个int类型" % args[0])
#
#     def square(args):
#         if args[1].isdigit():
#             square_area = int(args[1]) * int(args[1])
#             print("%s 面积等于 %d"%(args[0],square_area))
#             return square_area
#         else:
#             print("您输入%s的数值不是一个int类型" % args[0])
#
#     def rectangle(args):
#         if args[1].isdigit() and args[2].isdigit():
#             rectangle_area = int(args[1]) * int(args[2])
#             print("%s 面积等于 %d" % (args[0],rectangle_area))
#             return rectangle_area
#         else:
#             print("您输入%s的数值不是一个int类型"%args[0])
#
#     if args[0] == "圆形":
#         circular(args)
#     elif args[0] == '正方形':
#         square(args)
#     elif args[0] == '长方形':
#         rectangle(args)
#     else:
#         print("您输入的%s图形该函数无法处理"%args[0])
#
# area('圆形',"30")
# area('正方形',"30")
# area('长方形',"30","40")

"""
写函数，传入一个参数n，返回n的阶乘
"""


# def cal(n):
#
#     def factorial(n):
#         product = 1
#         for i in range(1,n):
#             product *=i
#         print(product)
#         return product
#
#     if type(n) is int:
#         factorial(n)
#     elif type(n) is str and n.isdigit():
#         n = int(n)
#         factorial(n)
#     else:
#         print("您输入的数据类型不符合")
#
# for i in range(1,8):
#     cal(i)



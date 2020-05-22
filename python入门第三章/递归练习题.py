"""
非固定参数练习
"""

# def print_info(*args, **kwargs):
#     print("----- 注册学生信息 -----")
#     for i in kwargs:
#         print(i + ':' + str(kwargs[i]))
# print_info(name="alex", age=22, sex='M')
# print_info(name='Jack', age=26, sex="M", hobbie="学习")

"""
嵌套函数练习
"""

# def get_rem(x):
#     return x % 2
# def get_chare(x,y,f):
#     return f(x) + f(y)
#
# result = get_chare(2,9,get_rem)
#
# print(result)

"""
用递归实现2分查找的算法，以从列表 a = [1,3,4,6,7,8,9,11,15,17,19,21,22,25,29,33,38,69,107] 查找指定的值。
"""

# list_test = [1, 3, 4, 6, 7, 8, 9, 11, 15, 17, 19, 21, 22, 25, 29, 33, 38, 69, 107]

# def re(a,b,u_list, users_input):
#     """
#     每次把列表规模折半，查找一个数据最多只需要2的n次方 < len(d_list),是2的多少次方，就是最多查多少次。
#     假如列表长度为200，那最多只需查询8次(2**8次方）
#     :param start: 查找的起始位置
#     :param end: 查找的结束位置
#     :param n: 要查找的值
#     :param d_list: 要找的列表
#     :return:
#     """
#     if a < b:
#         age = (a + b) // 2
#         if u_list[age] > users_input:
#             re(a,age,u_list,users_input)
#         elif u_list[age] < users_input:
#             re(age+1,b,u_list,users_input)
#         else:
#             print("值在列表里")
#     else:
#         print("值不在列表里")
# re(0,len(list_test),list_test,8)










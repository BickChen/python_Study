"""
静态方法、类方法、属性方法的区别，通过代码来体现
"""

# class Test(object):
#     name = 'aaa'
#     def __init__(self, name):
#         self.name = name
#
#     @classmethod              #只能访问类变量，无法访问实例变量
#     def name_test(cls):
#         print(cls.name)
#
#     @staticmethod             #无法访问实例变量和类变量，可以从外部传递参数
#     def funk(sss):
#         print(sss)
#
#     @property                 #可以访问实例变量和类变量，不可以从外部传递参数，调用时不能加()
#     def funk_1(self):
#         print(self.name)
#
# p = Test('Alex')
# p.name_test()
# p.funk("sss")
# print(p.funk_1)

"""
如何通过反射往一个类里添加一个方法
请通过代码实现反射判断当前模块里是否有一个Dog类
"""

# class Reflex(object):
#
#     sex = "M"
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print(self.sex)
#
# def printing(self):
#     print(self.name, self.age)
#
# setattr(Reflex, 'printing', printing)
# p = Reflex('Alex', 26)
# p.printing()
#
# import sys
# this_module = sys.modules[__name__]
# print(hasattr(this_module,'Dog'))


# import importlib
# package_key = importlib.import_module('dev.campus_IT')
# print(package_key)
# print(hasattr(package_key,'BranchSchool'))

"""
别看wiki里的代码，自己手动写出一个单例模式
"""

# class SingleCase(object):
#     sex = None
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def user(self):
#         print(self.name, self.age)
#
#     def __new__(cls, *args, **kwargs):
#         if cls.sex == None:
#             cls.sex = object.__new__(cls)
#         return cls.sex
#
# p1 = SingleCase('Alex',22)
# p2 = SingleCase('Yasin',23)
# print(p1.user())
# print(p2.user())

# class School:
#     def __init__(self,name,addr,type):
#         self.name = name
#         self.addr = addr
#         self.type = type
#     def __repr__(self):
#         return self.name
#     def __str__(self):
#         return '(%s,%s)' %(self.name,self.addr)
# s1=School('小猿圈','北京','私立')
# print('from repr: ',repr(s1))
# print('from str: ',str(s1))
# print(s1)
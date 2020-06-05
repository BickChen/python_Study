#
# class Person:
#     sex = "男"
#
#     def __init__(self,name,age,introduce):
#         self.name = name
#         self.age = age
#         self.introduce = introduce
#
#     def output(self):
#         a = print(self.name)
#         return a
# a = Person('小明',10,'上山去砍柴')
# print(a.output())

# class Stu(object):
#     __stu_num = 0
#     def __init__(self,name):
#         self.name = name
#         self.abc()
#
#     def abc(self):
#         self.__stu_num += 1
#         print("成功", self.__stu_num)
#
# a1 = Stu('Alex')
# a2 = Stu("Yasin")

class Flight(object):
    def __init__(self,name):
        self.name = name

    def filght_status(self,age):
        print("name : a",self.name,age)

def name(self):
    print(self.name)

f = Flight("Alex")
setattr(Flight, 'n', name)
f.n()
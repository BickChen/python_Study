
class Person:
    sex = "男"

    def __init__(self,name,age,introduce):
        self.name = name
        self.age = age
        self.introduce = introduce

    def output(self):
        a = print(self.name)
        return a
a = Person('小明',10,'上山去砍柴')
print(a.output())
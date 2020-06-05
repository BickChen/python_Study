"""
有多个课程，课程要有定价
有多个班级，班级跟课程有关联
有多个学生，学生报名班级，交这个班级对应的课程的费用
有多个老师，可以分布在不同校区，上不同班级的课
有多个员工，可以分布在不同校区在总部可以统计各校区的账户余额、员工人数、学员人数
学生可以转校、退学
"""

class Relationship:
    campus = []
    staff = {}
    stu = {}
    def join_headquarters(self,obj):
        self.campus.append(obj)
        self.staff[obj] = []
        self.stu[obj] = []

    def join_students(self,k,v):
        if k in self.staff:
            self.staff[k].append(v)
            print("%s %s 在%s校区工作"%(v.position,v.name,k.name))
        else:
            print("您选择加入的校区不存在！")

    def __repr__(self):
        return

    # def join_pupil(self,obj):
    #     if obj.class_obj.school_ojb in self.stu:
    #         self.stu[obj.class_obj.school_ojb].append(obj)
    #         print(self.stu)

class School:
    def __init__(self,name,address,capital):
        self.name = name
        self.address = address
        self.capital = capital
        self.relationship = Relationship()
        print("%s总部成立，地址为：%s, 注册资金：%d."%(self.name,self.address,self.capital))
    def pay_roll(self):
        for i in self.relationship.campus:
            for z in self.relationship.staff[i]:
                self.capital -= z.salary
                print("给%s校区的%s发了%d工资"%(i.name,z.name,z.salary))
        print("余额剩余：%d"%self.capital)

    def count_staff_num(self):
        num = 0
        for i in self.relationship.staff:
            b_schoole = len(self.relationship.staff[i])
            print("%s 校区一共有%d个员工。"%(i.name,b_schoole))
            num += b_schoole
        print("总共有%d名员工"%num)

    def count_stu_num(self):
        num = 0
        for i in self.relationship.stu:
            b_schoole = len(self.relationship.stu[i])
            print("%s 校区一共有%d个学员。"%(i.name,b_schoole))
            num += b_schoole
        print("总共有%d名学员"%num)

    # def new_staff_enrollment(self):
    #     pass

class BranchSchool:
    def __init__(self,name,address,head):
        self.name = name
        self.address = address
        self.head = head
        self.relationship = Relationship()
        print("%s 地址是：%s 隶属于%s总部,%s."%(self.name,self.address,self.head.name,self.head.address))

class Course:
    def __init__(self,name,price):
        self.name = name
        self.price = price
        print("小猿圈开设了%s课程，价格：%d"%(self.name,self.price))

class Class:
    def __init__(self,num,course_obj,school_ojb):
        self.class_num = num
        self.course_obj = course_obj
        self.school_ojb = school_ojb
        print("%s校区，%s课程，%s开课了"%(self.school_ojb.name,self.course_obj.name,self.class_num))

    def create_teaching_record(self):
        pass

    def drop_out(self):
        pass

class Staff:
    def __init__(self,name,age,position,salary,dept):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
        self.dept = dept
        self.relationship = Relationship()
        print("%s 年龄：%d 职位：%s 薪资：%d 部门：%s"%(self.name,self.age,self.position,self.salary,self.dept))

class Teacher(Staff):
    def __init__(self,name,age,position,salary,dept,teaching):
        super().__init__(name,age,position,salary,dept)
        self.teaching = teaching
        print("%s 讲师负责 %s校区%s课程的%s"%(self.name,self.teaching.school_ojb.name,self.teaching.course_obj.name,self.teaching.class_num))

class Student:
    def __init__(self,name,age,degree,class_obj,balance):
        self.name = name
        self.age = age
        self.degree = degree
        self.class_obj = class_obj
        self.balance = balance
        # self.relationship = Relationship()
        print("%s 年龄：%s 程度：%s 报名班级：%s 余额：%d"%(self.name,self.age,self.degree,self.class_obj.class_num,self.balance))

    def pay_tuition(self):
        self.relationship = Relationship()
        if self.class_obj.school_ojb in self.relationship.stu:
            self.balance -= self.class_obj.course_obj.price
            print("%s 缴费%d 余额：%d"%(self.name,self.class_obj.course_obj.price,self.balance))
            self.relationship.stu[self.class_obj.school_ojb].append(self)



headquarters = School("小猿圈", "北京市人民路122号", 50000000)
headquarters.relationship.join_headquarters(headquarters)
branch_01 = BranchSchool('小猿圈上海分校', '上海市人民路122号', headquarters)
branch_01.relationship.join_headquarters(branch_01)
branch_02 = BranchSchool('小猿圈深圳分校', '深圳市人民路122号', headquarters)
branch_02.relationship.join_headquarters(branch_02)

headquarters.pay_roll()


java_coures = Course('java',10000)
python_coures = Course('python',12000)

class_01 = Class('java-222班', java_coures, headquarters)
class_02 = Class('python-222班', python_coures, branch_01)

yasin = Staff('Yasin', 22, 'CEO', 500000, '总经办')
yasin.relationship.join_students(headquarters,yasin)

alex = Teacher('Alex', 26, '讲师', 50000, '教育部',class_02)
alex.relationship.join_students(branch_01,alex)

headquarters.pay_roll()
headquarters.count_staff_num()

student_01 = Student('zhangsan', 19, '开发小白', class_02, 50000)
student_02 = Student('lisi', 20, '开发小白', class_01, 100000)
student_01.pay_tuition()
headquarters.count_stu_num()

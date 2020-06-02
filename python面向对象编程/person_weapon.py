"""
开发一个反恐游戏，有警察、恐怖分子，还有各种武器，他们可以互砍互杀。
注意，警察不能用炸药包，恐怖分子可以。炸药包一用，全部玩家都得死。
提示：可以只写一个Person类，一个weapon类。
"""
class Weapon:
    def pocketknife(self,obj):
        """小刀"""
        self.name = '小刀'
        self.attack_val = 40
        obj.arms = self.name
        obj.aggressivity = self.attack_val

    def ak_47(self,obj):
        """AK_47"""
        self.name = 'AK_47'
        self.attack_val = 70
        obj.arms = self.name
        obj.aggressivity = self.attack_val

    def explosive(self,obj):
        """炸药包"""
        self.name = '炸药包'
        self.attack_val = 100
        if obj.role == '匪徒':
            obj.arms = self.name
            obj.aggressivity = self.attack_val
        else:
            print("%s 是一个警察，不能使用炸药包。"%obj.name)

class Person:
    aggressivity = 30
    arms = '拳头'
    blood_vol = 100
    def __init__(self,name,role):
        self.name = name
        self.role = role
        self.Weapon = Weapon()
    def attack(self,*args):
        if self.role == '匪徒' and self.arms == '炸药包':
            for i in args:
                i.blood_vol = 0
                print("[%s]:%s 使用%s攻击了[%s]:%s , [%s]:%s还剩%d点血" % (
                self.role, self.name, self.arms, i.role, i.name, i.role, i.name,
                i.blood_vol))
            self.blood_vol = 0
            print("[%s]:%s 使用%s，[%s]:%s还剩%d点血"%(self.role,self.name,self.arms,self.role,self.name,self.blood_vol))
        else:
            args[0].blood_vol -= self.aggressivity
            print("[%s]:%s 使用%s攻击了[%s]:%s , [%s]:%s还剩%d点血"%(self.role, self.name, self.arms, args[0].role, args[0].name, args[0].role, args[0].name, args[0].blood_vol))


a = Person("Yasin", "警察")
b = Person("Alex", "匪徒")
c = Person("Mjj", "匪徒")

a.Weapon.ak_47(a)
a.attack(b)
b.Weapon.explosive(b)
b.attack(a,c)

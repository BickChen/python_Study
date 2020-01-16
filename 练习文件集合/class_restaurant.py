class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print('Restaurant name: '+self.name.title()+'\nMenu: '+self.type)
        print('number served: '+str(self.number_served))
    def open_restaurant(self):
        print(self.name.title()+' open the door!')
    def set_number_served(self,number):
        self.number_served = number
    def increment_number_served(self,number):
        self.number_served+=number
# name = Restaurant('RNG','S')
# name_01 = Restaurant('EDG', 'B')
# name_02 = Restaurant('FPX', 'S')
# print(name.describe_restaurant())
# print(name_01.describe_restaurant())
# print(name_02.describe_restaurant())

name = Restaurant('rng', 's')
print(name.describe_restaurant())
name.set_number_served(30)
print(name.describe_restaurant())
name.increment_number_served(30)
print(name.describe_restaurant())
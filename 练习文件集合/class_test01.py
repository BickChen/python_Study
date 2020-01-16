class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
    def describe_restaurant(self):
        print('Restaurant name: '+self.name.title()+'\nMenu: '+self.type)
    def open_restaurant(self):
        print(self.name.title()+' open the door!')
name = Restaurant('RNG','S')
name_01 = Restaurant('EDG', 'B')
name_02 = Restaurant('FPX', 'S')
print(name.describe_restaurant())
print(name_01.describe_restaurant())
print(name_02.describe_restaurant())
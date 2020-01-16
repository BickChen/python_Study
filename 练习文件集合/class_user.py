class User():
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.login_attempts = 0
    def describe_user(self):
        print("name: "+self.name.title())
        print('gender: '+self.gender)
    def greet_user(self):
        print('Happy New Year '+self.name+'!')
    def increment_login_attempts(self):
        self.login_attempts+=1
    def reset_login_attempts(self):
        self.login_attempts = 0

name = User('lisi', 'girl')
print(name.login_attempts)
name.increment_login_attempts()
name.increment_login_attempts()
print(name.login_attempts)
name.reset_login_attempts()
print(name.login_attempts)
# tom_name = User('tom','man')
# jay_name = User('jay','girl')
# print(tom_name.describe_user())
# print(tom_name.greet_user())
# print(jay_name.describe_user())
# print(jay_name.greet_user())
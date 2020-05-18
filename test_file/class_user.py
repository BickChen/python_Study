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

class Admin(User):
    def __init__(self, name, gender):
        super().__init__(name, gender)
        self.admin = Privileges()
    def show_privileges(self):
        if self.name == "Admin":
            print("Administrator rights: ")
            print(self.admin.privileges[0])
            print(self.admin.privileges[1])
            print(self.admin.privileges[2])
        else:
            print("User access: ")
            print(self.admin.privileges[0])


class Privileges():
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']


admin_user = Admin('dmin','man')
print(admin_user.show_privileges())

# admin_user = Admin('dmin','man')
# print(admin_user.show_privileges())


# name = Useradd('lisi', 'girl')
# print(name.login_attempts)
# name.increment_login_attempts()
# name.increment_login_attempts()
# print(name.login_attempts)
# name.reset_login_attempts()
# print(name.login_attempts)
# tom_name = User('tom','man')
# jay_name = User('jay','girl')
# print(tom_name.describe_user())
# print(tom_name.greet_user())
# print(jay_name.describe_user())
# print(jay_name.greet_user())
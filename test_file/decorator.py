namedb = {'start':False, 'username':'zhangshan', 'password':'abc'}
def login(faid):
    def innor():
        if namedb['start'] == False:
            username = input("user:")
            password = input('Password:')
            if username == namedb['username'] and password == namedb['password']:
                namedb['start'] = True
                faid()
                print("登陆成功！")
            else:
                print("用户名或密码不对，请重新登陆")
                innor()
        else:
            faid()
            print('已登陆！')
    return innor

def home():
    print("---首页---")

@login
def usa():
    print("---USA---")

@login
def china():
    print("---China---")

home()
usa()
china()
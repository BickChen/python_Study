dic = {'socket':False}

def login(func):
    def inner(*args,**kwargs):
        if dic['socket'] == False:
            username = input("请输入用户名：")
            userpasswd = input("请输入密码：")
            file = open('users_certification_data', 'r', encoding='utf-8')
            for line in file:
                line = line.strip().split(',')
                if username == line[0] and userpasswd == line[1]:
                    dic['socket'] = True
                    func(*args,**kwargs)
        else:
            func(*args,**kwargs)
    return inner

def payment(func):
    def pay(*args,**kwargs):
        print("此网页需要收费10元，请支付")
        money = input(">>>: ")
        if money.isdigit():
            money = int(money)
            if money > 10:
                func(*args,**kwargs)
    return pay

@login
@payment
def usa(*args,**kwargs):
    print('欢迎来到USA')

@login
@payment
def china(*args,**kwargs):
    print('欢迎来到中国')

usa("users_certification_data")
#print(dic)
china("users_certification_data")

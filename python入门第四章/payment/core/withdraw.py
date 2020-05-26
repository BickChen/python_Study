import json, modular_mod, os, sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #__file__的是打印当前被执行的模块.py文件相对路径，注意是相对路径
sys.path.append(BASE_DIR)
from user_passwd_md5 import user_verification
#print("成功")
@user_verification
def withdrawal():
    user_data = modular_mod.file_info("../account")
    account_options = input("""
    ———- ICBC Bank ————-
      1.  账户信息
      2.  提现

    >>>:""")
    if account_options.isdigit() and int(account_options) in range(1,3):
        account_options = int(account_options)
        if account_options == 1:
            file = open(user_data['alex'])
            user_info = json.load(file)
            file.close()
            for i in user_info:
                print("%s:   %s"%(str(i), str(user_info[i])))
        else:
            file = open(user_data['alex'])
            user_info = json.load(file)
            file.close()
            amount_money = input("请输入提现金额：")
            if amount_money.isdigit() and int(amount_money) <= user_info['credit']:
                amount_money = int(amount_money)
                user_info['credit'] = int(user_info['credit']) - amount_money - amount_money * 0.05
                file = open(user_data['alex'], 'w')
                json.dump(user_info, file)
                file.close()
            else:
                print("你没有那么多信用额度")
    else:
        print("没有此选项")

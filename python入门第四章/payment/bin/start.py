import json, modular_mod, os, sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #__file__的是打印当前被执行的模块.py文件相对路径，注意是相对路径
sys.path.append(BASE_DIR)
from core.withdraw import withdrawal
from user_passwd_md5 import user_verification


# 生成用户数据文件
# name_data = {"username": "alex", "balance": 100000000}
# file = open('../account/alex', 'w')
# json.dump(name_data, file)
@user_verification
def transfer_accounts():
    user_data = modular_mod.file_info("../account")
    account_options = input("""
    ———- ICBC Bank ————-
      1.  账户信息
      2.  转账
    
    >>>:""")
    if account_options.isdigit() and int(account_options) in range(1,3):
        account_options = int(account_options)
        if account_options == 1:
            file = open(user_data['alex'])
            user_info = json.load(file)
            file.close()
            for i in user_info:
                print("%s:    %s"%(str(i), str(user_info[i])))
        else:
            file_alex = open(user_data['alex'])
            file_tesla = open(user_data['tesla_company'])
            alex = json.load(file_alex)
            tesla = json.load(file_tesla)
            file_alex.close()
            file_tesla.close()

            alex['balance'] = int(alex['balance']) - 9500000 - 9500000 * 0.05
            tesla['balance'] = int(tesla['balance']) + 9500000
            file_alex = open(user_data['alex'], 'w')
            file_tesla = open(user_data['tesla_company'] , 'w')
            json.dump(alex, file_alex)
            json.dump(tesla, file_tesla)
            file_alex.close()
            file_tesla.close()
    else:
        print("没有此选项")

transfer_accounts()
withdrawal()
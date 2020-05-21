
def print_user_info(format_list,dic,username):
    """
    传入读取的文件数据表格索引列表 format_list
    传入读取的文件数据生成的字典 dic
    传入需要打印用户数据的用户名 username
    用格式化打印的方式将所有数据传入for循环打印
    """
    print("-" * 40)
    count = 0
    for i in format_list:
        print("%s:             %s"%(i,dic[username][count]))
        count +=1
    print("-" * 40)

def save_back_file(format_list,dic,username):
    """
    传入读取的文件数据表格索引列表 format_list
    传入读取的文件数据生成的字典 dic
    传入需要修改用户数据的用户名 username
    判断用户输入的数据索引是否为真，不为真直接告知不是一个正确的索引，退出函数
    为真则修改用户数据字典dic 相应的值，然后通过join方法将列表转换为字符串重写文件
    """
    print('person data: ' + str(dic[username]))
    count = 0
    for i in format_list:
        print("%d.   %s:         %s"%(count,i,str(dic[username][count])))
        count +=1
    modify_index = input("[select column id to change]: ")
    if modify_index.isdigit():
        modify_index = int(modify_index)
        if modify_index <= (len(dic[username])-1) :
#            old_value = input("current value>: ")
            new_value = input("new value>: ")
            dic[username][modify_index] = new_value
            file = open(file_name, 'w', encoding='utf-8')
            file.write(','.join(format_list) + '\n')
            for line in dic:
                content = dic[line]
                file.write(','.join(content) + '\n')
            file.close()
        else:
            print("输入的索引不存在")
    else:
        print("输入的不是一个正确的索引")

def change_personal_info(format_list,dic,username):
    """
    传入读取的文件数据表格索引列表 format_list
    传入读取的文件数据生成的字典 dic
    传入需要修改用户数据的用户名 username
    修改用户数据字典dic 相应的值，然后通过join方法将列表转换为字符串重写文件
    """
    new_passwd = input("New Passwork：")
    dic[username][1] = new_passwd
    file = open(file_name, 'w', encoding='utf-8')
    file.write(','.join(format_list) + '\n')
    for line in dic:
        content = dic[line]
        file.write(','.join(content) + '\n')
    file.close()
    print("修改成功")


file_name = 'user_information'
open_file = open(file_name, 'r', encoding='utf-8')
open_file.seek(0)
type_dic = open_file.readline().strip().split(",")
user_dic = {}
for line in open_file:
    line = line.strip().split(",")
    user_dic[line[0]] = line
# print(user_dic.keys())
open_file.close()

count = 0
while count <3:
    count += 1
    username = input("Username: ")
    password = input("Password: ")
    if username in user_dic.keys() and password == user_dic[username][1]:
        while True:
            print("""
-------------------welcome alex --------------------
1. 打印个人信息
2. 修改个人信息
3. 修改密码
（输入q或quit退出程序）
            """)
            user_input = input('>>>')
            if user_input.isdigit():
                user_input = int(user_input)
            if user_input == 'q' or user_input == 'quit':
                print('bye.')
                exit()
            elif user_input == 1:
                print_user_info(type_dic,user_dic,username)
            elif user_input == 2:
                save_back_file(type_dic,user_dic,username)
            elif user_input == 3:
                change_personal_info(type_dic,user_dic,username)
            else:
                print("您输入的不是一个正确的选项")
    else:
        print('用户不存在！您还有%d次机会'%(3-count))



def file_modify(file_name, file_data):
    with open(file_name, 'w') as file:
        file.write(file_data)
        print('修改成功')

def file_replace(file_name, file_old_data, file_new_data):
    with open(file_name, 'r') as file:
        with open(file_name+'new', 'w') as file_new:
            for i in file:
                if file_old_data in i:
                    i.replace(file_old_data, file_new_data)
                    file_new.write(i)




if __name__ in '__main__':
    pass
    # file_name = 'test.txt'
    # file_data = 'Hi Yasin' + '\n'
    # file_modify(file_name, file_data)




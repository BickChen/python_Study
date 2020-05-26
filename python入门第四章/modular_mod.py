import os

# 生成用户数据文件
# name_data = {"expire_date": "2021-01-01", "id": 1234, "status": 0, "pay_day": 22, "password": "abc"}
# file = open('user_data/Yasin', 'w')
# json.dump(name_data, file)
def file_info(file_dir):
    """
    file_dir 应该填写文件所在的绝对路径
    生成字典形式为：
    {'higui.py': 'D:\\python_Study\\Mapping\\higui.py'}
    """
    user_data = {}
    user_catalog = os.listdir(file_dir)
    for i in user_catalog:
        user_data[i] = (os.path.join(os.path.abspath(file_dir), i))
    return user_data


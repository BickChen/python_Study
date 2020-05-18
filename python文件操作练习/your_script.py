"""
写一个脚本，允许用户按以下方式执行时，即可以对指定文件内容进行全局替换
"""

import sys
import os
user_input = sys.argv
# print(user_input)
#user_input = ['test', 'tast', 'test']
python_filename, old_str, new_str, filename = user_input
# filename = user_input[3]
# old_str = user_input[1]
# new_str = user_input[2]
new_filename = filename + '.new'
f = open(filename, 'r', encoding='UTF-8')
f_new = open(new_filename, 'w', encoding='UTF-8')
for i in f:
    if old_str in i:
        i = i.replace(old_str, new_str)
    f_new.write(i)
f.close()
f_new.close()

os.replace(new_filename, filename)


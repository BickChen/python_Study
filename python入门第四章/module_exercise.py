"""
导入模块的方式有哪几种，官方不推荐哪种？
导入目录的方式有以下几种：
import os
form os import read
form os.read import XXX as rename
form os import *
官方不推荐form os import *
这种方式可能会引起调用其他模块时有重名方法之间互相覆盖，导致代码难以排错。
"""

"""
如何让你写的模块可以被系统上任何一个py文件导入
将你写的模块复制到python的path中
"""

import time

current_time = time.time()
print(current_time)
current_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(current_time))
print(current_time)
current_time = time.mktime(time.strptime(current_time,'%Y-%m-%d %H:%M:%S'))
print(current_time)
current_time = time.localtime(current_time)
print(current_time)

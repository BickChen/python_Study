"""
任一个英文的纯文本文件，统计其中的每个单词出现的个数，注意是每个单词。。
"""

# f = open("username")
# user_list = []
# for i in f:
#     i = i.split()
#     for v in i:
#         user_list.append(v)
# user_set = set(user_list)
# for k in user_set:
#     print("%s 在list里有 %s个"%(k,user_list.count(k)))

"""
有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
"""

f = open("username")
codo_count = 0
comment_count = 0
blank_line = 0
for i in f:
    i = i.split()
    if len(i) == 0:
        blank_line +=1
    else:
        if i[0] == "#":
            comment_count += 1
        elif type(i[0]) is str:
            codo_count +=1
print("代码有：%d 行，注释有： %d 行，空行有： %d 行"%(codo_count, comment_count, blank_line))

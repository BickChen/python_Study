# names = ['tom','jer','tark']
#
# print("Hi "+names.pop().title()+" may I have dinner?")
# print("Hi "+names.pop().title()+" may I have dinner?")
# print("Hi "+names.pop().title()+" may I have dinner?")
#
# names = ['tom','jer','tark']
# del names[1]
# names.append('micael')
#
# print("Hi "+names.pop().title()+" may I have dinner?")
# print("Hi "+names.pop().title()+" may I have dinner?")
# print("Hi "+names.pop().title()+" may I have dinner?")

# names = ['tom','jer','tark']
# names.append("lisi")
# names.insert(0,'tyn')
# names.insert(-0,'panda')
# print(names)

# names = ['tom','jer','tark']
# names_del = names.pop()
# names.append('micael')
#
# print("Hi "+names.pop().title()+" may I have dinner?")
# print("Hi "+names.pop().title()+" may I have dinner?")
# print("Hi "+names.pop().title()+" may I have dinner?")
# print(names_del.title()+" Unfortunately!")

names = []
for i in range(0,3):
    if names:         #Python将非空字符串解读为True
        print(i)
        print(names)
    else:
        names.append('Yes')

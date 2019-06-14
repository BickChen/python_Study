# age = range(1,20)
# for i in age:
#     if i >= 1 and i <=5:
#         print(i)
#     elif i >= 7 and i <=9:
#         print(i)
#     elif i >= 11 and i <=12:
#         print(i)
#     else:
#         pass

# age = 0
# while age < 12:
#     if age == 5:
#         age +=2
#     elif age == 9:
#         age +=2
#     else:
#         age +=1
#     print(age)

# age = 0
# age_to = 101
# age_set = range(0,51)
# while age < 100:
#     if age < 50:
#         age_to -=1
#         print(age_to)
#         age +=1
#         continue
#     else:
#         for i in age_set:
#             print(i)
#         break
age = 1

while age <= 100:
    if age % 2 !=0:
        print(age)
    age +=1
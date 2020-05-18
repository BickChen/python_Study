# car = input("What car to buy?:")
# print("I want one "+car)

# names = int(input('How many people?:'))
# if names < 8:
#     print('OK, no problem.')
# else:
#     print('sorry, no location')

sandwich_orders = ['Tom','Jay','zhangsan','lisi']
finished_sandwiches = []
while len(sandwich_orders) != 0:
    abc = sandwich_orders.pop()
    finished_sandwiches.append(abc)
    print("I made your tuna sandwich!")
    # if len(sandwich_orders) == 0:
    #     break
    # else:
    #     continue
print(finished_sandwiches)
    # a = sandwich_orders.pop()
    # finished_sandwiches.append(a)


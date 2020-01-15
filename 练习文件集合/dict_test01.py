#
# names = []
# for i in range(0,6):
#     dict_names = {'name':'yasin','age':'22','address':'shanghai'}
#     names.append(dict_names)
#     print(names[i])

Tom = {'name':'Tom','age':'1','品种':'阿拉斯加'}
Jay = {'name':'Jay','age':'1','品种':'泰迪'}
a = {'Tom':['acl','abc'],'acl':{'name':'acl','age':'1','品种':'泰迪'}}
a['Tom'].append('cbd')
a['Tom'].sort()
print(a['Tom'])
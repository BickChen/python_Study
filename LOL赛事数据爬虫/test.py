# import pymongo
#
# myclient = pymongo.MongoClient('xxxx')
# dblist = myclient.list_database_names()
# print(dblist)

import oss2
endpoint = 'http://oss-cn-shanghai.aliyuncs.com'
auth = oss2.Auth('xxxx', 'xxxx')
backet = oss2.Bucket(auth, endpoint, 'xxxx')
for object_info in oss2.ObjectIterator(backet):
    print(object_info.key)
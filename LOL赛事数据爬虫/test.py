# import pymongo
#
# myclient = pymongo.MongoClient('mongodb://root:F2V2InNkKifsePJg@101.133.144.63:27017/')
# dblist = myclient.list_database_names()
# print(dblist)

import oss2
endpoint = 'http://oss-cn-shanghai.aliyuncs.com'
auth = oss2.Auth('LTAI4G7sKG8pdYAXkSo9ANrd', '8FeSeD6nyadeMkQ5jywhrMUm5BkQ4O')
backet = oss2.Bucket(auth, endpoint, 'lolmatchimg')
for object_info in oss2.ObjectIterator(backet):
    print(object_info.key)
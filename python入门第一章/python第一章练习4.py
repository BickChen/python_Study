"""
题目：假设一年期定期利率为3.25%，计算一下需要过多少年，一万元的一年定期存款连本带息能翻番？
"""


Principal = 10000
year = 0
while Principal < 20000:
    i = Principal * 0.0325
    Principal = Principal + i
    if Principal != 20000 :
        year +=1

print("需要%d年，10000元才能翻倍到%f元"%(year,Principal))

"""以下为网上标准答案"""
principal = 10000
year = 0
while principal < 20000:
    principal = principal * 1.0325
    year = year + 1
print('需要%d年一万元的存款才能连本带息翻番' % year)
print(str(year)+'年以后，一万元的存款才能连本带息翻番')  # 顺便复习str()

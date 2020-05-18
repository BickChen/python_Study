a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
b = int(input('请输入你要查找的数字：'))
def test(list_a,age):
    bak = int(len(list_a)/2)
    if age == list_a[bak]:
        print('参数存在')
    elif age > list_a[bak]:
        list_a = list_a[bak:]
        test(list_a, age)
    elif age < list_a[bak]:
        list_a = list_a[:bak]
        test(list_a, age)

test(a, b)


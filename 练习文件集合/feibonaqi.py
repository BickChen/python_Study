
def feibo(n):
    a = 0
    b = 1
    age = 0
    while age < n:
        tmp = a
        a = b
        b = tmp + b
        yield b
        age +=1
f = feibo(20)
list_test = []
while True:
    list_test.append(f.__next__())
    print(list_test)
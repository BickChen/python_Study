
def g_name(name):
    print("消费者%s,开始吃包子了!")
    while True:
        d = yield
        print("消费者%s,吃到%s包子！"%(name, d))

C1 = g_name('C1')
C2 = g_name('C2')
C3 = g_name('C3')
C1.__next__()
C2.__next__()
C3.__next__()

for i in range(1,10):
    C1.send(i)
    C2.send(i)
    C3.send(i)
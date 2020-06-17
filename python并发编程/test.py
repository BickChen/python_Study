# from multiprocessing import Process
# import time
# import random
#
#
# def task(n):
#     time.sleep(random.randint(1,3))
#     print('-------->%s' %n)
#
#
# if __name__ == '__main__':
#     p1 = Process(target=task, args=(1,))
#     p2 = Process(target=task, args=(2,))
#     p3 = Process(target=task, args=(3,))
#
#     p1.start()
#     p1.join()
#     p2.start()
#     p2.join()
#     p3.start()
#     p3.join()
#
#     print('-------->4')

# from multiprocessing import Process
# n=100 #在windows系统中应该把全局变量定义在if __name__ == '__main__'之上就可以了
# def work():
#     print('子进程内: ',n)
#
#
# if __name__ == '__main__':
#     p=Process(target=work)
#     p.start()
#     print('主进程内: ',n)

import socket
from multiprocessing import Process

host_post = ('0.0.0.0', 8080)
phone=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.bind((host_post))
# phone.listen(5)
def connt():
    coon, cilent_addr = phone.accept()
    print(coon, cilent_addr)

if __name__ == "__main__":
    p1 = Process(target=connt,)
    p2 = Process(target=connt,)

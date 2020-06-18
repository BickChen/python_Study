import socket
import struct
import json

host_post = ('127.0.0.1', 8080)
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.connect(host_post)

while True:
    #第一步，输入命令并判断命令是否为空，如果为空将重新循环，数据成功发送，反馈信息。
    user_input = input(">>>：").strip()
    if len(user_input) == 0:continue
    phone.send(user_input.encode("utf-8"))
    print("发送成功！")
    #第二步，接受服务端，发送的header信息长度，因为经过struct打包的bytes格式的整数字符串bytes长度都为4所以取4个bytes
    header = phone.recv(4)
    header_byes_size = struct.unpack('i', header)[0]
    print(header_byes_size)
    #第三步，根据解析出来的header数据长度获取header信息,并将header信息解析回字典格式。
    header_byes = phone.recv(header_byes_size)
    print(header_byes)
    header_size = json.loads(header_byes.decode('utf-8'))['date_size']
    print(header_size)

    # header_size = header_dic['date_size']
    # print(header_size)
    tital_size = 0
    # date_len = b""
    #第四步，根据header信息中获取的命令返回结果数据的长度来循环将数据从系统内存中取出来，并打印
    while tital_size < header_size:
        # print(header_size, tital_size)
        date = phone.recv(1024)
        print(date.decode("gbk"))
        tital_size += len(date)
        # date_len +=date

    # print(date_len.decode('utf-8'))
    # phone.close()
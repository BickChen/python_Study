import socket
import struct
import json

host_post = ('127.0.0.1', 8080)
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.connect(host_post)

while True:
    user_input = input(">>>：").strip()
    if len(user_input) == 0:continue
    phone.send(user_input.encode("utf-8"))
    print("发送成功！")

    header = phone.recv(4)
    header_byes_size = struct.unpack('i', header)[0]
    print(header_byes_size)
    header_byes = phone.recv(header_byes_size)
    print(header_byes)
    header_size = json.loads(header_byes.decode('utf-8'))['date_size']
    print(header_size)
    # header_size = header_dic['date_size']
    # print(header_size)
    tital_size = 0
    # date_len = b""

    while tital_size < header_size:
        # print(header_size, tital_size)
        date = phone.recv(1024)
        print(date.decode("utf-8"))
        tital_size += len(date)
        # date_len +=date

    # print(date_len.decode('utf-8'))
    # phone.close()
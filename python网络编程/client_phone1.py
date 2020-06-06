import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.connect(('127.0.0.1', 8080))

while True:
    user_input = input("请输入字符串：")
    phone.send(user_input.encode("utf-8"))
    date = phone.recv(1024)
    print(date)
    # phone.close()
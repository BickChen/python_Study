import socket
host = '192.168.10.12'
post = 8080

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.connect((host, post))

while True:
    user_input = input("请输入聊天信息：").strip()
    if len(user_input) == 0:continue
    phone.send(user_input.encode("utf-8"))
    print("发送成功！")
    date = phone.recv(1024)
    print(date.decode('utf-8'))
    # phone.close()
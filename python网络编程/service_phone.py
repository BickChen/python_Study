import socket
host = '0.0.0.0'
post = 8080
phone=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.bind((host, post))
phone.listen(5)

while True:
    print("starting----")
    conn, client_addr = phone.accept()
    while True:
        try:
            date = conn.recv(1024)
            print(date.decode("utf-8"))
            user_input = input("请输入聊天信息：")
            conn.send(user_input.encode('utf-8'))
        except ConnectionResetError:
            break
    conn.close()
    # phone.close()


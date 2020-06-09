import socket, struct, json, os

host_post = ('127.0.0.1', 8080)
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.connect(host_post)
file_position = r"D:\python_Study\python网络编程\client\download\\"

while True:
    user_input = input(">>>：").strip()
    if len(user_input) == 0:continue
    phone.send(user_input.encode("utf-8"))
    print("发送成功！")
    res, file_name = user_input.split()

    if res == 'get':
        header = phone.recv(4)
        header_byes_size = struct.unpack('i', header)[0]
        print(header_byes_size)
        header_byes = phone.recv(header_byes_size)
        print(header_byes)
        header_dic = json.loads(header_byes.decode('utf-8'))
        file_name = header_dic["filename"]
        header_size = header_dic["date_size"]
        print(header_size)

        tital_size = 0
        file_path = file_position + file_name
        file = open(file_path, 'wb')
        while tital_size < header_size:
            print(header_size, tital_size)
            date = phone.recv(1024)
            file.write(date)
            tital_size += len(date)
        file.close()
    elif res == 'push':
        file_path = file_position + file_name
        file = open(file_path, 'rb')

        header_data = {
            'filename': file_name,
            'date_size': os.path.getsize(file_path)
        }
        header_json = json.dumps(header_data)
        header_byes = header_json.encode('utf-8')
        header = struct.pack('i', len(header_byes))
        phone.send(header)
        phone.send(header_byes)

        for line in file:
            phone.send(line)
        file.close()
    else:
        print("您输入的不是一个正确的命令")

    # print(date_len.decode('utf-8'))
phone.close()
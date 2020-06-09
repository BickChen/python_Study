import socket, struct, json, os.path
# import subprocess
host_post = ('0.0.0.0', 8080)
phone=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.bind((host_post))
phone.listen(5)
file_position = r"D:\python_Study\python网络编程\service\file\\"

while True:
    print("starting----")
    conn, client_addr = phone.accept()
    print("发送端：", client_addr)
    while True:
        try:
            date = conn.recv(1024)
            res,file_name = date.decode('utf-8').split()
            file_path = file_position + file_name

            if res == 'get' and os.path.isfile(file_path):
                file = open(file_path, 'rb')

                header_data = {
                    'filename': file_name,
                    'date_size': os.path.getsize(file_path)
                }
                header_json = json.dumps(header_data)
                header_byes = header_json.encode('utf-8')
                header = struct.pack('i', len(header_byes))
                conn.send(header)
                conn.send(header_byes)

                for line in file:
                    conn.send(line)
                file.close()
            elif res == 'push':
                header = conn.recv(4)
                header_byes_size = struct.unpack('i', header)[0]
                print(header_byes_size)
                header_byes = conn.recv(header_byes_size)
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
                    date = conn.recv(1024)
                    file.write(date)
                    tital_size += len(date)
                file.close()


        except ConnectionResetError:
            break
        except ConnectionAbortedError:
            break
    conn.close()
    # phone.close()


import socket
import struct
import hashlib
import json
import os

class FtpClient(object):
    socket_region = socket.AF_INET
    socket_agree = socket.SOCK_STREAM
    host_post = ('127.0.0.1', 8080)
    coding = 'utf-8'
    header_bytes = 4
    receive_bytes = 1024
    user_status = 0
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    user_date_file = 'download'
    user_update_file = 'update'

    def __init__(self):
        self.socket = socket.socket(self.socket_region, self.socket_agree)
        self.socket.connect(self.host_post)
        self.md5_date = hashlib.md5()

    def run(self):
        print("连接服务器:",self.host_post)
        while True:
            if self.user_status == 0:
                self.user_login()
                if self.user_status == 1:
                    print('登陆成功！')
                else:
                    print('登陆失败！')
                    break
            elif self.user_status == 1:
                self.user_command()
                break
                # else:
                #     print('登陆成功！无需再次登陆！')
                #     break
        self.socket.close()

    def __header_send(self):
        user_date = json.dumps(self.user_date).encode(self.coding)
        date_len = struct.pack('i', len(user_date))
        self.socket.send(date_len)
        self.socket.send(user_date)

    def __header_receive(self):
        head_struct = self.socket.recv(self.header_bytes)
        head_len = struct.unpack('i', head_struct)[0]
        head_json = self.socket.recv(head_len).decode(self.coding)
        self.head_dic = json.loads(head_json)
        # print(self.head_dic)

    def user_login(self):
        username = input("请输入用户名：")
        password = input("请输入密码：")
        self.md5_date.update(password.encode(self.coding))
        password = self.md5_date.hexdigest()
        self.user_date = {'username': username, 'password': password}
        self.__header_send()
        print("发送成功")
        return_date = self.socket.recv(self.receive_bytes).decode(self.coding)
        print("接收成功")
        if return_date.isdigit():
            return_date = int(return_date)
            self.user_status = return_date
        else:
            print(return_date)

    def user_command(self):
        while True:
            try:
                user_input = input('>>>:')
                if not user_input: continue
                self.socket.send(user_input.encode('utf-8'))
                self.cmds = user_input.split()
                if hasattr(self, self.cmds[0]):
                    getattr(self, self.cmds[0])()
                else:
                    print('请重新输入')
            except Exception as e:  # server关闭了
                print(e)
                break

    def get(self):
        self.__header_receive()
        file_size = self.head_dic['file_size']
        file_name = os.path.join(self.base_dir, self.user_date_file, self.cmds[1])
        total = 0
        print(self.base_dir)
        print(file_name)
        with open(file_name, 'wb') as f:
            while total < file_size:
                recv_date = self.socket.recv(self.receive_bytes)
                f.write(recv_date)
                total += len(recv_date)
            print('传输完成，共传输：%d 字节'%total)

    def put(self):
        file_name = os.path.join(self.base_dir, self.user_update_file, self.cmds[1])
        print(file_name)
        print(os.path.exists(file_name))
        if os.path.exists(file_name):
            file_size = os.path.getsize(file_name)
            self.user_date = {'file_size': file_size}
            self.__header_send()
            file = open(file_name, 'rb')
            for line in file:
                self.socket.send(line)
            file.close()




FtpClient().run()
import socket
import struct
import json
from configparser import ConfigParser
import os
import subprocess

class FtpServer(object):
    socket_region = socket.AF_INET
    socket_agree = socket.SOCK_STREAM
    host_post = ('127.0.0.1', 8080)
    pending_num = 5
    receive_bytes = 1024
    header_bytes = 4
    coding = 'utf-8'
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    user_date_file = os.path.join(base_dir,'config','user_config')


    def __init__(self):
        self.socker = socket.socket(self.socket_region,self.socket_agree)
        self.socker.bind(self.host_post)
        self.socker.listen(self.pending_num)

    def connection(self):
        while True:
            print("----staring----")
            self.user_status = False
            self.conn, self.cilent_addr = self.socker.accept()
            print("客户端地址：",self.cilent_addr)
            try:
                while True:
                    if self.user_status is False:
                        self.user_auth()
                    else:
                        self.user_command()
            except Exception:
                continue

    def __header_receive(self):
        head_struct = self.conn.recv(self.header_bytes)
        head_len = struct.unpack('i', head_struct)[0]
        head_json = self.conn.recv(head_len).decode(self.coding)
        self.head_dic = json.loads(head_json)
        # print(self.head_dic)

    def __header_send(self):
        user_date = json.dumps(self.user_date).encode(self.coding)
        date_len = struct.pack('i', len(user_date))
        self.conn.send(date_len)
        self.conn.send(user_date)

    def user_auth(self):
        self.__header_receive()
        username = self.head_dic['username']
        password = self.head_dic['password']
        # print(username, password)
        conf = ConfigParser()
        conf.read(self.user_date_file.encode(self.coding))
        # print(conf.has_section(username))
        # print(conf.get(username, 'password'))
        if conf.has_section(username) and conf.get(username,'password') == password:
            print("登陆成功！")
            self.user_status = True
            self.user_home = conf.get(username, 'home')
            self.user_quota = conf.get(username, 'user_quota')
            # print(self.user_status)
            self.conn.send('1'.encode(self.coding))
            print("发送成功")
        else:
            self.conn.close()

    def user_command(self):
        self.cilent_cmd = self.conn.recv(self.receive_bytes).decode(self.coding).split()
        if hasattr(self, self.cilent_cmd[0]):
            getattr(self, self.cilent_cmd[0])()

    def get(self):
        file_name = self.user_home + self.cilent_cmd[1]
        print(file_name)
        print(os.path.exists(file_name))
        if os.path.exists(file_name):
            file_size = os.path.getsize(file_name)
            self.user_date = {'file_size': file_size}
            self.__header_send()
            file = open(file_name, 'rb')
            for line in file:
                self.conn.send(line)
            file.close()

    def put(self):
        file_name = self.user_home + self.cilent_cmd[1]
        print(file_name)
        self.__header_receive()
        file_size = self.head_dic['file_size']
        with open(file_name, 'wb') as f:
            total = 0
            while total < file_size:
                recv_date = self.conn.recv(self.receive_bytes)
                f.write(recv_date)
                total += len(recv_date)
            print('传输完成，共传输：%d 字节'%total)



    def ls(self):
        pass

    def mkdir(self):
        pass

    def cd(self):
        pass

    def remove(self):
        pass


FtpServer().connection()
import socket, struct, json, os.path
from configparser import ConfigParser


class HeaderDate(object):
    def __init__(self):
        pass


class UserAuth(object):

    user_date = r'D:\python_Study\python_ftp_project\ftp_server\config\user_config'
    user_state = False
    user_home = r''
    user_quota = ''

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def user_login(self):
        if not self.user_state:
            get_data = ConfigParser()
            get_data.read(self.user_date.encode('utf-8'))
            # print(self.password)
            if get_data.has_section(self.name) and get_data.get(self.name, 'password') == self.password:
                print('登陆成功！')
                user_state = True
                user_home = get_data.get(self.name, 'home')
                user_quota = get_data.get(self.name, 'user_quota')
                # print(self.user_home)
                # print(self.user_quota)
            else:
                print('登陆失败！')
        else:
            print('登陆成功,无需重新登陆')


class FtpService(object):
    user = UserAuth
    header_date = HeaderDate

    def __init__(self):
        pass


host_post = ('0.0.0.0', 8080)
connect = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect.bind(host_post)
connect.listen(5)

while True:
    print("starting----")
    conn, client_addr = connect.accept()
    if not UserAuth.user_state:
        user_dic = {'username': '', 'password': ''}
        for i in user_dic:
            print(i)
            date = conn.recv(1024)
            user_dic[i] = date.decode('utf-8')
        print(user_dic)
        f = UserAuth(user_dic['username'], user_dic['password'])
        f.user_login()





import socket,struct,json, os.path
from configparser import ConfigParser


def user_login(func, self):
    def innfo(args):
        if not self.user_state:
            self.conn.send('请输入用户名：'.encode(self.coding))
            user_name = self.conn.recv(self.max_packet_size).decode(self.coding)
            self.conn.send('请输入密码：'.encode(self.coding))
            user_passwd = self.conn.recv(self.max_packet_size).decode(self.coding)
            get_data = ConfigParser()
            get_data.read(self.user_date.encode(self.coding))
            if get_data.has_section(user_name) and get_data.get(user_name, 'password') == user_passwd:
                self.conn.send('登陆成功'.encode(self.coding))
                self.user_state = True
                self.user_home = get_data.get(user_name, 'home')
                self.user_quota = get_data.get(user_name, 'user_quota')
                func(args)
            else:
                self.conn.send('登陆失败'.encode(self.coding))
        else:
            func(args)

    return innfo


class MYTCPServer:

    address_family = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    allow_reuse_address = False
    max_packet_size = 8192
    coding='utf-8'
    request_queue_size = 5
    server_dir = 'config'
    user_date = r'D:\python_Study\python_ftp_project\ftp_server\config\user_config'
    user_state = False
    user_home = r''
    user_quota = ''

    def __init__(self, server_address, bind_and_activate=True):
        """Constructor.  May be extended, do not override."""
        self.server_address=server_address
        self.socket = socket.socket(self.address_family,
                                    self.socket_type)
        if bind_and_activate:
            try:
                self.server_bind()
                self.server_activate()
            except:
                self.server_close()
                raise

    def server_bind(self):
        """Called by constructor to bind the socket.
        """
        if self.allow_reuse_address:
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(self.server_address)
        self.server_address = self.socket.getsockname()

    def server_activate(self):
        """Called by constructor to activate the server.
        """
        self.socket.listen(self.request_queue_size)

    def server_close(self):
        """Called to clean-up the server.
        """
        self.socket.close()

    def get_request(self):
        """Get the request and client address from the socket.
        """
        return self.socket.accept()

    def close_request(self, request):
        """Called to clean up an individual request."""
        request.close()

    def run(self):
        while True:
            self.conn,self.client_addr=self.get_request()
            print('from client ',self.client_addr)
            while True:
                try:
                    head_struct = self.conn.recv(4)
                    if not head_struct:break
                    head_len = struct.unpack('i', head_struct)[0]
                    head_json = self.conn.recv(head_len).decode(self.coding)
                    head_dic = json.loads(head_json)
                    print(head_dic)
                    #head_dic={'cmd':'put','filename':'a.txt','filesize':123123}
                    cmd=head_dic['cmd']
                    if hasattr(self,cmd):
                        func=getattr(self,cmd)
                        func(head_dic)
                except Exception:
                    break


    #@user_login(self)
    def put(self,args):
        file_path=os.path.normpath(os.path.join(
            self.server_dir,
            args['filename']
        ))
        filesize=args['filesize']
        recv_size=0
        print('----->',file_path)
        with open(file_path,'wb') as f:
            while recv_size < filesize:
                recv_data=self.conn.recv(self.max_packet_size)
                f.write(recv_data)
                recv_size+=len(recv_data)
                print('recvsize:%s filesize:%s' %(recv_size,filesize))

    def get(self,args):
        file_path=os.path.normpath(os.path.join(
            self.server_dir,
            args['filename']
        ))
        print(file_path)
        if not os.path.isfile(file_path):
            print('file:%s is not exists' %file_path)
            return
        else:
            filesize=os.path.getsize(file_path)
        head_dic={'filename':os.path.basename(file_path),'filesize':filesize}
        print(head_dic)
        head_json=json.dumps(head_dic)
        head_json_bytes=bytes(head_json,encoding=self.coding)
        head_struct=struct.pack('i',len(head_json_bytes))
        self.socket.send(head_struct)
        self.socket.send(head_json_bytes)
        send_size=0
        with open(file_path,'rb') as f:
            for line in f:
                self.socket.send(line)
                send_size+=len(line)
                send_percentage = send_size / filesize
                print('%.2f%%' %(send_percentage * 100))
            else:
                print('upload successful')







tcpserver1 = MYTCPServer(('127.0.0.1',8080))
tcpserver1.run()



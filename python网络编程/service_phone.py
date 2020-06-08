import socket
import subprocess
import struct
import json
host_post = ('0.0.0.0', 8080)
phone=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.bind((host_post))
phone.listen(5)

while True:
    """
    等待接受客户端数据
    """
    print("starting----")
    conn, client_addr = phone.accept()
    print("发送端：", client_addr)   #接受客户端数据后打印客户端的IP地址和端口信息
    while True:
        try:
            #接收客户端发送的命令，并执行命令，返回的结果存放到subprocess管道中，stdout为标准输出，stderr为错误输出
            date = conn.recv(1024)
            res = subprocess.Popen(date.decode("utf-8"), shell=True,
                               stdout=subprocess.PIPE,
                               stdin=subprocess.PIPE,
                               stderr=subprocess.PIPE)
            #第一步，获取命令执行结果
            stdout = res.stdout.read()
            stderr = res.stderr.read()
            #第二步，制作应用程序固定header头信息
            header_data = {
                'filename':'test',
                'date_size': len(stdout) + len(stderr)
            }                                       #制作header信息字典
            header_json = json.dumps(header_data)   #将header字典转换为json格式
            header_byes = header_json.encode('utf-8')   #将json格式的数据编译为bytes类型
            header = struct.pack('i', len(header_byes)) #计算header数据bytes类型的长度，并将长度打包为bytes数据包
            #第三步，将header头的bytes长度信息和header头的数据传输给客户端，以便客户端获取header信息
            conn.send(header)                          #将header数据的bytes长度传输给客户端
            conn.send(header_byes)                     #将header数据传输给客户端
            # conn.send(res.stdin.read())
            #第四步，传输命令执行结果
            conn.send(stdout)
            conn.send(stderr)
        except ConnectionResetError:
            break
        except ConnectionAbortedError:
            break
    conn.close()
    # phone.close()


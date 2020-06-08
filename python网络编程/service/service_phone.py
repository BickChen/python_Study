import socket
import subprocess
import struct
import json
host_post = ('0.0.0.0', 8080)
phone=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.bind((host_post))
phone.listen(5)

while True:
    print("starting----")
    conn, client_addr = phone.accept()
    print("发送端：", client_addr)
    while True:
        try:
            date = conn.recv(1024)

            res = subprocess.Popen(date.decode("utf-8"), shell=True,
                               stdout=subprocess.PIPE,
                               stdin=subprocess.PIPE,
                               stderr=subprocess.PIPE)
            stdout = res.stdout.read()
            stderr = res.stderr.read()
            header_data = {
                'filename':'test',
                'date_size': len(stdout) + len(stderr)
            }
            header_json = json.dumps(header_data)
            header_byes = header_json.encode('utf-8')
            header = struct.pack('i', len(header_byes))
            conn.send(header)
            conn.send(header_byes)
            # conn.send(res.stdin.read())
            conn.send(stdout)
            conn.send(stderr)
        except ConnectionResetError:
            break
        except ConnectionAbortedError:
            break
    conn.close()
    # phone.close()


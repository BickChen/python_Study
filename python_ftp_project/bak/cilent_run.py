import socket, struct, json, os

host_post = ('127.0.0.1', 8080)
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.connect(host_post)

user_date = ['username:', 'password']
for i in user_date:
    user_input = input(i)
    phone.send(user_input.encode('utf-8'))

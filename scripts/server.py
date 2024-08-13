import socket

host = '192.168.5.104'
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host, 8080))
socket.listen(1)
connection, address = socket.accept()

while True:
    buffer = connection.recv(1024)
    if len(buffer) > 0:
        print(buffer)


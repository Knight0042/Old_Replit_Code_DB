import socket
import sys
from _thread import *

server = "192.168.1.94"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    print(str(e))

s.listen(2)
print('Waiting for connection server started...')


def threadded_client(conn):
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")
            if not data:
                print('disconnected')
                break
            else:
                print("Recieved: ", reply)
                print('Sending: ', reply)
            conn.sendall(str.encode(reply))
        except:
            break


while True:
    conn, addr = s.accept()
    print(f'Connected to {addr}')

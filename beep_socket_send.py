#!/usr/bin/env python3

import socket
import os 

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = int( os.environ[ 'BEEP_SOCKET_SEND_PORT' ] )       # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'beep')
    # data = s.recv(1024)

print('Received', repr(data))
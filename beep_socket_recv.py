#!/usr/bin/env python3

import socket
import os 
import time 


HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = int( os.environ[ 'BEEP_SOCKET_RECV_PORT' ] )     


BEEP_SCRIPT = print(os.path.dirname(os.path.realpath(__file__))) + '/beep.sh'



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        
        print('Connected by', addr)
        
        while True:
        
            data = conn.recv(1024)

            print( data )

            if data == 'beep' : 
                os.system( BEEP_SCRIPT )
        
            if not data:
                time.sleep(1)
        
            conn.sendall(data)
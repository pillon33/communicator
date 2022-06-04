#!/usr/bin/env python3

import socket
from time import sleep

#socket.setblocking(false)

HOST = ''  # The server's hostname or IP address
PORT = 65432        # The port used by the server

header_len = 8

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.settimeout(1)
    while True:
        msg = input("<You> ")
        msg = msg.encode()
        if msg != b'':
            s.send(msg)
        while True:
            try:
                header = s.recv(header_len)
                msg_len = int(header)
                msg = s.recv(msg_len)      #receiving messages from server
            except:
                break
            print(msg)

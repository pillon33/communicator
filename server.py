#!/usr/bin/env python3

import socket

HOST_RECV = ''  # Standard loopback interface address (localhost)
PORT_RECV = 65432        # Port to listen on (non-privileged ports are > 1023)

header_len = 8

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s1:
    s1.bind((HOST_RECV, PORT_RECV))
    s1.listen()
    conn, addr = s1.accept()
    conn.settimeout(0.1)
    msg = []
    
    conn2, addr2 = s1.accept()
    conn2.settimeout(0.1)
    msg2 = []
        
    while True:
        while True:
            try:
                rec = conn.recv(1024)
                msg.append(rec) #try to receive from pc1
            except:
                break
        while True:
            try:
                rec = conn2.recv(1024)
                msg2.append(rec) #try to receive from pc2
            except:
                break
                    
                    
        if len(msg):    
            to_send = msg.pop(0)    #get the message to send
            to_send = f'<{addr[0]}> {str(to_send)[2:-1]}'
            header = f'{len(to_send)}'
            while len(header) < header_len:
                header = '0' + header
            try:
                conn2.send(f'{header}{to_send}'.encode())  #try to send message to pc2
                print(f'sent: {header}{to_send}')
            except Exception as e:
                continue
            
        if len(msg2):
            to_send = msg2.pop(0)  #get the message to send
            to_send = f'<{addr[0]}> {str(to_send)[2:-1]}'
            header = f'{len(to_send)}'
            while len(header) < header_len:
                header = '0' + header
            try:
                conn.send(f'{header}{to_send}'.encode())   #try to send message to pc1
                print(f'sent: {header}{to_send}')
            except Exception as e:
                continue
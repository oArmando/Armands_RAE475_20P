#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 15:08:12 2020

@author: armands
"""
import socket
HEADERSIZE = 10 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #define socket paramters
s.connect((socket.gethostname(),9090)) #define host and port

while True:
    
    full_msg = ''
    new_msg = True
    while True:
        msg = s.recv(16)
        if new_msg: #define mesagelength block
            print(f"new message length: {msg[:HEADERSIZE]}")
            msglen = int(msg[:HEADERSIZE])
            new_msg = False
    
        full_msg += msg.decode("utf-8")
    
     
        if len(full_msg)-HEADERSIZE == msglen:
            print("full msg recvd")#print that all is recieved
            print(full_msg[HEADERSIZE:])#print message
            new_msg = True
            full_msg = ''
   
    
        print(full_msg)

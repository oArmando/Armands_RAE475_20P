#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 13:52:27 2020

@author: armands
"""
import socket
import time

HEADERSIZE = 10 #set headersize
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#set TCP socket parameters
s.bind((socket.gethostname(),9090))#set host and port
s.listen(5)#set to listenint

while True:
    clientsocket, address = s.accept()
    print(f"Connection form {address} has been established!")#show in server.py connection
    
    msg = "Welcome to the server!" #send welcome message
    msg= f'{len(msg):<{HEADERSIZE}}' +msg
    
    clientsocket.send(bytes(msg,"utf-8"))
    
    while True:#send time module
        time.sleep(3)
        msg = f"The time is {time.time()}"
        msg= f'{len(msg):<{HEADERSIZE}}' +msg
        clientsocket.send(bytes(msg,"utf-8"))
    
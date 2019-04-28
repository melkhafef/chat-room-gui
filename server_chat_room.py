# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 14:48:33 2019

@author: melkhafef
"""

from socket import *
from threading import Thread
import _thread
def sendMessageToAll(message,sender):
    for client in sessions :
        if client != sender :
            client.send(message.encode('utf-8'))
def sendMessageJoin(message):
    for client in sessions :
            client.send(message.encode('utf-8'))
def connectNewUser(session_num,addr):
     ip_client=addr[0]
     port_client=addr[1]
     sendMessageJoin("{}{} join to chat\n".format(addr[0],addr[1]))
     while True :
        m=session_num.recv(2048)
        m='{}.{}:{}'.format(addr[0],addr[1],m.decode('utf-8'))
        sendMessageToAll(m,session_num)
try:
    s=socket(AF_INET,SOCK_STREAM)
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    host="127.0.0.1"
    port=8000
    s.bind((host,port))
    s.listen(10)
    sessions=[]
    while True :
        session_num,addr=s.accept()
        sessions.append(session_num)
        _thread.start_new_thread(connectNewUser,(session_num,addr))
except error as e :
    print(e)
except KeyboardInterrupt :
    print("Ok")
    s.close()


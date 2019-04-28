# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 11:18:01 2019

@author: CSE
"""
from tkinter import *
from tkinter import messagebox
from socket import *
import _thread
import random
s=socket(AF_INET,SOCK_STREAM)
host="127.0.0.1"
port=8000
s.connect((host,port))
wind = Tk()
wind.title('client')
wind.geometry('500x500')
wind.configure(background='#2e59d1')
entryText = StringVar()
en=Entry(wind,width=100,textvariable=entryText)
en.grid(column=1,row=1)
btn=Button(wind,width=3,height=1,text="send")
btn.grid(column=1,row=2)
r=3
bgcolorR='#'
fgcolorR='#'
bgcolorMe='#'
fgcolorMe='#'
fgvalues=['8','9','a','b','c','d','e','f']
bgvalues=['0','1','2','3','4','5','6','7']
for i in range(6):
    bgcolorMe+=random.choice(bgvalues)
    fgcolorMe+=random.choice(fgvalues)
def rec():
    global r,s,lab,color,bgcolorR,fgcolorR
    for i in range(6):
        bgcolorR+=random.choice(bgvalues)
        fgcolorR+=random.choice(fgvalues)
    while True:
        w=s.recv(2048)
        Button(wind,text=w.decode('utf-8'),bd=5,relief=FLAT,bg=bgcolorR,fg=fgcolorR,padx=5,pady=5,wraplength=500,width=80).grid(column=1,row=r)  
        r=r+1
_thread.start_new_thread(rec,())
def clicked():
    global r,s,lab,entryText
    s.send((en.get()).encode('utf-8'))
    x='I : {}'.format(en.get())
    Button(wind,text=x,bd=5,relief=FLAT,bg=bgcolorMe,fg=fgcolorMe,padx=5,pady=5,wraplength=500,width=80).grid(column=1,row=r)  
    entryText.set("")
    r=r+1
btn["command"]=clicked
wind.mainloop()


import socket
import threading
import base64
import time
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("https://git.heroku.com/mysterious-plateau-17836.git",3000))
s.listen(100000000)
k=[]
p=[]
l=1
def acceptor():

    clt,adr=s.accept()
    k.append(clt)
    p.append(adr) 
    l=1

while True:
    if l==1:
        l=0
        threading.Thread(target=acceptor).start()
    s=input('')
    s.encode('utf-8')
    with open(f'{s}','rb') as imagefile:
        byteform=base64.b64encode(imagefile.read())
        

    for a in k:
        
        a.send(s.encode())
        
        time.sleep(2)
        a.send(byteform)






















''''import tkinter
from tkinter import *


root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )

mylist = Listbox(root, yscrollcommand = scrollbar.set )
for line in range(100):
   mylist.insert(END, "This is line number " + str(line))

mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )

mainloop()



import tkinter
from tkinter import *
root=Tk()
frame=Frame(root,width=300,height=300)
frame.pack(expand=True, fill=BOTH) #.grid(row=0,column=0)
canvas=Canvas(frame,bg='#FFFFFF',width=300,height=300,scrollregion=(0,0,500,500))
lb=Label(canvas,text="qwerty")
lb.grid(row=0,column=0)
hbar=Scrollbar(frame,orient=HORIZONTAL)
hbar.pack(side=BOTTOM,fill=X)
hbar.config(command=canvas.xview)
vbar=Scrollbar(frame,orient=VERTICAL)
vbar.pack(side=RIGHT,fill=Y)
vbar.config(command=canvas.yview)

canvas.config(width=300,height=300)
canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
canvas.pack(side=LEFT,expand=True,fill=BOTH)
root.mainloop()
'''

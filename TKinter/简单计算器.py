from tkinter import *

master = Tk()

v1 = StringVar()
v2 = StringVar()
v3 = StringVar()

def test(content):
    return content.isdigit()
testCMD = master.register(test)
e1 = Entry(master, textvariable=v1, validate="key", validatecommand=(testCMD, '%P'))\
    .grid(row=0,column=0)
Label(master,text='+').grid(row=0,column=1)
e2 = Entry(master, textvariable=v2, validate="key", validatecommand=(testCMD, '%P'))\
    .grid(row=0,column=2)
Label(master,text='=').grid(row=0,column=3)
e3 = Entry(master, textvariable=v3, state='readonly').grid(row=0,column=4)
def calc():

    result=int(v1.get())+int(v2.get())
    v3.set(result)
Button(master,text="计算结果",command=calc).grid(row=1,column=2)

mainloop()
from tkinter import *
master=Tk()
def test():
    if e1.get()=='小甲鱼':
        print("正确")
        return True
    else:
        print("错误!")
        #清空
        e1.delete(0,END)
        return False
def test2():
    print("我被调用了")

v=StringVar()
#invalidcommand 当validatecommand返回False时调用
e1=Entry(master,textvariable=v,validate='focusout',validatecommand=test,invalidcommand=test2)
e2=Entry(master)
e1.pack(padx=10,pady=10)
e2.pack(padx=10,pady=10)
mainloop()
from tkinter import *
root=Tk()
variable=StringVar()
variable.set('one')
#一种类似组合框的菜单类型
w=OptionMenu(root,variable,'one','two','three')
w.pack()
mainloop()

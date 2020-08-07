from tkinter import *
import hashlib
root=Tk()
#undo开启撤销功能
#autoseparators 关闭自动分段,就是撤销的分割符
text=Text(root,width=30,height=5,undo=True,autoseparators=False)
text.pack()
text.insert(INSERT,"I love FishC.com")
def callback(event):
    #插入撤销分隔符
    text.edit_separator()
text.bind('<Key>',callback)
def show():
    text.edit_undo()
Button(root,text='撤销',command=show).pack()

mainloop()
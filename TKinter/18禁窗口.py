from tkinter import *
import io
from PIL import Image, ImageTk
def say():
    var.set("吹吧你,我不信你")

root=Tk()
f1=Frame(root)
f2=Frame(root)
f1.pack()
f2.pack()
root.title='18禁'
var=StringVar()
var.set('您所下载的影片含有未成年人限制内容\n请满18岁后再点击观看')
textlabel=Label(f1,
                textvariable=var,
                justify=LEFT,
                padx=10)
textlabel.pack(side=LEFT)

photo=PhotoImage(file=r'C:\Users\Administrator\Desktop\pkq.gif')
imgLabel=Label(f1,image=photo)
imgLabel.pack(side=RIGHT)


b=Button(f2,text='我已满18岁',command=say)
b.pack(side=LEFT)


mainloop()

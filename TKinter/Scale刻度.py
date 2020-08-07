from tkinter import *
root=Tk()
#tickinterval 每x显示一个刻度 resolution就是一格-多少,默认是1 精度
s1=Scale(root,from_=0,to=42,tickinterval=10,resolution=5)
s1.pack()
s2=Scale(root,from_=0,to=200,orient=HORIZONTAL)
s2.pack()


def show():
    print(s1.get(),s2.get())
Button(root,text='获取位置',command=show).pack()
mainloop()
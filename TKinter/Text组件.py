from tkinter import *
root=Tk()
#width一行多少个字,,height多少行
text=Text(root,width=60,height=60)
text.pack()
text.insert(INSERT,'i love \n')
text.insert(INSERT,'baidu.com')
photo=PhotoImage(file=r"C:\Users\Administrator\Desktop\timg.gif")
def show():
    print("我被点了一下")
    text.image_create(INSERT,image=photo)

b1=Button(text,text='点我点我 ',command=show)
#也可以插入组件
text.window_create(INSERT,window=b1)

mainloop()

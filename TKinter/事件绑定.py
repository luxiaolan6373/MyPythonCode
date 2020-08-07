from tkinter import*
root=Tk()
def callback(event):
    print('点击位置',event.x,event.y)
def keyback(event):
    print(event.char)
def Motionback(event):
    print('当前位置',event.x,event.y)
frame=Frame(root,width=200,height=200)
frame.bind('<Button-1>',callback)
frame.bind('<Motion>',Motionback)
frame.bind('<Key>',keyback)
frame.focus_set()
frame.pack()

mainloop()
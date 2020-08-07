from tkinter import*


root=Tk()
f=Frame(root,padx=10,pady=10)
f.pack()
#row,column 表格坐标
l1=Label(f,text='作品:').grid(row=0,column=0)
l2=Label(f,text='作者:').grid(row=1,column=0)
v1=StringVar()
v2=StringVar()

e1=Entry(f,textvariable=v1)
e1.grid(row=0,column=1,padx=10,pady=5)
e1.get()#这可以调用
#show 相当于密码字符替换
e2=Entry(f,textvariable=v2,show='*')
e2.grid(row=1,column=1,padx=10,pady=5)
e2.get()

def getmsg():
    #也可以用e1.get()
    print('作品:《%s》'% v1.get())
    print('作者:%s' % v2.get())
#sticky 靠左靠右
b1=Button(f,text='获取信息',command=getmsg)\
    .grid(row=2,column=0,sticky=W,padx=10,pady=5)
b2=Button(f,text='退出',command=root.quit)\
    .grid(row=2,column=1,sticky=E,padx=10,pady=5)
mainloop()
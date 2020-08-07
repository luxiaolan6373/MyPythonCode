from tkinter import *
root=Tk()
#表格布局器 sticky=W 左对齐
Label(root,text='用户名').grid(row=0,column=0,sticky=W)
Label(root,text='密码').grid(row=1,column=0,sticky=W)

Entry(root,text='用户名').grid(row=0,column=1)
Entry(root,text='密码',show="*").grid(row=1,column=1)

photo=PhotoImage(fil=r'C:\Users\Administrator\Desktop\pkq.gif')
#rowspan表示占用2行
Label(root,image=photo).grid(row=0,column=2,rowspan=2)


mainloop()
from tkinter import *
root=Tk()
group=LabelFrame(root,text="最好的脚本语言是?",padx=5,pady=5)
group.pack(padx=10,pady=10)
LANGS=[('Python',1),
       ('Per1',2),
       ('Ruby',3),
       ('Lua',4)]
v=IntVar()
for lang, num in LANGS:
    #indicatoronu设置样式,,可以是单选框 ,也可以是按钮
    b=Radiobutton(group,text=lang,variable=v,value=num,indicatoron=False)
    #填充
    b.pack(fill=X)

mainloop()
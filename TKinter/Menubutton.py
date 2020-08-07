from tkinter import *

root = Tk()


def callback():
    print('你好')

#创建一个菜单对象
mb = Menubutton(root,text='点我',relief=RAISED)
mb.pack()

#窗口的菜单绑定

#绑定这个菜单的子菜单
filemenu=Menu(mb,tearoff=False)

#设置子菜单
filemenu.add_command(label='打开', command=callback)
filemenu.add_command(label='保存', command=callback)
filemenu.add_separator()#分割线
filemenu.add_command(label='退出', command=root.quit)
#最好把主菜单的标题显示,然后绑定
mb.config(menu=filemenu)



mainloop()
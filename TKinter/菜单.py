from tkinter import *

root = Tk()


def callback():
    print('你好')

#创建一个菜单对象
menubar = Menu(root)
#窗口的菜单绑定
root.config(menu=menubar)
#绑定这个菜单的子菜单
filemenu=Menu(menubar,tearoff=False)
#设置子菜单
filemenu.add_command(label='打开', command=callback)
filemenu.add_command(label='保存', command=callback)
filemenu.add_separator()#分割线
filemenu.add_command(label='退出', command=root.quit)
#最好把主菜单的标题显示,然后绑定
menubar.add_cascade(label='文件',menu=filemenu)

#绑定这个菜单的子菜单
editmenu=Menu(menubar,tearoff=False)
#设置子菜单
editmenu.add_command(label='剪切', command=callback)
editmenu.add_command(label='拷贝', command=callback)
editmenu.add_command(label='粘贴', command=root.quit)
#最好把主菜单的标题显示,然后绑定
menubar.add_cascade(label='编辑',menu=editmenu)


mainloop()

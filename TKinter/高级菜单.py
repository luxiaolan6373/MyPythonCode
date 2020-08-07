from tkinter import *

root = Tk()


def callback():
    print('你好')

#创建一个菜单对象
menubar = Menu(root)
openVar=IntVar()
saveVar=IntVar()
quitVar=IntVar()

#窗口的菜单绑定
root.config(menu=menubar)
#绑定这个菜单的子菜单
filemenu=Menu(menubar,tearoff=False)
#设置子菜单
filemenu.add_checkbutton(label='打开', command=callback,variable=openVar)
filemenu.add_checkbutton(label='保存', command=callback,variable=saveVar)
filemenu.add_separator()#分割线
filemenu.add_checkbutton(label='退出', command=root.quit,variable=quitVar)
#最好把主菜单的标题显示,然后绑定
menubar.add_cascade(label='文件',menu=filemenu)

editVar=IntVar()
#绑定这个菜单的子菜单
editmenu=Menu(menubar,tearoff=False)
#设置子菜单
editmenu.add_radiobutton(label='剪切', command=callback,variable=editVar,value=1)
editmenu.add_radiobutton(label='拷贝', command=callback,variable=editVar,value=2)
editmenu.add_radiobutton(label='粘贴', command=root.quit,variable=editVar,value=3)
#最好把主菜单的标题显示,然后绑定
menubar.add_cascade(label='编辑',menu=editmenu)


mainloop()

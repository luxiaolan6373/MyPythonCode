from tkinter import *
OPTIOWS=[
    'California',
    '458',
    'FF',
    'ENZO',
    'LaFerrari'
]
root=Tk()
variable=StringVar()
#设置默认的选中项
variable.set(OPTIOWS[0])
#一种类似组合框的菜单类型
#参数中*代表解包 序列  **代表解包字典
w=OptionMenu(root,variable,*OPTIOWS)
w.pack()
mainloop()

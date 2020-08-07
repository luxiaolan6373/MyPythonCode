from tkinter import *
master=Tk()
f=Frame(master)
f.pack()
#滚动条
sb=Scrollbar(f)
#靠右,并且Y轴无限填充
sb.pack(side=RIGHT,fill=Y)
#Listbox 组件根据 selectmode 选项提供了四种不同的选择模式：SINGLE（单选）、BROWSE（也是单选，但拖动鼠标或通过方向键可以直接改变选项）、MULTIPLE（多选）和 EXTENDED（也是多选，但需要同时按住 Shift 键或 Ctrl 键或拖拽鼠标实现）。默认是 BROWSE。
#height默认10  显示多少行
#yscrollcommand绑定滚动条  第一个字母x y表示方向
theLB=Listbox(f,selectmode=EXTENDED,height=10,yscrollcommand=sb)
theLB.pack()
#绑定方法
sb.config(command=theLB.yview)
for item in range(110):
    theLB.insert(END,item)

#删除delete
#ACTIVE当前选择项
thenButton=Button(master,text="删除它",
                  command=lambda x=theLB:x.delete(ACTIVE)).pack(side=BOTTOM)

mainloop()
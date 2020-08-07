from tkinter import *
root=Tk()
text=Text(root,width=30,height=5)
text.pack()
text.insert(INSERT,"I love FishC.com")
#选中范围,然后设置样式
text.tag_add('tag1','1.7','1.12','1.14')
text.tag_config('tag1',background='yellow',foreground='red')
text.tag_config('tag2',background='blue')
#提高它的优先级
#text.tag_raise('tag2')
#降低它的优先级
#text.tag_lower('tag2')



mainloop()
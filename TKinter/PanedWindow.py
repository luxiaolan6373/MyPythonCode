from tkinter import*
root=Tk()
#,,这个相当于表格布局
m1=PanedWindow(root,showhandle=True,sashrelief=SUNKEN)
m1.pack(fill=BOTH,expand=1)

left=Label(m1,text="left pane")
m1.add(left)

m2=PanedWindow(root,orient=VERTICAL,showhandle=True,sashrelief=SUNKEN)
m1.add(m2)

top=Label(m2,text='top pane')
m2.add(top)
buttom=Label(m2,text='bottom pan')
m2.add(buttom)
mainloop()
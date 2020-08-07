from tkinter import*
root=Tk()
listbox=Listbox(root)
#expand 自动填充补满父组件
listbox.pack(fill=BOTH,expand=True)
for i in range(20):
    listbox.insert(END,str(i))
mainloop()
import tkinter as tk
class APP:
    def __init__(self,master):
        frame=tk.Frame(master)
        #默认最上边 LEFT RIGHT TOP BUTTOM
        frame.pack(side=tk.LEFT)

        self.hi_there=tk.Button(frame,text='打招呼',bg='black',fg='blue',command=self.say_hi)
        self.hi_there.pack()
    def say_hi(self):
        print('大家好!更大更尴尬的时光')


root=tk.Tk()
app=APP(root)
root.mainloop()


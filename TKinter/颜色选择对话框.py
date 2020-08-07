from tkinter import *
from tkinter import colorchooser
root = Tk()

def callback():
    fileName = colorchooser.askcolor()
    print(fileName)

Button(root, text="选择颜色", command=callback).pack()

mainloop()
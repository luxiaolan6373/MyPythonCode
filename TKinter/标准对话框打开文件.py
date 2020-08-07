from tkinter import *
from tkinter import filedialog
root = Tk()

def callback():
    fileName = filedialog.askopenfilename(filetypes=[("PNG", ".png"), ("JPG", ".jpg"), ("GIF", ".gif")])
    print(fileName)

Button(root, text="打开文件", command=callback).pack()

mainloop()
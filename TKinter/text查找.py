from tkinter import *
import hashlib
root=Tk()
text=Text(root,width=30,height=5)
text.pack()
text.insert(INSERT,"I love FishC.com")
def getIndex(text):
    return tuple(map(int,str.split(text,'.')))
start='1.0'
while True:
    pos=text.search('o',start,stopindex=END)
    if not pos:#没有找到就到循环尾
        break

    print('找到了,位置是:',getIndex(pos))
    start=pos+'+1c'

mainloop()
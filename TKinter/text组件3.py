from tkinter import *
import webbrowser
root=Tk()
text=Text(root,width=30,height=5)
text.pack()
text.insert(INSERT,"I love FishC.com")
#选中范围,然后设置样式
text.tag_add('link','1.7','1.16')
text.tag_config('link',foreground='blue',underline=True)
def show_hand_cursor(event):
    text.config(cursor='arrow')
def show_xterm_cursor(event):
    text.config(cursor='xterm')
def click(event):
    webbrowser.open('https://www.v2ex.com/t/470233')
text.tag_bind('link','<Enter>',show_hand_cursor)
text.tag_bind('link','<Leave>',show_xterm_cursor)
text.tag_bind('link','<Button-1>',click)

mainloop()
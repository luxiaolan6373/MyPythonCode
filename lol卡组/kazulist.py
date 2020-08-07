
from tkinter import *
from tkinter import ttk
from strategy import Strategy
class KaZuList():
    def __init__(self,list,chess,equip,job,race,height):
        self.list=list
        self.chess = chess
        self.equip = equip
        self.job = job
        self.race = race
        self.root = Toplevel()
        self.root.title('python获取卡组演示')
        self.root.wm_attributes('-topmost', 1)
        self.root.overrideredirect(True)
        self.root.geometry(f'+{0}+{height}')
    def trefun(self,event):
        curItem = self.tree.focus()

        line_id=self.tree.item(curItem)['text']
        Hid = Strategy(line_id, self.chess, self.equip, self.job, self.race,self.root.winfo_width())
        Hid.show()
    def show(self):
        titles = ('评级', '标题')
        self.scrollbar = Scrollbar(self.root)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.tree = ttk.Treeview(self.root, column=titles, yscrollcommand=self.scrollbar.set,show='headings',)
        self.tree.bind('<<TreeviewSelect>>',self.trefun)

        #表示列,作为索引,不显示
        self.tree.column('评级',width=50,anchor='center')
        self.tree.column('标题',width=250,anchor='center')

        self.tree.heading('评级',text='评级')#显示表头
        self.tree.heading('标题', text='标题(官方卡组)')  # 显示表头
        i=0
        for item in self.list:
            #插入
            self.tree.insert('',END,text=item['line_id'],values=(item['quality'],item['line_name']))
            i+=1
        #绑定
        self.scrollbar.config(command=self.tree.yview)
        self.tree.pack()
        self.root.mainloop()













'''
#get图片的尺寸
w,h = pil_image.size
#取文件名
fname = url.split('/')[-1]
#按格式显示
sf = "{} ({}x{})".format(fname,w,h)
#设置标题
root.title(sf)
'''


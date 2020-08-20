from tkinter import ttk
from tkinter import *
import requests
import threading
import io
from PIL import Image, ImageTk
from 大型单机游戏.gamedownload import GameDown

class GameUI():
    def __init__(self):
        self.root = Tk()
        self.root.title("大型游戏下载")
        self.var = StringVar()
        self.var_xunlei = StringVar()
        self.var_baidu = StringVar()
        self.var_zhongzi = StringVar()
    #显示所有组件
    def show(self):
        # gd.get_games_Down_Url(gameid[0]['url'])
        self.show_button()
        self.show_download()
        self.show_img()
        self.root.mainloop()
    #列表绑定事件,点击响应
    def trefun(self, event):
        curItem = self.tree.focus()
        line_id = int(self.tree.item(curItem)['text'])
        global games, gd
        print(games[line_id]['url'])
        downs = gd.get_games_Down_Url(games[line_id]['url'])
        print(downs['xunlei'])
        self.var_xunlei.set(downs['xunlei'])
        self.var_baidu.set(downs['baidu'])
        self.var_zhongzi.set(downs['zhongzi'])
        self.img=self.get_img(games[line_id]['img'])
        self.imglb.config(image=self.img)
    # 创建一个列表tree
    def londlist(self):
        fm = Frame(self.root)
        fm.grid(row=0, column=0)
        titles = ('GameName', 'Score', "Type", "Label", 'Data')
        self.scrollbar = Scrollbar(fm)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.tree = ttk.Treeview(fm, column=titles, yscrollcommand=self.scrollbar.set, show='headings', height=20)
        self.tree.bind('<<TreeviewSelect>>', self.trefun)
        # 表示列,作为索引,不显示 只是设置列的一些属性
        self.tree.column('GameName', width=300, anchor='center')
        self.tree.column('Score', width=50, anchor='center')
        self.tree.column('Type', width=100, anchor='center')
        self.tree.column('Label', width=200, anchor='center')
        self.tree.column('Data', width=100, anchor='center')
        # 显示的表头名字
        self.tree.heading('GameName', text='GameName')  # 显示表头
        self.tree.heading('Score', text='Score')  # 显示表头
        self.tree.heading('Type', text='Type')  # 显示表头
        self.tree.heading('Label', text='Label')  # 显示表头
        self.tree.heading('Data', text='Data')  # 显示表头
        self.scrollbar.config(command=self.tree.yview)
        self.tree.pack()
    #往列表里加内容
    def insert_list(self, games):
        for i, item in enumerate(games):
            print(item['name'], item['score'], item['type'], item['label'], item['date'])

            if float(item['score'])>=8:
                self.tree.insert('', END, text=str(len(self.tree.get_children())),
                                 values=(item['name'], item['score'], item['type'], item['label'], item['date']),tags = ('excellent',))

            elif float(item['score'])>=6 and float(item['score'])<8:
                self.tree.insert('', END, text=str(len(self.tree.get_children())),
                                 values=(item['name'], item['score'], item['type'], item['label'], item['date']),
                                 tags=('pass',))
            else:
                self.tree.insert('', END, text=str(len(self.tree.get_children())),
                                 values=(item['name'], item['score'], item['type'], item['label'], item['date']),
                                 tags=('fail',))
            self.tree.tag_configure('excellent', background='red')
            self.tree.tag_configure('pass', background='pink')
            self.tree.tag_configure('fail', background='blue')
    # 继续爬一页
    def keep_load(self):
        global games, yema, ye
        yema += 1
        if yema <= int(ye):
            gd = GameDown(yema)
            gd.get_num()
            gs = gd.get_games()
            ui.insert_list(gs)
            # 存起来
            games += gs
            gd.get_num()
            lenlgh = len(self.tree.get_children())
            self.var.set(f"目前已经帮您找到{lenlgh}/{num}个游戏,{yema}/{ye}页的下载地址")
    # 加载全部页面
    def keep_load_all(self):
        t = threading.Thread(target=self.keep_load_all_map)
        t.setDaemon(True)
        t.start()
    #过程子程序
    def keep_load_all_map(self):
        global games, yema, ye
        while True:
            yema += 1
            if yema <= int(ye):
                gd = GameDown(yema)
                gd.get_num()
                gs = gd.get_games()
                ui.insert_list(gs)
                # 存起来
                games += gs
                gd.get_num()
                lenlgh = len(self.tree.get_children())
                self.var.set(f"目前已经帮您找到{lenlgh}/{num}个游戏,{yema}/{ye}页的下载地址")
            else:
                return
    #创建按钮
    def show_button(self):

        global ye, num, yema
        fm = Frame(self.root)
        fm.grid(row=1, column=0, sticky=W)
        b1 = Button(fm, text='继续加载', command=self.keep_load)
        b1.grid(row=0, column=0)
        b2 = Button(fm, text='爬取全部', command=self.keep_load_all)
        b2.grid(row=0, column=1)
        lenlgh = len(self.tree.get_children())
        self.var.set(f"目前已经帮您找到{lenlgh}/{num}个游戏,{yema}/{ye}页的下载地址")
        l1 = Label(fm, textvariable=self.var,foreground='red')
        l1.grid(row=0, column=2)
    # 创建下载地址的标签
    def show_download(self):
        fm = Frame(self.root)
        fm.grid(row=2, column=0, sticky=W)
        Label(fm, text="迅雷下载:").grid(row=0, column=0, sticky=W)
        t1 = Entry(fm, textvariable=self.var_xunlei, width=100)
        t1.grid(row=0, column=1, sticky=W)
        Label(fm, text="其它方式:").grid(row=1, column=0, sticky=W)
        t2 = Entry(fm, textvariable=self.var_baidu, width=100)
        t2.grid(row=1, column=1, sticky=W)
        Label(fm, text="其它方式:").grid(row=2, column=0, sticky=W)
        t3 = Entry(fm, textvariable=self.var_zhongzi, width=100)
        t3.grid(row=2, column=1, sticky=W)
    # 创建海报
    def show_img(self):
        fm=Frame(self.root)
        fm.grid(row=0,column=1)
        self.imglb=Label(fm)
        self.imglb.pack()
    #返回一个网络上的图片
    def get_img(self, url):
        #获取网络图片的内容
        image_bytes =requests.get(url).content
        #保存到内存
        data_stream = io.BytesIO(image_bytes)
        #加载内存数据
        pil_image = Image.open(data_stream)
        #修改尺寸
        pil_image = pil_image.resize((150, 183), Image.ANTIALIAS)
        #转化成tk支持的图片
        tk_image = ImageTk.PhotoImage(pil_image)
        return tk_image
if __name__ == "__main__":
    # 限制线程数量
    pool_sema = threading.BoundedSemaphore(50)
    # 创建互斥体
    mutex = threading.Lock()
    ui = GameUI()
    games = []
    ui.londlist()
    yema = 1
    gd = GameDown(1)
    num = gd.get_num()
    ye = gd.get_ye()
    gs = gd.get_games()
    ui.insert_list(gd.get_games())
    games += gs
    ui.show()

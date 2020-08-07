#这里的目录要自己改成TFT
from tkinter import *
from TFT import TFT
import io
from PIL import Image, ImageTk
from urllib.request import urlopen

class Strategy():

    def __init__(self, line_id, chess, equip, job, race,width):
        self.line_id = line_id
        self.chess = chess
        self.equip = equip
        self.job = job
        self.race = race
        self.r=Toplevel()  # 只能有一个tk 后面都只能用toplevel
        self.r.wm_attributes('-topmost', 1)
        self.r.geometry(f'+{width - 5}+0')

        self.root = Frame(self.r)
        self.root.grid(row=0,column=0)
        self.root1 = Frame(self.r)
        self.root1.grid(row=0,column=1)


        self.tk_early_images = []
        self.tk_metaphase_images = []
        self.tk_ereplace_images = []
        self.tk_hero_location=[]
        self.tk_equip_images = []
        self.tk_hero_images = []
        l_image = Image.open(r'data\none.png')
        l_image = l_image.resize((50, 50), Image.ANTIALIAS)
        self._image = ImageTk.PhotoImage(l_image)

    def show(self):
        tft = TFT()
        strategy = tft.get_strategy(self.line_id)
        self.r.title(strategy['lineup_name'] + " " + strategy['author_name'])
        self.show_early_heros(strategy)
        self.show_metaphase_heros(strategy)
        self.show_hero_replace(strategy)
        self.show_hero_location(strategy)
        self.show_equip_heros(strategy)
        self.show_doc(strategy)
        self.root.mainloop()

    def show_early_heros(self, strategy):
        f = Frame(self.root)
        f.pack(anchor=W)
        heros = strategy['early_heros'].split(",")
        Label(f, text='前期 > ').grid(row=0, column=0)
        for i in range(len(heros)):
            url = self.get_img_url(heros[i])
            tk_image = self.get_img(url)
            self.tk_early_images.append(tk_image)
            Label(f, image=self.tk_early_images[-1]).grid(row=0, column=i + 1)

    def show_metaphase_heros(self, strategy):
        f = Frame(self.root)
        f.pack(anchor=W)
        heros = strategy['metaphase_heros'].split(",")
        Label(f, text='中期 > ').grid(row=0, column=0)
        for i in range(len(heros)):
            url = self.get_img_url(heros[i])
            tk_image = self.get_img(url)
            self.tk_metaphase_images.append(tk_image)
            Label(f, image=self.tk_metaphase_images[-1]).grid(row=0, column=i + 1)

    def show_hero_replace(self, strategy):
        f = Frame(self.root)
        f.pack(anchor=W)
        heros = strategy['hero_replace']
        s = 0
        Label(f, text='备选    ').grid(row=0, column=s)
        for i in range(len(heros)):
            url = self.get_img_url(heros[i]['hero_id'])
            tk_image = self.get_img(url)
            self.tk_ereplace_images.append(tk_image)
            s += 1
            Label(f, image=self.tk_ereplace_images[-1]).grid(row=0, column=s)
            s += 1
            Label(f, text='>').grid(row=0, column=s)

            if "," in heros[i]['replace_heros']:
                h = heros[i]['replace_heros'].split(',')

                for r in h:
                    url = self.get_img_url(r)
                    tk_image = self.get_img(url)
                    self.tk_ereplace_images.append(tk_image)
                    s += 1
                    Label(f, image=self.tk_ereplace_images[-1]).grid(row=0, column=s)
            else:
                h = heros[i]['replace_heros']
                url = self.get_img_url(h)
                tk_image = self.get_img(url)
                self.tk_ereplace_images.append(tk_image)
                s += 1
                Label(f, image=self.tk_ereplace_images[-1]).grid(row=0, column=s)

            s += 1
            Label(f, text='  ').grid(row=0, column=s)

    def show_hero_location(self, strategy):


        f = Frame(self.root)
        f.pack(anchor=W)
        Label(f, text='站位').grid(row=0,column=0,rowspan=4)
        heros = strategy['hero_location']
        for i in range(4):
            for j in range(7):
                hero_set =False
                for item in heros:
                    x, y = item['location'].split(',')


                    if int(x)==i+1 and int(y)==j+1:
                        hero_set=True
                        h=item

                        break
                if hero_set==True:
                    url = self.get_img_url(h['hero_id'])
                    tk_image = self.get_img(url)
                    self.tk_metaphase_images.append(tk_image)
                    Label(f, image=self.tk_metaphase_images[-1]).grid(row=i, column=j + 1)
                else:

                    Label(f, image=self._image).grid(row=i, column=j + 1)
    def show_equipment_info(self, strategy):
        f = Frame(self.root)
        f.pack(anchor=W)
        heros = strategy['equipment_info'].split(",")
        Label(f, text='推荐出装 > ').grid(row=0, column=0)
        for i in range(len(heros)):
            url = self.get_img_url(heros[i])
            tk_image = self.get_img(url)
            self.tk_early_images.append(tk_image)
            Label(f, image=self.tk_early_images[-1]).grid(row=0, column=i + 1)
    def show_equip_heros(self, strategy):
        f = Frame(self.root)
        f.pack(anchor=W)
        hero_location = strategy['hero_location']
        Label(f, text='主C装备').grid(row=0, column=0)
        i=0

        for item in hero_location:
            #判断是否有装备
            if item['equipment_id']!="" and item['equipment_id']!=None:
                i+=1
                url = self.get_img_url(item['hero_id'])
                tk_image = self.get_img(url)#通过id找到图片地址
                self.tk_hero_images.append(tk_image)
                Label(f, image=self.tk_hero_images[-1]).grid(row=i, column=0)
                #将装备文本切割
                equips = item['equipment_id'].split(',')
                for j in range(len(equips)):
                    print('data\\'+equips[j]+".png")
                    tk_image = self.get_img('data\\'+equips[j]+".png")
                    self.tk_equip_images.append(tk_image)
                    Label(f,image=self.tk_equip_images[-1]).grid(row=i, column=j + 1)
    def show_doc(self, strategy):
        f = LabelFrame(self.root1,text="早期过渡")
        f.pack(anchor=W)
        hero_location = strategy['early_info']
        Label(f, text=hero_location, anchor=W, justify=LEFT,wraplength=500).pack()

        f = LabelFrame(self.root1, text="装备分析")
        f.pack(anchor=W)
        hero_location = strategy['equipment_info']
        Label(f, text=hero_location, anchor=W, justify=LEFT, wraplength=500).pack()

        f = LabelFrame(self.root1, text="搜牌节奏")
        f.pack(anchor=W)
        hero_location = strategy['d_time']
        Label(f, text=hero_location, anchor=W, justify=LEFT,wraplength=500).pack()

        f = LabelFrame(self.root1, text="阵容站位")
        f.pack(anchor=W)
        hero_location = strategy['location_info']
        Label(f, text=hero_location, anchor=W, justify=LEFT,wraplength=500).pack()

        f = LabelFrame(self.root1, text="克制分析")
        f.pack(anchor=W)
        hero_location = strategy['enemy_info']
        Label(f, text=hero_location, anchor=W, justify=LEFT,wraplength=500).pack()

    def get_img(self, url):
        pil_image = Image.open(url)
        pil_image = pil_image.resize((50, 50), Image.ANTIALIAS)
        tk_image = ImageTk.PhotoImage(pil_image)
        return tk_image

    def get_img_url(self, hero_id):
        url = ''
        for n in range(len(self.chess)):
            if hero_id == self.chess[n]['chessId']:
                url = 'data\\'+ self.chess[n]['name']
        return url

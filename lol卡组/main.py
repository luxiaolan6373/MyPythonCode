#自己把目录去掉.就可以引用成功了
from TFT import TFT
from kazulist import KaZuList
from tkinter import *
from urllib.request import urlopen
import pickle
class mainwindw():
    def __init__(self,chess,equip,job,race):
        self.chess=chess
        self.equip=equip
        self.job=job
        self.race=race
        self.root=Tk()
        self.root.title("演示主界面")
        self.root.wm_attributes('-topmost', 1)#窗口置顶
        self.root.overrideredirect(True)#去掉边框 标题栏
    def listshow(self):
        # 可以使用print(列表名)打印数据
        tft=TFT()
        list = tft.get_linelist()
        kz = KaZuList(list, self.chess, self.equip, self.job, self.race,self.root.winfo_height())
        kz.show()
    def show(self):
        b_kazulist=Button(self.root,text='推荐列表',command=self.listshow)
        b_kazulist.grid(row=0,column=0)
        b_chess = Button(self.root,text='英雄资料')#懒得写.自己完善吧
        b_chess.grid(row=0, column=1)
        b_equip = Button(self.root,text='装备资料')#懒得写.自己完善吧
        b_equip.grid(row=0, column=2)
        b_equip = Button(self.root, text='关闭',command=self.root.quit)
        b_equip.grid(row=0, column=3)
        self.root.mainloop()


def download_chess_pic(chess):
    for item in chess:
        image_bytes = urlopen("https://game.gtimg.cn/images/lol/act/img/tft/champions/"+item['name'] ).read()
        with open('data\\'+item['name'], 'wb') as f:
            f.write(image_bytes)

    #with open(r'data\'+item['name'],'wb') as f:
def download_equip_pic(equip):
    for item in equip:
        image_bytes = urlopen(item['imagePath']).read()
        name=str(item['imagePath']).split('/')[-1]
        with open('data\\'+name, 'wb') as f:
            f.write(image_bytes)

    #with open(r'data\'+item['name'],'wb') as f:
def main():
    try:
        f = open(r'data\chess.pkl', 'rb')
        chess = pickle.load(f)
        f.close()
        f = open(r'data\equip.pkl', 'rb')
        equip = pickle.load(f)
        f.close()
        f = open(r'data\job.pkl', 'rb')
        job = pickle.load(f)
        f.close()
        f = open(r'data\race.pkl', 'rb')
        race = pickle.load(f)
        f.close()
    except:
        tft = TFT()
        chess = tft.get_chess()  # 获取所有的棋子数据 返回一个列表
        download_chess_pic(chess)
        equip = tft.get_equip()  # 获取所有的装备数据 返回一个列表
        download_equip_pic(equip)
        job = tft.get_job()  # 获取所有的职业数据 返回一个列表
        race = tft.get_race()  # 获取所有的羁绊数据 返回一个列表
        with open(r'data\chess.pkl', 'wb') as f:
            pickle.dump(chess, f)
        with open(r'data\equip.pkl', 'wb') as f:
            pickle.dump(chess, f)
        with open(r'data\job.pkl', 'wb') as f:
            pickle.dump(chess, f)
        with open(r'data\race.pkl', 'wb') as f:
            pickle.dump(chess, f)
    mw=mainwindw(chess,equip,job,race)
    mw.show()











    # 演示推荐列表
    # for i in list:
    # 一个一个获取攻略数据
    # 具体的调用字典的哪个key.请自己看函数里面的备注说明.要显示出来就需要自己写一个界面了.饭已做好,要自己拿筷子吃了 举一反三
    # strategy=tft.get_strategy(i['line_id'])
    # 这里演示的一些数据 还有N多数据,反正都已经获取到了

    # print(i['line_name'],strategy['author_name'],strategy['early_info'])

if __name__ == "__main__":
    main()

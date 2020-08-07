import requests
import bs4#BeautifulSoup4
import re
import openpyxl
#定义类
class DouBanGet:
    def __init__(self,url):
        self.url=url
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
        self.res = requests.get(self.url, headers=self.headers)
        self.soup = bs4.BeautifulSoup(self.res.text, "html.parser")
    def getTitle(self):#获取标题
        targets = self.soup.find_all("div", class_="hd")
        t = []
        for each in targets:
            t.append(each.a.span.text)
        return t
    def getRating_num(self):#获取评分
        targets = self.soup.find_all("span", class_="rating_num")
        t = []
        for each in targets:
            t.append(each.text)
        return t
    def getBrief(self):#获取简介
        targets = self.soup.find_all("div", class_="bd")
        t = []
        for each in targets:
            if each.p.text!="豆瓣":
                #'取两个\n中间的数据'
                t.append(each.p.text.split('\n')[1].strip()+each.p.text.split('\n')[2].strip())
        return t
    def getPic(self):#获取海报地址
        targets = self.soup.find_all("div", class_="pic")
        t = []
        for each in targets:
            t.append(each.a.img['src'])
        return t
    def getCount(self):#获取数量
        targets = self.soup.find("span", class_="count")
        # 正则表达式取数字
        return re.sub("\D", "", targets.text)

def save_to_excel(result):
    wb=openpyxl.Workbook()
    ws=wb.active

    ws.append(['电影名称','评分','简介','海报地址'])

    for each in result:
        print(each)
        ws.append(each)
    wb.save(r"C:\Users\Administrator\Desktop\top250.xlsx")

#开始获取-------------------------------------------------
db1=DouBanGet("https://movie.douban.com/top250")
num=int(db1.getCount())#获取页数
num=num//25#整除
text=""#结果文本初始化
result=[]
for i in range(num):
    #每隔25个为一页
    url="https://movie.douban.com/top250?start=%d" % (i*25)
    db = DouBanGet(url)
    title=db.getTitle()#标题
    rating_num=db.getRating_num()#评分
    brief=db.getBrief()
    pic=db.getPic()#海报地址
    for i in range(len(title)):
        result.append([title[i],rating_num[i],brief[i],pic[i]])

#最后保存
save_to_excel(result)











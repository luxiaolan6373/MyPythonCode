import requests
import bs4
class Bibili():
    def __init__(self,text,page=1):
        self.url= "https://search.bilibili.com/all"
        self.params={'keyword':text,'page':str(page)}
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
        #访问
        self.res=requests.get(self.url,params=self.params,headers=self.headers)
        #将网页源码转换成bs4类.这样就很好提取数据
        self.soup=bs4.BeautifulSoup(self.res.text,"html.parser")
        print(self.soup.text)
    def get_title(self):
        titles=self.soup.find_all('li',class_="video-item matrix")
        test=[]
        for each in titles:
            test.append(each.a['title'])
        return test
    def get_url(self):
        url=self.soup.find_all('li',class_="video-item matrix")
        test = []
        for each in url:
            test.append("https:"+each.a['href'])
        return test

    def get_img(self):
        img = self.soup.find_all('li', class_="video-item matrix")
        test = []
        for each in img:
            test.append(each.a.div.div.img['src'])
        return test
    def get_watchnum(self):
        watchnum=self.soup.find_all('span',title="观看")
        test=[]
        for each in watchnum:
            test.append(each.text)
        return test
def main():
    text=input("请输入关键字:")
    length=int(input("您想要爬多少页:"))
    for i in  range(length):
        bl = Bibili(text, i+1)
        bl.get_title()
        bl.get_url()
        bl.get_img()
        bl.get_watchnum()
if __name__=="__main__":
    main()
import requests
import bs4
import openpyxl
def openurl(url):
    headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}
    res=requests.get(url,headers=headers)

    return res
def finddata(res):
    soup=bs4.BeautifulSoup(res.text,"html.parser")
    content=soup.find(class_="fjlist-box boxstyle1")
    content=content.find("ul")
    content=content.find_all("li")
    test=[]
    #content=iter(target)#转换成迭代器
    for s in content:
        #
        # 如果是有多个标签名是一样的,那就用next(s).a.b.text  这样可以访问下一个下标的
        test.append([s.a.b.text,
                     s.a.span.text,
                     s.a.em.text])
        print(s.a.b.text,s.a.span.text,s.a.em.text)
    return test
def to_excel(data):
    wb=openpyxl.Workbook()
    wb.guess_types=True
    ws=wb.active
    ws.append(['城市',"平均房价","涨幅"])
    for each in data:
        ws.append(each)
    wb.save(r"C:\Users\Administrator\Desktop\2020全国房价排行.xlsx")
def main():
    url="https://www.anjuke.com/fangjia/quanguo2020/"
    res=openurl(url)
    with open(r"C:\Users\Administrator\Desktop\test.txt","w",encoding="utf-8") as file:
        file.write(res.text)
        data=finddata(res)
        to_excel(data)
if __name__=="__main__":
    main()
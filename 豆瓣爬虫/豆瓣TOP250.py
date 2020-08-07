import requests
import bs4 #BeautifulSoup4
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
res=requests.get("http://movie.douban.com/top250" , headers=headers)
print(res.status_code)
soup=bs4.BeautifulSoup(res.text,"html.parser")
targets=soup.find_all("div", class_="hd")
for each in targets:
    print(each.a.span.text)
print(len(targets))
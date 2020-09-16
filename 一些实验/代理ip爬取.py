import bs4,requests,time

def getIP(page):
    url=f'https://www.kuaidaili.com/free/inha/{page}/'
    res=requests.get(url)
    soup=bs4.BeautifulSoup(res.text,'html.parser')
    soup=soup.find('tbody')
    soup=soup.find_all('tr')
    for item in soup:
        d=dict.fromkeys(('ip','port'))
        d['ip']=item.td.text
        d['port'] = item.td.next_sibling.next_sibling.text
        print(d)
for i in range(4):
    getIP(i+1)
    time.sleep(1)



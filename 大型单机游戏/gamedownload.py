import requests
import bs4


class GameDown():
    def __init__(self, num):
        self.res = requests.get(f"https://dl.3dmgame.com/all_all_{num}_hot")
        self.soup = bs4.BeautifulSoup(self.res.text, "html.parser")

    def get_num(self):
        soup = self.soup.find("div", class_='num')
        return soup.span.text

    def get_ye(self):
        soup = self.soup.find("li", class_='last')
        print(soup.a['data-page'])
        return soup.a['data-page']

    # 返回游戏所有的资料
    def get_games(self):
        soup = self.soup.find_all('div', class_="item")
        test = []
        for item in soup:
            t = str(item)
            if "微端下载" not in t:  # 排除恶心的广告
                d = dict.fromkeys(('name', 'img', 'url', 'type', 'label', 'language', 'score', 'date', 'platform'))
                d['img'] = item.div.a.img['src']  # 图片
                s = bs4.BeautifulSoup(t, "html.parser")
                s = s.find('div', "text")
                d['name'] = s.div.a.text  # 名称
                d['url'] = s.div.a['href'].split("/")[-1].split('.')[0]  # 地址
                d['type'] = s.ol.li.i.text  # 类型
                s = bs4.BeautifulSoup(str(s.ol), "html.parser")
                s = s.find_all('li')
                d['language'] = s[2].i.text  # 语言
                d['score'] = s[3].i.text  # 评分
                d['date'] = s[4].i.text  # 日期
                d['platform'] = s[5].i.text  # 平台
                s = bs4.BeautifulSoup(str(s[6]), "html.parser")
                s = s.find_all('a')
                labels = []
                for sem in s:
                    labels.append(sem.text)

                d['label'] = labels  # 标签 是一个列表
                test.append(d)
        return test

    def get_games_Down_Url(self, id):
        res = requests.get(f"http://box.hyds360.com/down/{id}-2.html")
        soup = bs4.BeautifulSoup(res.text, "html.parser")
        urls = dict.fromkeys(('xunlei', "baidu", "zhongzi"))
        s = soup.find_all("a", "gameDown down_bd")

        try:
            xunlei=res.text.split("url: '")[-1].split("'")[0]
            if "thunder" in xunlei:
                urls['xunlei'] = xunlei
            else:
                urls['xunlei'] = "暂无资源"
        except:
            urls['xunlei'] = "暂无资源"
        try:
            urls['baidu'] = s[0]['href'] + s[0].text.replace("网盘下载", "").replace("种子下载", "")
        except:
            urls['baidu'] = "暂无资源"
        try:
            urls['zhongzi'] = s[1]['href']
        except:
            urls['zhongzi'] = "暂无资源"
        return urls

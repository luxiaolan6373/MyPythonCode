import requests
import bs4

class GameDown():
    def __init__(self,num,sort):
        '''
        :param num:整数型 页码
        :param sort: 字符串类型,类型有time,hot,score,和前面加个-就是倒序
        '''
        self.res = requests.get(f"https://dl.3dmgame.com/all_all_{num}_{sort}")
        self.soup = bs4.BeautifulSoup(self.res.text, "html.parser")

    def get_num(self):
        '''
        :return: 返回有游戏的总数
        '''
        soup = self.soup.find("div", class_='num')
        return soup.span.text

    def get_ye(self):
        '''
        :return: 返回游戏的总页数
        '''
        soup = self.soup.find("li", class_='last')
        return soup.a['data-page']

    def get_games(self):
        '''
        :return: 返回游戏的资料
        '''
        soup = self.soup.find_all('div', class_="item")
        test = []
        for item in soup:
            t = str(item)
            if "微端下载" not in t:  # 排除恶心的广告
                d = dict.fromkeys(('name', 'img', 'id', 'type', 'label', 'language', 'score', 'date', 'platform','hot','size'))
                d['img'] = item.div.a.img['src']  # 图片
                s = bs4.BeautifulSoup(t, "html.parser")
                d['hot'] = s.a.text.split('(')[-1].split(')')[0]  # 大小
                s = s.find('div', "text")
                d['name'] = s.div.a.text  # 名称
                d['id'] = s.div.a['href'].split("/")[-1].split('.')[0]  # 地址
                d['type'] = s.ol.li.i.text  # 类型
                d['hot'] = s.ol.li.next_sibling.next_sibling.i.text  # 热度

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
        '''
        :param id: 游戏id 资料里面获取
        :return: 返回下载链接
        '''
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

    def find_Game(self,keyword):
        '''
        :param keyword: 关键字搜索
        :return: 搜索到了之后返回游戏资料列表
        '''
        url=f"https://so.3dmgame.com/?keyword={keyword}&type=5&page=1"
        res=requests.get(url)
        ye=int(str(res.text).split('total : ')[-1].split(',')[0])
        ls=[]
        for i in range(ye):
            if i>0:
                url = f"https://so.3dmgame.com/?keyword={keyword}&type=5&page={i + 1}"
                res = requests.get(url)
            soup = bs4.BeautifulSoup(res.text, 'html.parser')
            soup = soup.find_all('div', class_='search_lis lis_djxz')
            #next_sibling.next_sibling 意思就是下一个兄弟元素
            for item in soup:
                d = dict.fromkeys(('name', 'img', 'id', 'type', 'label', 'language', 'score', 'date', 'platform','hot','size'))
                d['name'] = item.a.text  # 游戏名
                d['id'] = item.a['href'].split('/')[-1].split('.')[0]  # 游戏id
                d['img'] = item.a.next_sibling.next_sibling.img['src']#海报

                d['type'] = item.ul.li.p.text.replace('类型：','')
                d['hot'] = item.ul.li.p.next_sibling.next_sibling.text.replace('热度：', '')

                d['score'] = item.ul.li.next_sibling.next_sibling.p.text.replace('评分：', '')
                d['language'] = item.ul.li.next_sibling.next_sibling.p.next_sibling.next_sibling.text.replace('语言：', '')

                d['date'] = item.ul.li.next_sibling.next_sibling.next_sibling.next_sibling.p.text.replace('更新：', '')
                d['platform'] = item.ul.li.next_sibling.next_sibling.next_sibling.next_sibling.p.next_sibling.next_sibling.text.replace('平台：', '')

                d['size'] = item.ul.li.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.p.text.replace('大小：', '')
                d['label'] = item.ul.li.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.p.next_sibling.next_sibling.text.replace('标签：', '').split('，')
                ls.append(d)
        return ls

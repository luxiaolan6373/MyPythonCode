import requests
import os
import bs4
import json
from 视频爬取.下载3u8m视频 import *
import threading
class BaoYu():
    def __init__(self,url,playurl,path,okpath):
        self.url=url
        self.playurl=playurl
        self.path=path
        self.okpath=okpath
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
    def get_web(self, url):
        try:
            res = requests.get(url, headers=self.headers)

            soup = bs4.BeautifulSoup(res.text, "html.parser")
            content = soup.find('ul', class_="stui-header__menu type-slide")
            content = content.find_all('li')
            # print(content)
            urls = []
            for item in content:
                if item.a['href'] != '/' and item.a['href'] != '#':
                    d = dict.fromkeys(('title', 'url'))
                    d['title'] = item.a.text
                    d['url'] = url + item.a['href']
                    urls.append(d)
            return urls
        except:
            print('get_web访问主页失败,请检查网址或者网络')
            return '-1'
    def get_num_pages(self, url):
        try:
            res = requests.get(url, headers=self.headers)
            soup = bs4.BeautifulSoup(res.text, "html.parser")
            content = soup.find('li', class_="active visible-xs")
            return int(content.span.text.split('/')[-1])
        except:
            print("get_num_pages获取页数错误,请调试找出问题!")
            return -1
    def get_zipai_urls(self, url, typ):  # 返回所有的视频链接和标题的字典
        try:
            url = url.split('.html')[0]
            url = url + "/page/" + str(typ) + ".html"
            res = requests.get(url, headers=self.headers)
            # print( res.text)
            soup = bs4.BeautifulSoup(res.text, "html.parser")
            content = soup.find('ul', class_="stui-vodlist clearfix")
            content = content.find_all('li')
            urls = []
            for item in content:
                d = dict.fromkeys(('title', 'url', 'pic', 'playls'))  # 标题,链接,图片,播放量
                d['title'] = item.div.a['title']
                d['pic'] = item.div.a['data-original']
                d['url'] = item.div.a['href']
                txt = str(item.div.a)
                con = bs4.BeautifulSoup(txt, "html.parser")
                con = con.find('span', class_='pic-text text-right')
                d['playls'] = con.text
                urls.append(d)
            return urls
        except:
            print('get_zipai_urls访问失败,请检查网址或者网络')
            return -1
    def get_play_3u8m_url(self, urls):  # 下载主过程
        # print('当前子线程: {}'.format(threading.current_thread().name))
        url = urls['url']
        playurl = self.get_data_url(self.url + url)
        title = urls['title']
        title = title.replace(" ", "_")
        url_m3u8 = self.playurl + f'{playurl}/360p/360p.m3u8'
        videoName = url_m3u8.split('/')[-3]
        path = self.path + title
        print(videoName)
        if self.find_url_is_ture(videoName) == False:
            if os.path.isdir(path) == False:
                os.makedirs(path)
            try:
                if getVideo_urllib(url_m3u8, path, videoName):
                    mutex.acquire()
                    with open(self.okpath, 'a')  as file:
                        file.write(videoName + "\n")
                    mutex.release()
                else:
                    print(title + " " + playurl + ' 下载失败! 1')

            except:
                print(title + " " + playurl + ' 下载失败! 2')
        else:
            print(title + " " + url + ' 跳过,早就下载过了!')
        pool_sema.release()

    def get_data_url(self,url):
        try:
            res = requests.get(url, headers=self.headers)
            soup = bs4.BeautifulSoup(res.text, "html.parser")
            soup = soup.find('div', class_='stui-player__video embed-responsive embed-responsive-16by9 clearfix')
            soup = soup.find('script', type='text/javascript')
            soup = str(soup).split('script type="text/javascript">var player_data=')[-1]
            soup = soup.split('</script>')[0]
            j = json.loads(soup)

            t=str(j['url']).split('/index.m3u8')[0]
            return t
        except:
            print("get_data_url访问出错,请检查!")
            return '-1'
    def find_url_is_ture(self,url):  # 判断是否是在完成的库中
        try:
            with open(self.okpath, 'r')  as file:

                for item in file.readlines():
                    if url.strip() == item.strip():
                        return True
                return False
        except:
            return False
class MyThread(threading.Thread):
    def __init__(self, func, args):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args

    def run(self):
        self.func(self.args[0])
def main():
    #这里设置好条件-------------
    url="https://www.byjj222jzdou077fulc1r8.fun:52789/"
    playurl='https://z.weilekangnet.com:59666/'
    path=f'D:\\baoyu\\dongman\\'
    okpath=r'D:\baoyu\完成列表.ini'
    by = BaoYu(url,playurl,path,okpath)
    # 有几个栏目
    urls = by.get_web(url)
    # 读取urls[1]['url'] 栏目 有多少页
    l = 4 # 栏目 0开始   返回一页的所有视频3m8u链接
    num_pages = by.get_num_pages(urls[l]['url'])
    for i in range(num_pages):
        print('-------------------------正在爬取%s的第%d页-------------------------'%(urls[l]['title'],i+1))
        play_urls = by.get_zipai_urls(urls[l]['url'], i)
        for item in play_urls:
            pool_sema.acquire()
            t=MyThread(by.get_play_3u8m_url, args=(item,))
            t.setDaemon(True)
            t.start()
if __name__ == '__main__':
    #限制线程数量
    pool_sema = threading.BoundedSemaphore(50)
    #创建互斥体
    mutex = threading.Lock()
    # que = queue.Queue()
    # by = BaoYu()
    # 有几个栏目
    # rls = by.get_web("https://www.byjj222jzdou077fulc1r8.fun:52789//")
    # by.get_num_pages(urls[1]['url'])
    # by.get_play_3u8m_url(play_urls[2])

    main()
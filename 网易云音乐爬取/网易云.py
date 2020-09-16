import threading, requests
from wangyiyunJx import WangYiYun
from tkinter import *
import urllib.request
# 多线程模板,直接抄就行
class MyThread(threading.Thread):
    '''多线程模板,直接抄就行'''

    def __init__(self, func, args):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args

    def run(self):
        # 多线程模板,直接抄就行 这里的参数,有多少个就多少个args[]
        self.func(self.args[0], self.args[1])
class wyyUI():
    def __init__(self):
        self.root=Tk()
        self.root.title("网易云音乐下载器")


def download(url, pathName):
    '''
    下载文件
    :param url: 目标网址
    :param pathName: 保存文件名0
    :return: 返回是否成功
    '''
    headers = {
        'cookie':'这里自己填上cookie',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
    pathName = pathName + '.mp3'
    try:
        data = requests.get(url,headers=headers).content
        with open(pathName, 'wb')as flie:
            flie.write(data)
        print(pathName + '下载成功!')
    except:
        print(pathName,'下载失败!',url,'正在尝试第二次')
        try:
            data = urllib.request.urlopen(url, headers=headers).content
            with open(pathName, 'wb')as flie:
                flie.write(data)
            print(pathName + '下载成功!')
        except:
            print(pathName, '第二次尝试下载失败!', url, )
    finally:
        pool_sema.release()

def download_music_all(musics):
    '''
    多线程下载音乐,需要提前设置好线程和相关变量申请
    :param musics: 音乐资料列表
    :return: 是否完成
    '''
    print('-----------开始下载----------')
    for item in musics:
        #url=wyy.get_music_url(item['id'])
        url=f"https://music.163.com/song/media/outer/url?id={item['id']}"
        pool_sema.acquire()
        t = MyThread(download, args=(url, Spath + item['name']))
        t.setDaemon(True)
        t.start()
    print('全部下载工作完成!')

if __name__ == '__main__':
    Spath = 'D:\网易云音乐\\'
    # 限制线程数量
    pool_sema = threading.BoundedSemaphore(20)
    # 初始化网易云解析对象
    wyy = WangYiYun()
    # 获取所有的排行榜类型
    tops = wyy.get_Top()
    for i, item in enumerate(tops):
        print(i, item['title'])
    while True:
        key = input(f'请选择功能填写序号:  0-{len(tops)}\r\n')
        try:
            musics = wyy.get_TopList(tops[int(key)]['id'])
            break
        except:
            print('输入有误!请重新输入!')
    for i, item in enumerate(musics):
        text = ''
        for a, art in enumerate(item['artists']):
            if a == len(item['artists']) - 1:
                text = text + art['name']
            else:
                text = text + art['name'] + '/'

        print(i, item['name'], text)
    key = input(f'请选择要下载的歌曲:  0-{len(musics)}\r\n  全下输入# 返回输入f 退出输入x')
    download_music_all(musics)

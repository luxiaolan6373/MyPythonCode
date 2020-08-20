from 大型单机游戏.gamedownload import GameDown
import threading
class MyThread(threading.Thread):
    def __init__(self, func, args):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args

    def run(self):
        self.func(self.args[0])

def get_games_all(gd,):

    gd.get_games_Down_Url
    pool_sema.release()
if __name__ == "__main__":
    # 限制线程数量
    pool_sema = threading.BoundedSemaphore(50)
    # 创建互斥体
    mutex = threading.Lock()
    gd = GameDown(1)
    num = gd.get_num()
    ye = gd.get_ye()
    #一共这么多页
    for i in range(ye):
        gd = GameDown(i+1)
        games=gd.get_games()
        #每一页都有这么多数据
        for item in games:
            pool_sema.acquire()
            t=MyThread(gd.get_games_Down_Url,args=(item['url'],))
            t.setDaemon(True)
            t.start()





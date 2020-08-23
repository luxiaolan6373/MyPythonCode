from 大型单机游戏.gamedownload import GameDown
import threading
import openpyxl
import datetime
#多线程模板,直接抄就行
class MyThread(threading.Thread):
    def __init__(self, func, args):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args

    def run(self):
        # 多线程模板,直接抄就行 这里的参数,有多少个就多少个
        self.func(self.args[0],self.args[1])

def find_game_is_ture(okpath, name):  # 判断是否是在完成的库中
    try:
        with open(okpath, 'r')  as file:
            for item in file.readlines():
                #删除首位空格
                if name.strip() == item.strip():
                    return True
            return False
    except:
        return False
def get_games_all(gd, game):
    '''
    这个主要是把下载链接获取到
    :param gd: 因为方法在游戏类里面,所以要把对象提交过来
    :param game: 游戏字典数据(通过这个来获取下载地址)
    :return: 返回一个字典数据,就是把先前没下载地址的更新上下载地址,里面有游戏的各种资料,
    '''
    #线程池+1
    path='已经完成的.txt'
    #查看是否有存过
    if find_game_is_ture(path,game['name']) ==False:
        try:
            g=gd.get_games_Down_Url(game['url'])
            #把先前没下载地址的更新上下载地址
            game.update(g)
            if (game['xunlei'] == '暂无资源' and game['baidu'] == '暂无资源' and game['zhongzi'] == '暂无资源') or "正版" in game['name']:
                print('{}暂无资源'.format(game['name']))
                pool_sema.release()
                return
            mutex.acquire()
            #如果有则说明不需要搞标题,没有就直接创建
            try:
                wb = openpyxl.load_workbook(sname)
                ws = wb.active  # 获取工作表
            except:
                wb = openpyxl.Workbook()
                ws = wb.active  # 获取工作表
                ws.freeze_panes = 'B2'
                ws.append(['游戏名', '类型', '标签', '语言', '评分', '上架日期',
                          '平台', '迅雷下载', '其它下载1', '其它下载2', '海报地址'])
            ws.append([game['name'],game['type'],str(game['label']),game['language'],game['score'],game['date'],game['platform'],game['xunlei'],game['baidu'],game['zhongzi'],game['img']])
            wb.save(sname)
            with open(path, 'a')  as file:
                file.write(game['name'] + "\n")
            print(f"保存[{game['name']}]到 {sname} 成功!")
        except:
            print(f"保存[{game['name']}]到 {sname} 失败!")
        # 线程池-1
        mutex.release()
    else:
        print(f"[{game['name']}]已经爬过 跳过它!")
    pool_sema.release()
if __name__ == "__main__":
    tm= datetime.datetime.now()
    sname = f"大型单机游戏{tm.year}年{tm.month}月{tm.day}日.xlsx"
    # 限制线程数量
    pool_sema = threading.BoundedSemaphore(50)
    # 创建互斥体
    mutex = threading.Lock()
    gd = GameDown(1)
    num = gd.get_num()
    ye = int(gd.get_ye())
    # 一共这么多页
    for i in range(ye):
        gd = GameDown(i + 1)
        games = gd.get_games()
        # 每一页都有这么多数据
        for item in games:
            pool_sema.acquire()
            t = MyThread(get_games_all, args=(gd, item))
            t.setDaemon(True)
            t.start()

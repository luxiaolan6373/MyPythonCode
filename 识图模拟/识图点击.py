import pyautogui, threading, time
# 多线程模板,直接抄就行
class MyThread(threading.Thread):
    def __init__(self, func, args):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args

    def run(self):
        # 多线程模板,直接抄就行 这里的参数,有多少个就多少个
        self.func(self.args[0], self.args[1])


def st(imageID, i):
    '''
    全屏找图
    :param imageID: 英雄编号
    :return: 无返回值
    '''
    x, y=0,0
    #截商店区域的图 用于对比识别
    haystackImage=pyautogui.screenshot(region=(475, 1035, 940, 30))
    #对比
    location = pyautogui.locate(needleImage=f'stImage\\{imageID}.png',haystackImage=haystackImage, grayscale=True)
    if location != None:
        # 利用center()函数获取目标图像在系统中的中心坐标位置
        x, y = pyautogui.center(location)
        x,y=x+475+20, y+1035 - 20
        print(imageID,x, y)
        # 如果上一回的x值不等于这个x,则继续
        if RecordsX[i] != x:
            mutex.acquire()  # 锁住资源 以防冲突
            # 对识别出的目标图像进行点击
            # 参数x,y代表坐标位置，clicks代表点击次数,button可以设置为左键或者右键
            pyautogui.click(x=x, y=y, clicks=2, button='left')
            mutex.release()  # 解锁资源
    RecordsX[i] = x


if __name__ == "__main__":
    stlmage = []
    # 这里模拟选中了5个英雄 存的是图片的序号
    stlmage.append(1)
    stlmage.append(2)
    stlmage.append(3)
    stlmage.append(4)
    stlmage.append(5)
    mutex = threading.Lock()
    # 这个用来存储上一次的识图情况,这样可以判断,是否点击成功
    #暂时存一下和选中列表一样的数据,占位置的作用
    RecordsX = stlmage.copy()
    # 有多少个选中的英雄,就开启多少个线程
    while True:
        t=[]
        for i, item in enumerate(stlmage):
            # 启动线程  i记录是第几个英雄的线程
            t.append(MyThread(st, args=(item, i)))
            t[-1].start()
        #等待线程结束
        for item in t:
            item.join()

        print(RecordsX)




import os
from comtypes import client
#这里只能用comtypes 不能用win32com来调用.不然会报错,研究了贼久才搞明白!并且必须是32位的python
def regLW():
    '''
    注册乐玩插件,需要把文件lw.dll放在根目录
    :return: 返回乐玩对象
    '''
    try:
        lw = client.CreateObject("lw.lwsoft3")
    except:
        os.system('regsvr32 lw.dll')
        lw = client.CreateObject("lw.lwsoft3")
    return lw


# 从系统中卸载乐玩
def unRegLW():
    '''
    从系统中卸载乐玩插件,有些时候注册不成功,可以先卸载一下
    :return:
    '''
    os.system('regsvr32 lw.dll /u')


lw = regLW()
print(lw.ver())
lw.MoveTo(0,0)
# 接下来就可以自己查接口说明来使用里面的全部方法了

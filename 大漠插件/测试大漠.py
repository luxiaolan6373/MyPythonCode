from win32com.client import Dispatch
import os

#注册大漠到系统中.
def regDM():
    '''
    注册大漠插件,需要把文件dm.dll放在根目录
    :return: 返回大漠对象
    '''
    try:
        dm = Dispatch('dm.dmsoft')
    except:
        os.system('regsvr32 dm.dll')
        dm = Dispatch('dm.dmsoft')
    return dm

#从系统中卸载大漠
def unRegDM():
    '''
    从系统中卸载大漠插件
    :return:
    '''
    os.system('regsvr32 dm.dll /u')


if __name__ == "__main__":
    # 注册大漠
    dm = regDM()
    reg_code = "luxiaolan63735f4be12fda045a12cf1b2927d5cbc19c"  # 大漠后台的注册码
    ver_info = '0001'  # 附加信息,主要用于查询消费情况 填了更好查询,不填也无所谓
    # 登录大漠.就是身份验证一下,从而使用插件的高级功能,如果你的是3.xx的免费版本,就不需要这步
    value = dm.reg(reg_code, ver_info)
    # 调试验证结果
    print(value)
    if value != 1:
        if value == -2:
            print('进程没有以管理员方式运行或者被第三方杀毒拦截. (建议关闭uac和杀毒软件),请用管理员权限运行本程序!')
        else:
            print(f'验证失败,失败代码为:{value},大概率是被杀毒拦截了,请联系作者!')

    # 接下来就可以自己查接口说明来使用里面的全部方法了

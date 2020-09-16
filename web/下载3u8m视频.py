import os, shutil
import urllib.request, urllib.error
import socket
import threading
socket.setdefaulttimeout(30)
# 打开并读取网页内容
def getUrlData(url):
    try:
        urlData = urllib.request.urlopen(url, timeout=20)  # .read().decode('utf-8', 'ignore')
        return urlData
    except Exception as err:
        print(f'err getUrlData({url})\n', err)
        return -1
    except socket.timeout:
        print(f'err getUrlData({url})下载超时!\n',err)
        return -1
# 下载文件-urllib.request
def getDown_urllib(url, file_path):
    try:
        urllib.request.urlretrieve(url, filename=file_path)
        return True
    except socket.timeout:
        count = 1
        while count <= 10:
            try:
                urllib.request.urlretrieve(url, filename=file_path)
                return True
                break
            except socket.timeout:
                err_info = 'Reloading for %d time' % count if count == 1 else 'Reloading for %d times' % count
                print(err_info)
                count += 1
        if count > 10:
            print('重试了10次全部失败')
            return False
    except urllib.error.URLError as e:
            #hasttr(e, 'code')，判断e 是否有.code属性，因为不确定是不是HTTPError错误，URLError包含HTTPError，但是HTTPError以外的错误是不返回错误码(状态码)的
        if hasattr(e, 'code'):
            print(e.code)  # 打印服务器返回的错误码（状态码），如403，404,501之类的
        elif hasattr(e, 'reason'):
            print(e.reason)  # 打印错误原因
        return False
def getVideo_urllib(url_m3u8, path, videoName):
    print(videoName+"开始下载")
     # urlData = getUrlData(url_m3u8).readlines()
    urlData = getUrlData(url_m3u8)
    if urlData==-1 :#超时了返回-1
        return False
    tempName_video = os.path.join(path, f'{videoName}.ts')  # f'{}' 相当于'{}'.format() 或 '%s'%videoName
    # print(urlData)
    #接上上次中断的
    try:
        with open(path + "\location.ini", 'r')  as file:
            num = int(file.read())
            print(videoName + " ", num, '发现有下载过,成功续上!')
    except:
        num = 0
    s=0

    for i,line in enumerate(urlData):
        # 解码，由于是直接使用了所抓取的链接内容，所以需要按行解码，如果提前解码则不能使用直接进行for循环，会报错
        # 改用上面的readlines()或readline()也可以，但更繁琐些，同样需要按行解码，效率更低
        url_ts = line.decode('utf-8')
        path
        tempName_ts = os.path.join(path, f'{num}.ts')  # f'{}' 相当于'{}'.format()
        if not '.ts' in url_ts:
            s+=1
            continue

        else:
            if not url_ts.startswith('http'):  # 判断字符串是否以'http'开头，如果不是则说明url链接不完整，需要拼接
                # 拼接ts流视频的url
                url_ts = url_m3u8.replace(url_m3u8.split('/')[-1], url_ts)
        print('当前线程数量', threading.activeCount())
        if i<num+s:#用来直接续上
            continue
        #print(url_ts)
        # 下载视频流
        if getDown_urllib(url_ts, tempName_ts)==False:
            return False
        if num == 0:
            # 重命名，已存在则自动覆盖
            shutil.move(tempName_ts, tempName_video)
            # 成功了就记录下来,方便续传
            with open(path + "\location.ini", 'w')  as file:
                file.write(str(num))
            num += 1
            continue
        cmd = f'copy /b {tempName_video}+{tempName_ts} {tempName_video}'
        res = os.system(cmd)
        if res == 0:
            os.system(f'del {tempName_ts}')
            #成功了就记录下来,方便续传
            with open(path + "\location.ini", 'w')  as file:
                file.write(str(num))
            num += 1
            continue
        print(f'Wrong, copy {num}.ts-->{videoName}.ts failure')
        return False
    os.system(f'del {path}/*.ts')  # 调用windows命令行（即cmd）工具，运行命令
    filename = os.path.join(path, f'{videoName}.mp4')
    shutil.move(tempName_video, filename)
    print(f'{videoName}.mp4 finish down!')
    return True

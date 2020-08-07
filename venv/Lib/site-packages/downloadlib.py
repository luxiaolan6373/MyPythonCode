#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

"""
author: luoboiqingcai <sf.cumt@gmail.com>

=======
重构说明
=======
这一版本放弃继续使用urllib2库进行http连接，而是引进了requests包进行http连接处理。这么做的原因主要不是像requests自己吹的那样是由于requests的接口比较简单，第一位的原因是为了同时兼容python2和python3。由于python3的标准库中取消了urllib2，因此原本只考虑了python2的本程序不得不重写。如果python3中还保留urllib2我才不会没事改脚本呢。使用requests虽然引入了外部依赖，但它用起来确实很pythonic，也达到了我需要的python 2和3间的兼容性要求，不错。

在对代码进行http连接部分进行重构的同时，也期待解决下面两个问题：

 - 与gui的兼容性
 - 超星下载的问题
 - prex不起作用的bug

为了防止被服务器端发现是在用机器人下资源，应避免从一个服务器下载。每次文献传递都可能是分配一个与众不同的服务器来提供文献。因此每次将咨询等到的服务器与现有服务器列表对照，如果这个服务器还没有被列入已知服务器列表，则把它加进去。

"""
import io
import requests
import random
import re
import getopt
import sys
import logging
import time
#import platform
import os
import os.path

from strategy import (FromDuxiuRemote, FromDuxiuLocal, FromChaoxing)
from multiprocessing import (cpu_count, Pool, log_to_stderr)

__author__ = "luoboiqingcai"
__contact__ = "sf.cumt@gmail.com"
__licence__ = "MIT"

duxiu_source_list = ["www2.zhengzhifl.cn","www.zirankxzl.cn","www.zhexuezj.cn","www.junshilei.cn",]

DEBUG = False
TEM_FILE = "remote_webpage_content.html"

class DownloadLib(object):
    """
    main class for this module

    from_remote
        用浏览器下载下来的网页与requests下载下来的网页是不同的，浏览器下载下来的网页可能已经过浏览器渲染过了，而用 requests 下载下来的没有经过客户端渲染。因此两都表现不同。
    lnp
        根据远程文件的名字取得用于本地存储的名字。
    pattern
        用于在网页中取得试读图片的相对地址。
    img_url_prex
        img_url_prex+pattern用于取得试读图片的完整地址。
    prex
        用于存储图片和日志文件的子目录，该子目录必须已存在。
    logfile
        日志文件名。
    """
    def __init__(self,
                 lnp,
                 pattern,
                 img_url_prex,
                 prex=None,
                 logfile=None):
        if prex != None and isinstance(prex,str):
            self.prex = prex
        else:
            self.prex = ''
            sys.stderr.write("warning: prex is empty")
        if logfile != None and isinstance(logfile,str):
            self.logfile = logfile
        else:
            self.logfile = ''
        self.pattern = pattern
        self.img_url_prex = img_url_prex
        self.lnp = re.compile(lnp)
        self.log = logging.getLogger('')
        if DEBUG:
            self.log.setLevel(logging.DEBUG)
        else:
            self.log.setLevel(logging.INFO)
        if logfile:
            self.log.addHandler(logging.FileHandler(os.path.join(self.prex,logfile),mode='w'))
        else:
            self.log.addHandler(logging.StreamHandler(sys.stderr))
        self.log.debug("DownloadLib is instanced")
    def get_content(self,url,remotep=True):
        """
        从远程网址或下载下来的本地网页中读取内容.
        
        返回一个*读打开*的*文件*对象（filelike object）。以便进行模式匹配。

        url
            试读地址或网页文件地址,根据此地址获得网页中的试读图片。
        remotep
            如果是从远程读取网页内容，应为True
            如果是从本地网页中读取内容，就为False
        """
        self.log.debug("enter get_content")
        if remotep:
            if DEBUG:
                if os.path.exists(TEM_FILE):
                    self.log.debug("%s existed"%TEM_FILE)
                    content = open(TEM_FILE,'r',encoding='utf-8')
                    #如果是写入字节:
                    #content = open(TEM_FILE,'rb')
                    #with open(TEM_FILE,'wb') as f:
                    #    print(bytes(something,'utf-8'),file=f)#错，因为print不支持二进制串
                else:
                    response = requests.get(url)
                    with open(TEM_FILE,'w',encoding='utf-8') as f:
                        self.log.debug("type of response.text:%s\ntype of f:%s"%(str(type(response.text)),str(type(f))))
                        f.write(response.text)
                        #f.write("hi") 因为文件是'b'打开的，因此写入的应是二进制而不是字符形！
                        #print(response.text,f)
                    self.log.debug("%swriten"%TEM_FILE)
                    content = io.StringIO(response.text)
            else:
                response = requests.get(url)
                content = io.StringIO(response.text)
        else:
            content = open(url,'r')
        return content
    def get_img(self,url):
        """
        返回一个二进制字节流
        url
            试读图片相对地址
        """
        s = self.img_url_prex + url
        try:
            img = requests.get(s).content
        except requests.exceptions.RequestException as e:
            self.log.warn('first time download failed: %s'%e)
            time.sleep(10)
            try:
                img = requests.get(s).content
            except requests.exceptions.RequestException as e:
                self.log.warn('try second time failed: %s'%e)
                self.log.info("%s wasn't downloaded."%s)
            else:
                self.log.info('second time succeed.')
                return img
        else:
            return img

    def get_localname(self,url):
        """
        url
            试读图片的相对地址，函数利用此相对地址取得本地存储的名字。
        """
        match = re.search(self.lnp,url)
        if match:
            localname = match.group(1) + '.png'
        else:
            localname = None
        return localname

    def get_img_pairs(self,strategy,url,
                      sp='',
                      ep=''):
        """
        返回远程地址和本地将要写入的文件的名字

        对于不同的策略(strategy),处理不同的情况。
        对于读秀下载下来的网页，其中包括完整的图片地址，而对于读秀远程和超星已下载，并不直接包含完整的图片地址，需要从其中提出信息进行处理。

        - FromDuxiuRemote() 读秀远程
        - FromDuxiuLocal() 读秀已下载
        - FromChaoxing() 超星已下载
        """
        imgurls = []
        p = re.compile(self.pattern) # 匹配图片的相对地址
        p1 = re.compile(r'.?jpgRange = "(\d+)-(\d+)";') #匹配页码范围
        if isinstance(strategy, (FromDuxiuRemote,FromChaoxing)):
            #用于从读秀远程取得的网页和下载下来的超星网页
            matched = None
            matched1 = None
            if isinstance(strategy, FromDuxiuRemote):
                content = self.get_content(url, remotep=True)
            else:
                content = self.get_content(url, remotep=False)
            for line in content:
                match = re.match(p,line)
                match1 = re.search(p1,line)
                if match:
                    matched = match
                    self.log.debug('p match')
                if match1:
                    matched1 = match1
                    self.log.debug('p1 match1')
                if matched and matched1: break
            content.close()
            if not matched or not matched1:
                raise SystemError('regular expression error.matched:%s,matched1:%s'%(matched,matched1))
            imgurl = matched.group(1)
            start_p = int(matched1.group(1))
            self.log.info('*** from:%d'%start_p)
            if sp and start_p < int(sp):
                start_p = int(sp)
            end_p = int(matched1.group(2))
            self.log.info('*** end:%d'%end_p)
            if ep and end_p > int(ep):
                end_p = int(ep)
            sys.stderr.write(str((start_p,end_p)))
            sys.stderr.flush() #如果没有这句，标准错误流就不会立即打印。
            #imgurls = map(lambda x:imgurl+x[-6:]+'?.',['000000%d'%p for p in range(start_p,end_p+1)])
            imgurls = [imgurl+'{0:06}?.'.format(p) for p in range(start_p,end_p+1)]
        elif isinstance(strategy, FromDuxiuLocal):
            # 读秀已下载
            content = self.get_content(url,remotep=False)
            for line in content:
                imgurls = re.findall(p,line)
            content.close()
        return [{'url':self.img_url_prex+imgurl,'localname':os.path.join(self.prex,self.get_localname(imgurl))} for imgurl in imgurls]

    def downloadit(self,
                   strategy,
                   url,
                   sp='',
                   ep=''):
        """
        main function.

        url
            试读内容的网址
        strategy
            对于不同的策略(strategy),处理不同的情况。
            对于读秀下载下来的网页，其中包括完整的图片地址，而对于读秀远程和超星已下载，并不直接包含完整的图片地址，需要从其中提出信息进行处理。
              
             - FromDuxiuRemote() 读秀远程
             - FromDuxiuLocal() 读秀已下载
             - FromChaoxing() 超星已下载

        sp
            从sp页开始下载,如果sp小于网页上的最小页码，则还是按网页上的最小页码开始下载。对已经下载下来的duxiu网页没有作用(remote==false)
        ep
            下载到ed页,如果ed大于网友上的最大页码，则还是下载到网页上的最大页码处。对已经下载下来的duxiu网页没有作用(remote==False)
        """
        self.log.debug("entering downloadit")
        count = 0
        img_pairs =self.get_img_pairs(strategy,url,sp,ep)
        for ul in img_pairs:
            img = self.get_img(ul['url'])
            count += 1
            try:
                f = open(ul['localname'],'wb')
                self.log.debug("type of img:%s"%type(img))
                #print(img,file=f) print不支持二进制写，而这里img是二进制流，帮出错
                f.write(img)
            except Exception as e:
                raise e
            else:
                self.log.info("%s has been download and stored locally."%ul['localname'])
            finally:
                f.close()
        self.log.info("%d images are downloaded."%count)
        return count
    __call__ = downloadit

def multidownloadlib(pair):
    """
    helper for Downloadduxiu
    """
    img = None
    try:
        img = requests.get(pair['url']).content
    except requests.exceptions.RequestException as e:
        time.sleep(10)
        try:
            img = requests.get(pair['url']).content
        except requests.exceptions.RequestException as e:
            print("second time failed")
        else:
            print("second time succeed")
    if img:
        with open(pair['localname'],'wb') as f:
            f.write(img)
    else:
        print("img empty")

def usage():
    """print program usage"""
    print('''This Python script can be used to download duxiu documents.
use this software at your own risk
author:%s %s
downlaodduxiu.py [options] arg0 arg1
Note: this script only support two argument.
Options:
-h --help print help information
--prex download dir
--logfile logfile
--resume resume recent breaken download schedule based on logfile, take preference to --sp and --ep. If the program run with --sp or --ep options and is terminated normally. --resume will NOT make any sense
--sp specify where download start
--ep specify where download end
--procnum specify whether utilize multiprocessing, only work when ep and sp parameters are not used. This option apply for both chaoxing and duxiu

arg0 "duxiu_url" :remote fetch duxiu; "duxiu_file": fetch duxiu img whose address is fetched whithin downloaded page; chaoxing:fetch chaoxing imag whose address can be inferred from downloaded page;
arg1 the url or file.

EXAMPLE:
./downloadlib.py --prex=myprex --logfile=logfile duxiu_url "url of duxiu book location"

'''%(__author__,__contact__))

def resume_point(logfile):
    """
    resume the schedule interrupted by some case.
    """
    r = re.compile(r'.* are downloaded.')
    match = None
    resume_point = ''
    with open(logfile,'rb') as f:
        with open(logfile+'.back','wb') as f1:
            f1.write(f.read())
        f.seek(0)
        tem = ''
        for l in f:
            l = l[:-1]
            if re.search(r,l):
                return ''
            tem = l
        match = re.search(r'.*?(\d+)\.png.*',tem)
        resume_point = match.group(1)
        return resume_point

if __name__ == '__main__':
    pattern_for_duxiu_l = r'<input .+?src="drspath_files/(.+?)" scr="(.+?)" .*?>' #用于取得用'''浏览器'''下载下来的网页上的图片的正则表达式。
    pattern_for_duxiu_r = r'\s+var str = "(.+)";' #用于取得'''远程'''图片的正则表达式。
    pattern_for_chaoxing =  pattern_for_duxiu_r
    lnp = r'.+/(\d+)\?\.' #根据远程图片的完整地址取得图片本地存储名字的正则表达式。
    img_url_prex = 'http://' + random.choice(duxiu_source_list) + '/n/'  # 读秀试读
    print("img_url_prex:%s\n"%img_url_prex)
    chaoxing_img_url_prex = 'http://img.sslibrary.com/n/' #超星全文
    try:
        opts, args = getopt.getopt(sys.argv[1:],'h',['help','resume','method=','prex=','logfile=','sp=','ep=','procnum='])
    except getopt.GetoptError as err:
        usage()
        raise err
        sys.exit(2)
    prex = None
    logfile = None
    resume = False
    sp = ep = ''
    processes = 1
    pool = None
    if not len(opts):
        usage()
        sys.exit(0)
    for o, a in opts:
        if o == '-h' or o == '--help':
            usage()
            sys.exit(0)
        elif o == '--prex':
            if a[-1] == '/' or a[-1] == '\\':
                prex = a[:-1]
            else:
                prex = a
        elif o == '--logfile':
            logfile = a
        elif o == '--resume':
            resume = True
        elif o == '--sp':
            sp = str(int(a))
        elif o == '--ep':
            ep = str(int(a))
        elif o == '--procnum':
            if a and a.isdigit():
                processes = int(a)
            else:
                processes = cpu_count()
        else:
            assert False, "unhandled option"
    if processes > 1:
        pool = Pool(processes=processes)
    if len(args)>2:
        print("only support two arguments one time")
        exit(1)
    else:
        libtype_ = args[0]
        if args[0] == "chaoxing":
            libtype = FromChaoxing()
        elif args[0] == "duxiu_url":
            libtype = FromDuxiuRemote()
        elif args[0] == "duxiu_file":
            libtype = FromDuxiuLocal()
        else:
            raise ValueError("wrong libtype, should be chosen among chaoxing,duxiu_url,duxiu_file.")
        arg = args[1]
    if libtype_ == "chaoxing":
        instance = DownloadLib(lnp=lnp,pattern=pattern_for_chaoxing,img_url_prex=chaoxing_img_url_prex,prex=prex,logfile=logfile)
        if resume:
            instance(libtype, arg, sp=resume_point(os.path.join(prex,logfile)))
            sys.exit(0)
        if sp and ep:
            instance(libtype, arg, sp=sp, ep=ep)
            sys.exit(0)
        if sp:
            instance(libtype, arg, sp=sp)
            sys.exit(0)
        if ep:
            instance(libtype, arg, ep=ep)
            sys.exit(0)
        if processes > 1:
            #print instance.get_img_pairs(from_remote,arg)
            #TODO
            pool.map_async(multidownloadlib,instance.get_img_pairs(libtype, arg),processes)
            pool.close()
            pool.join()
            sys.exit(0)
        else:
            instance(libtype,arg)
            sys.exit(0)
    elif libtype_ in ("duxiu_url","duxiu_file"): # from duxiu
        if libtype == "duxiu_url":
            instance = DownloadLib(lnp=lnp,pattern=pattern_for_duxiu_r,img_url_prex=img_url_prex,prex=prex,logfile=logfile)
        else:
            instance = DownloadLib(lnp=lnp,pattern=pattern_for_duxiu_l,img_url_prex=img_url_prex,prex=prex,logfile=logfile)
        if processes == 1:
            instance(libtype,arg)
        else:
            pool.map_async(multidownloadlib,instance.get_img_pairs(libtype,arg),processes)
            pool.close()
            pool.join()
    sys.exit(0)

import requests, bs4
import random, datetime
import base64
from binascii import hexlify
from Crypto.Cipher import AES
import json


class WangYiYun():
    def __init__(self):
        self.url = 'https://music.163.com'
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
        self.modulus = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
        self.nonce = '0CoJUm6Qyw8W8jud'
        self.pubKey = '010001'

    def get_Top(self):
        '''
        :return: 返回所有排行榜的字典列表
        '''
        res = requests.get('https://music.163.com/discover/toplist?', headers=self.headers)
        s = bs4.BeautifulSoup(res.text, 'html.parser')
        s=s.find_all('li', class_='mine')
        ls=[]
        for item in s:
            d=dict.fromkeys(('title','id'))
            d['title']=item.div.p.a.text
            d['id'] = item['data-res-id']
            ls.append(d)
        return ls

    def get_TopList(self, id):
        '''
        根据排行榜id获取里面排行榜的音乐
        :param url: id 网址里面id的值
        :return: 返回值如果有多个结果则是字典类型的列表
        '''
        res = requests.get(f'https://music.163.com/discover/toplist?id={id}', headers=self.headers)

        s = bs4.BeautifulSoup(res.text, 'html.parser')
        s = s.find('textarea', id="song-list-pre-data")
        j = json.loads(s.text)
        ls = []
        for item in j:
            d = dict.fromkeys(('name', 'id', 'artists', 'time'))
            d['name'] = item['name']
            d['id'] = item['id']
            d['artists'] = item['artists']
            time = datetime.timedelta(seconds=int(int(item['duration']) / 1000))
            d['time'] = str(time)
            ls.append(d)
        return ls

    def search_music(self, s):
        '''
        通过关键字搜索音乐
        :param s: 关键字
        :return: 返回值如果有多个结果则是字典类型的列表
        '''
        text = {"hlpretag": "<span class='s-fc7'>", "hlposttag": "</span>", "s": s, "type": "1", "offset": "0",
                "total": "true", "limit": "100", "csrf_token": ""}
        secKey = self.getRandom()
        text = json.dumps(text)
        params = self.aesEncrypt(self.aesEncrypt(text, self.nonce), secKey)
        encSecKey = self.rsaEncrypt(secKey)
        data = {'params': params,
                'encSecKey': encSecKey
                }
        res = requests.post(f'https://music.163.com/weapi/cloudsearch/get/web', data=data,
                            headers=self.headers)
        j = json.loads(res.text)
        j = j['result']['songs']
        ls = []
        for item in j:
            d = dict.fromkeys(('name', 'ar', 'al', 'id'))
            d['name'] = item['name']  # 歌名
            d['ar'] = item['ar']  # 作者列表
            d['al'] = item['al']  # 专辑
            d['id'] = item['id']  # 歌曲播放页面id
            ls.append(d)
        return ls

    def get_music_url(self, id):
        '''
        通过音乐id获取真实下载和播放链接
        :param s: 歌曲id 文本型  可以有多个 用逗号分隔
        :return: 返回值如果有多个结果则是字典类型的列表
        '''
        text = {"ids": f"[{id}]", "level": "standard", "encodeType": "aac", "csrf_token": ""}
        secKey = self.getRandom()
        text = json.dumps(text)
        params = self.aesEncrypt(self.aesEncrypt(text, self.nonce), secKey)
        encSecKey = self.rsaEncrypt(secKey)
        data = {'params': params,
                'encSecKey': encSecKey
                }
        try:
            res = requests.post('https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token=', data=data,headers=self.headers)
            j = json.loads(res.text)
            return j['data']['url']
        except:
            return ""
    def getRandom(self):
        '''
        取16位的随机字符
        :return: 返回一串16位的随机字符
        '''
        str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
        random_str = '';
        for i in range(16):
            index = random.randint(0, len(str) - 1);
            random_str += str[index];
        return random_str;

    def aesEncrypt(self, text, secKey):
        '''
        aes加密
        :param text: 要加密的文本
        :param secKey: 秘钥
        :return: 加密后的文本
        '''
        pad = 16 - len(text) % 16
        text = text + pad * chr(pad)
        text = text.encode('utf-8')
        encryptor = AES.new(bytes(secKey.encode('utf-8')), 2, b'0102030405060708')
        ciphertext = encryptor.encrypt(text)
        ciphertext = base64.b64encode(ciphertext).decode("utf-8")
        return ciphertext

    def rsaEncrypt(self, text):  # text是16位的随机字符串
        '''
        rsa加密
        :param text: 要加密的文本
        :return: 返回加密后的文本
        '''
        text = text[::-1];
        result = pow(int(hexlify(text.encode()), 16), int(self.pubKey, 16), int(self.modulus, 16));
        return format(result, 'x').zfill(131);

    def getParam(self, text):
        '''
        通过加密后的文本运算得出提交的params和encSecKey数据
        :param text:
        :return: 返回需要提交的params和encSecKey数据
        '''
        secKey = self.getRandom()
        params = self.aesEncrypt(self.aesEncrypt(text, secKey), self.nonce)
        encSecKey = self.rsaEncrypt(secKey, self.pubKey, self.modulus)
        return params, encSecKey

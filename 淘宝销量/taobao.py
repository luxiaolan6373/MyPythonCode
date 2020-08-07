import requests
import json
import re
def open_url(keyword,page=1):
    #s=0表示第一个商品 s=44是第二页
    #sort=sale-desc表示按销量排行
    payload={'q':keyword,'s':str((page-1)*44),'sort':'sale-desc'}
    url = "https://s.taobao.com/search"
    headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
               "cookie":"t=c0069c948c0c5b9ff3078e7b171e876a; cna=W8iZFyejNhgCAW9L5HlUexG4; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; cookie2=1a4384af429734dd4fd7a7d50a37f2e7; _tb_token_=e5bff3e1e7de7; v=0; _samesite_flag_=true; sgcookie=EdoHGaBBfQ5ULPDUx582t; unb=2659928092; uc3=lg2=UtASsssmOIJ0bQ%3D%3D&vt3=F8dBxGPiBrl6kwGHeVY%3D&id2=UU6kWrFsFJWaog%3D%3D&nk2=0vqsM%2FLL79BRdJTc; csg=6d6fa94f; lgc=%5Cu7B28%5Cu732A%5Cu732A%5Cu722C%5Cu6811%5Cu5427; cookie17=UU6kWrFsFJWaog%3D%3D; dnk=%5Cu7B28%5Cu732A%5Cu732A%5Cu722C%5Cu6811%5Cu5427; skt=f20be4f527f69c40; existShop=MTU5NTM0NDU0MA%3D%3D; uc4=id4=0%40U2xpWMrcYnG4dWR7qFsW6S20h8q0&nk4=0%400EsjHIZeLevAepS%2BIhd5c09cagAINq8%3D; tracknick=%5Cu7B28%5Cu732A%5Cu732A%5Cu722C%5Cu6811%5Cu5427; _cc_=U%2BGCWk%2F7og%3D%3D; _l_g_=Ug%3D%3D; sg=%E5%90%A72d; _nk_=%5Cu7B28%5Cu732A%5Cu732A%5Cu722C%5Cu6811%5Cu5427; cookie1=B0Fi%2FFib%2FVEZ9dlHKwT0qKiixRCxjRY4Tt%2FhaZuiKjo%3D; enc=j%2Bh97oXHR%2BMQ7WTtAqQjbt5iniS0eSK%2Bcj%2BiC3nCUveyEF9PLNjijm6aeRV30oRISNfiTWW%2FZY4rXjxhnXBbgw%3D%3D; __guid=154677242.3400814625193444000.1595344544441.4246; mt=ci=3_1; tfstk=cCHdBVc8xFY3nSrt0XdgP8scMctcZ9T85Male3q1CO99Gk6RixDmHwzwOuwRahC..; JSESSIONID=D8F2DF55A988E9E466268B86464199B0; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; monitor_count=7; l=eBxcJ8arOTyCM-vbBO5ZPurza77tnIRbzsPzaNbMiInca6Gl6F1s-NQqEAnXJdtjgtCbEexzYAkGMdUH5OUKvxDDBexrCyConxvO.; isg=BGNjU5UBOF0usPRrx1xpfG1A8qcNWPeaIpjDoZXAOUI51IH2HyqH6j_MyqRa9E-S; uc1=cookie21=URm48syIYB3rzvI4Dim4&pas=0&cookie15=V32FPkk%2Fw0dUvg%3D%3D&cookie16=VFC%2FuZ9az08KUQ56dCrZDlbNdA%3D%3D&cookie14=UoTV6e6HG3F0Fg%3D%3D&existShop=false",
               }
    res=requests.get(url,params=payload,headers=headers)
    print(res.url)
    return res
def get_items(res):
    # 用正则表达式 提取中间的json数据 调用file.read可以直接读取内容

    g_page_config = re.search(r"g_page_config = (.*?);\n", res.text)
    # 把字符串内容转换成json类型 group(1)就是不要前缀和后缀的东西只要中间的内容
    g_page_config_json = json.loads(g_page_config.group(1))
    page_items=g_page_config_json['mods']['itemlist']['data']['auctions']
    results=[]#挣来出我们要的数据(id,标题,链接,售价,销量,商家)
    for each_item in page_items:
        #创建一个字典的列表
        dict1=dict.fromkeys(('nid','title','detail_url','view_price',"view_sales",'nick'))
        dict1['nid']=each_item['nid']
        dict1['title'] = each_item['title']
        dict1['detail_url'] = each_item['detail_url']
        dict1['view_price'] = each_item['view_price']
        dict1['view_sales'] = each_item['view_sales']
        dict1['nick'] = each_item['nick']
        #将字典数据加入进列表
        results.append(dict1)
    return results#返回结果字典
def count_sales(items):
    count=0
    for each in items:
        #如果标题中包含 '小甲鱼则进行计算
        if '小甲鱼' in each['title']:
            #用正则表达式提取数字
            count+=int(re.search(r'\d+',each['view_sales']).group())
    return count#把销量结果返回
def main():
    keyword=input("请输入关键字:")
    #页数
    pageL=3
    total=0
    for i in range(pageL):
        #搜索,并且返回网页内容
        res=open_url(keyword,i+1)
        #用json提取需要的数据
        items=get_items(res)
        #计算最后的结果
        total+=count_sales(items)
    print("总销量是",total)
if __name__=="__main__":
    main()
import requests
import json
def get_hot_comments(res):
    comments_json=json.loads(res.text)
    hot_comments=comments_json['hotComments']
    with open(r'C:\Users\Administrator\Desktop\hot_comments.txt','w',encoding="utf-8") as file:
        for each in hot_comments:
            file.write(each['user']['nickname']+":\n\n")
            file.write(each['content']+'\n')
            file.write("--------------------------------\n")
def get_comments(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWe"
                      "bKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "referer":url}
    data={"params": "3ru/uWidMxbFyXvGq8vH/56mIPG46SI5URaUqT3VH0qWythMwznzzXeXFkgBDdGY6Lqjtz/+RQrb20GExb+TZEIf1msjIrHgMNK/RjjNDxGY3iWZbdv9HKGtLKFoRoYRFLwc21gjoeb3BWcFxLqwwVhUc5Y7PltzToCHgHd9cV3wF0wZKmxeO22CgaRIysP74A1M269oAvBAbCrMzJEREMmMK6uX+/X43lV+8hd38xFCppHd0bUi8l+7DrsSNtmcFOiAthQvlKUo/HUi1w1RHQbwcYtc4HaHwi0h6JS3g0k=",
        "encSecKey": "37b9a576c319fac1611538ae82d6da81d78ec7ef0aa7b3a35b46d0dff2b75f7e9c7b3d1ffa74fa98dc62bcd15c9b395ff1790d6280e2f0f8a1a4b3bc4262e710776b99671b975c80436b0b0a60f5affc34690b9359be933459648a0bcdabf2d4a6a5262affdbd77de616ff0a9fa6dadb9bb3f5e4750b8b3cc99ec0630e7e455d"}
    name_id = url.split('=')[1]
    target_url= "http://music.163.com/weapi/v1/resource/comments/R_SO_4_{}?csrf_token=".format(name_id)
    res = requests.post(target_url, headers=headers,data=data)
    return res
def main():
    url=input("请输入链接地址：")
    res=get_comments(url)
    get_hot_comments(res)
if __name__=="__main__":
    main()
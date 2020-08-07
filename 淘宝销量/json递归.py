import json
import re
def get_space_end(level):
    return " "*level+"_"
def get_space_expand(level):
    return " "*level+"+"
def find_keys(targets,level):
    keys=iter(targets)#将数据转换成迭代器
    for each in keys:
        #如果它的子集不是字典,说明到头了是最后一层
        print()
        if type(targets[each]) is not dict:
            #是最后一层就直接输出就好
            print(get_space_end(level)+each)
        else:
            next_level=level+1#既然还是字典那说明是还有子集的,多加一次空格
            print(get_space_expand(level)+each)
            #继续递归,并且将当前的最上级和空格情况传递
            find_keys(targets[each],next_level)

def main():
    #打开一个文件,然后赋值到变量file中
    with open(r'C:\Users\Administrator\Desktop\taobao.txt','r',encoding="utf-8")as file:
        #用正则表达式 提取中间的json数据 调用file.read可以直接读取内容
        g_page_config=re.search(r"g_page_config = (.*?);\n",file.read())
        #把字符串内容转换成json类型 group(1)就是不要前缀和后缀的东西只要中间的内容
        g_page_config_json=json.loads(g_page_config.group(1))
        find_keys(g_page_config_json,1)
if __name__=="__main__":
    main()
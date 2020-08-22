import execjs


def encodes(kw):
    path='1.js'
    with open(path, 'r', encoding='utf-8') as f:
        js = f.read()
        cx_js = execjs.compile(js)
        # 调用call方法去执行js代码
        a = cx_js.call("test", "美丽的神话")  # 第一个为函数名，后面的为参数，多的就用逗号隔开
    return a
print(encodes("nihao"))
#主动引发异常
raise ZeroDivisionError("除数为0的异常")

name=input("请输入文件名:")
try:
    1+'1'
    f = open(name, 'rb')
    print(f)

except OSError as reason:
    print("文件出错了!"+str(reason))
except TypeError as reason:
    print("类型错误!" + str(reason))
#也支持这样写
except(TypeError,OSError):
    print("出错了!")
finally:#无论如何都会执行的
    f.close()





2
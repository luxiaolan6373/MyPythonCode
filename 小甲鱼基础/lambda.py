#匿名函数表达式 lambda 参数1,参数2 : 过程
g= lambda x:2*x+1

#flter 可以过滤掉 函数运行结果返回值=False 或者0 None 的结果

print(list(filter(lambda x:x%2,range(10))))

#map 创建一个迭代器,去调用函数.输出所有结果
print(list(map(lambda x:x*2,range(10))))
import sys as s
#设置递归的层数
#s.setrecursionlimit(100)

def factorial(n):
    if n==1:
        #出口
        return 1
    else:
        return n*factorial(n-1)
number=int(input("请输入了一个正整数:"))
result=factorial(number)
print("%d 的阶乘是:%d"%(number,result))

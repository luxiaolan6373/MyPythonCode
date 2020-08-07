count=5
def Myfun():
    #标记一下说明是使用全局的count变量
    global count
    count=10
    print(10)

def fun1():
    print("fun1正在被调用")
    def fun2():
        print("fun2正在被调用")
    fun2()

fun1()
#fun2只能是fun内部调用,外部不能直接调用


def Fun1():
    x=5
    def Fun2():
        #标记告诉它不是局部变量,而是上一级的变量
        nonlocal x
        x*=x
        return x
    return Fun2()

print(Fun1())




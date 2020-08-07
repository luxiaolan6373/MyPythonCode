from turtle import *


def my_goto(x, y):
    penup()
    goto(x, y)
    pendown()


def eyes():
    tracer(False)
    a = 2.5
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a -= 0.05
            lt(3)
            fd(a)
        else:
            a += 0.05
            lt(3)
            fd(a)
    tracer(True)


##鼻子
def nose():
    my_goto(-10, 150)
    fillcolor('#e70010')
    begin_fill()
    circle(20)
    end_fill()


##嘴巴
def mouth():
    my_goto(5, 145)
    seth(270)
    fd(100)
    seth(0)
    circle(120, 50)
    seth(230)
    circle(-120, 100)


##眼睛
def black_eyes():
    ## 左眼珠子
    seth(0)
    my_goto(-20, 195)
    fillcolor('#000000')
    begin_fill()
    circle(13)
    end_fill()
    pensize(6)
    ##右眼珠子
    my_goto(20, 205)
    seth(75)

    circle(-10, 150)
    pensize(3)
    my_goto(-17, 200)
    seth(0)
    fillcolor('#ffffff')
    begin_fill()

    circle(5)
    end_fill()
    my_goto(0, 0)


##围巾
def scarf():
    fillcolor("#e70010")
    begin_fill()
    seth(0)
    fd(200)
    circle(-5, 90)
    fd(10)
    circle(-5, 90)
    fd(207)
    circle(-5, 90)
    fd(10)
    circle(-5, 90)
    end_fill()


##胡须
def beard():
    ##    第一根
    my_goto(-37, 135)
    seth(165)
    fd(60)
    ##    第二根
    my_goto(-37, 125)
    seth(180)
    fd(60)
    ##    第三根
    my_goto(-37, 115)
    seth(193)
    fd(60)
    ##    第四根
    my_goto(37, 135)
    seth(15)
    fd(60)
    ##    第五根
    my_goto(37, 125)
    seth(0)
    fd(60)
    ##    第六根
    my_goto(37, 115)
    seth(-13)
    fd(60)


##脸
def face():
    seth(0)
    fd(180)
    fillcolor('#ffffff')
    begin_fill()
    lt(44)
    circle(120, 100)
    seth(90)
    eyes()
    seth(180)
    penup()
    fd(60)
    pendown()
    seth(90)
    eyes()
    penup()
    seth(180)
    fd(61)
    pendown()
    seth(215)
    circle(120, 100)
    end_fill()


##头部
def head():
    penup()
    circle(150, 40)
    pendown()
    fillcolor('#00a0de')
    begin_fill()
    circle(150, 280)
    end_fill()


##右手
def righthands():
    my_goto(200.8, 44.5)
    seth(50)
    fillcolor('#ffffff')
    begin_fill()
    circle(30)
    end_fill()


##左手
def lefthands():
    my_goto(-185, -65)
    seth(70)
    fillcolor('#ffffff')
    begin_fill()
    circle(-30)
    end_fill()


##脚
def foots():
    ##右脚
    my_goto(103.74, -182.59)
    seth(0)
    fillcolor('#ffffff')
    begin_fill()
    fd(15)
    circle(-15, 180)
    fd(90)
    circle(-15, 180)
    seth(0)
    fd(5)
    end_fill()

    ##左脚
    my_goto(-96.26, -182.59)
    seth(180)
    fillcolor('#ffffff')
    begin_fill()
    fd(15)
    circle(15, 180)
    fd(90)
    circle(15, 180)
    seth(0)
    fd(-5)
    end_fill()


##口袋
def pocket():
    ##    大环
    my_goto(-79, 14)
    seth(-120)
    begin_fill()
    circle(90, 240)
    end_fill()

    ##    小环
    seth(270)
    my_goto(-70, -23)
    circle(70, 180)
    seth(0)
    fd(-140)


##铃铛
def smallbell():
    my_goto(4.5, -5.5)
    fillcolor("#ffca0b")
    begin_fill()
    circle(18)
    end_fill()

    my_goto(-11, 16)
    seth(0)
    fd(30)
    circle(2, 180)
    seth(-180)
    fd(30)

    circle(2, 180)
    fillcolor('#000000')
    my_goto(4.5, 5)
    begin_fill()
    pensize(2)
    circle(3.5)
    end_fill()
    seth(92)
    fd(-11)


##    身体
def body():
    my_goto(0, 0)
    seth(0)
    penup()
    circle(150, 50)
    pendown()
    seth(30)
    fd(40)
    ##右手臂
    seth(70)
    circle(-30, 270)

    fillcolor('#00a0de')
    begin_fill()
    seth(230)
    fd(80)
    seth(90)
    circle(1000, 1)

    seth(-89)
    circle(-1000, 10)

    seth(180)
    fd(70)
    seth(90)
    circle(30, 180)
    seth(180)
    fd(70)

    ##左手臂
    seth(100)
    circle(-1000, 9)
    seth(92.5)
    fd(-77)

    circle(1000, 2)
    seth(230)
    fd(33)
    circle(-30, 230)
    seth(45)
    fd(83)
    seth(0)
    ##围巾和右手臂衔接处
    fd(200)
    circle(4, 90)
    fd(13)
    circle(4, 90)
    fd(7)
    seth(41)
    circle(150, 10)
    seth(30)
    fd(40)
    end_fill()


def Doraemon():
    # 头部
    head()

    ##围巾
    scarf()

    # 脸
    face()

    # 红鼻子
    nose()

    ##嘴巴
    mouth()

    ##胡须
    beard()

    # 身体
    body()

    # 右手
    righthands()

    ##脚
    foots()

    # 左手
    lefthands()

    ##眼睛
    black_eyes()

    ##口袋
    pocket()

    ##铃铛
    smallbell()


if __name__ == "__main__":
    screensize(800, 600, "#f0f0f0")
    pensize(3)  # 画笔宽度
    speed(11)  # 画笔速度
    Doraemon()
    my_goto(100, -300)
    write('Hi, I am A dream.', font=("Bradley Hand ITC", 30, "bold"))
    mainloop()

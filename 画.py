import turtle
import time as ti
t = turtle.Pen()
s = turtle.Screen()
 
def fd() :
    t.setheading(90)
    t.fd(20)
def bk() :
    t.setheading(270)
    t.fd(20)
def ltfd() :
    t.setheading(180)
    t.fd(20)
def rtfd() :
    t.setheading(0)
    t.fd(20)
def down() :
    t.pendown()
    t.write("已落笔",font=("楷体",25,"normal"))
    ti.sleep(0.2)
    t.undo()
def up() :
    t.penup()
    t.write("已抬笔",font=("楷体",25,"normal"))
    ti.sleep(0.2)
    t.undo()
def pco() :
    penco = s.textinput("pencolor","请输入笔的颜色：(示例:red,dodgerblue)")
    t.color(penco)
    s.listen()
def psi() :
    psiz = s.numinput("pensize","请输入笔的粗细：(数字)")
    t.pensize(psiz)
    s.listen()
def bco() :
    bgco = s.textinput("bgcolor","请输入背景色：(示例:red,white)")
    s.bgcolor(bgco)
    s.listen()
def undo() :
    t.undo()
    t.undo()
    t.write("撤销···",font=("楷体",25,"normal"))
    ti.sleep(0.2)
    t.undo()
def res() :
    t.reset()
    s.bgcolor("white")
    t.write("复位完毕···",font=("楷体",25,"normal"))
    ti.sleep(0.2)
    t.undo()
def exit() :
    t.write("欢迎下次使用!",font=("楷体",25,"normal"))
    ti.sleep(0.2)
    s.bye()

s.title("画板")
s.setup(width=1000,height=600,startx=0,starty=0)
t.speed(10)
s.onkeypress(fd,"Up")
s.onkeypress(bk,"Down")
s.onkeypress(ltfd,"Left")
s.onkeypress(rtfd,"Right")
s.onkey(pco,"c")
s.onkey(psi,"s")
s.onkey(bco,"b")
s.onkey(undo,"a")
s.onkey(res,"r")
s.onkey(exit,"e")
s.onkey(down,"d")
s.onkey(up,"u")
s.listen()
 
s.mainloop()

#制作:权家乐  想法提供:权家乐
#版权所有 侵权必究

"""=============================操作说明======================================
1.按“↑,↓,←,→”键对画笔进行移动。
2.按“U”键抬笔，可以这样记:抬笔是up，就按U。
3.按“D”键落笔，记忆法同上。
4.按“A”键撤销，将回到上一步。
5.按“R”复位，将更改背景色为白色，清除所有画迹，将画笔位置设为0,0。
    (注意:此操作也会清除所有撤销缓冲区，所以无法撤销！)
6.按“B”键更改背景色，形式为str。
7.按“C”键更改画笔色，形式同上。
8.按“S”键更改画笔粗细，形式为float。
    (整数也行。)
9.按“E”键退出。
    (你要是感觉没有什么用，不用也行。)"""

#这是我花了很长时间才做成的，不要不用他哦！

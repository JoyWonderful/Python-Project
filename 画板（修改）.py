import turtle
from tkinter.messagebox import *
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
    t.write("已落笔",font=("楷体",10,"normal"))
    ti.sleep(0.2)
    t.undo()
def up() :
    t.penup()
    t.write("已抬笔",font=("楷体",10,"normal"))
    ti.sleep(0.2)
    t.undo()
def pco() :
    try :
        penco = s.textinput("pencolor","请输入笔的颜色：(示例:red,dodgerblue)")
        t.color(penco)
    except Exception as e :
        showerror(e,"请输入正确的颜色英文！")
    finally :
        s.listen()
def psi() :
    try :
        psiz = s.numinput("pensize","请输入笔的粗细：(数字)")
        t.pensize(psiz)
    except Exception as e :
        showerror(e,"请输入数字！")
    finally :
        s.listen()
def bco() :
    try :
        bgco = s.textinput("bgcolor","请输入背景色：(示例:red,white)")
        s.bgcolor(bgco)
    except Exception as e :
        showerror(e,"请输入正确的英文单词！")
    finally :
        s.listen()
def undo() :
    t.undo()
    t.undo()
    t.write("撤销···",font=("楷体",10,"normal"))
    ti.sleep(0.2)
    t.undo()
def res() :
    t.reset()
    s.bgcolor("white")
    t.write("复位完毕···",font=("楷体",10,"normal"))
    ti.sleep(0.2)
    t.undo()
def exit() :
    t.write("欢迎下次使用!",font=("楷体",10,"normal"))
    ti.sleep(0.2)
    s.bye()
 
s.title("画板")
s.setup(width=500,height=400,startx=None,starty=None)
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
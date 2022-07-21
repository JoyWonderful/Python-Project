import tkinter as tk
from tkinter.filedialog import *
from tkinter import messagebox
root = tk.Tk()
 
global text_insert
text_insert = tk.Text(root,
                                    undo = True,autoseparators = False,yscrollcommand = True,
                                    width = 110,height = 30)
text_insert.grid(padx = 1,pady = 1,row = 0)
 
def open_file() :
    file_path = askopenfile(title = "打开",filetypes = [("纯文本文档",".txt"),("Python文件",".py"),("所有文件",".*")])
    messagebox.showinfo(file_path,file_path)
    with open (file_path.name,"r") as f :
        data = f.read()
        messagebox.showinfo(data,data)
        text_insert.edit_separator()
        text_insert.delete(1.0,"end")
        text_insert.insert("end",data)
def save_as_file() :
    file_path = asksaveasfile(title = "另存为",defaultextension = ".txt")
    messagebox.showinfo(file_path,file_path)
    with open (file_path.name,"w") as f :
        data = text_insert.get(1.0,"end")
        f.write(data)
        messagebox.showinfo("信息",file_path.name+"另存为成功！")
 
def text_undo() :
    text_insert.edit_undo()
def text_redo() :
    text_insert.edit_redo()
 
def copy() :
    def yes() :
        srt = en1.get()
        stp = en2.get()
        global text
        text = text_insert.get(float(srt),float(stp))
        messagebox.showinfo("提示",str(text))
        copy_win.destroy()
    copy_win = tk.Toplevel()
    copy_win.title("复制选项")
    info1 = tk.Label(copy_win,text = "请输入要复制的字符\n的列和行,形式为\"行.列\"")
    info1.grid(padx = 5,pady = 5,row = 0,column = 1)
    info2 = tk.Label(copy_win,text = "起始:")
    info2.grid(row = 1,column = 0)
    info3 = tk.Label(copy_win,text = "终止:")
    info3.grid(row = 2,column = 0)
    
    en1 = tk.Entry(copy_win,width = 5)
    en1.grid(row = 1,column = 2)
    en2 = tk.Entry(copy_win,width = 5)
    en2.grid(row = 2,column = 2)
    
    yes_btn = tk.Button(copy_win,text = "确定",command = yes)
    yes_btn.grid(row = 3,column = 0)
    no_btn = tk.Button(copy_win,text = "取消",command = copy_win.destroy)
    no_btn.grid(row = 3,column = 2)
def cut() :
    def yes() :
        srt = en1.get()
        stp = en2.get()
        global text
        text = text_insert.get(float(srt),float(stp))
        text_insert.edit_separator()
        text_insert.delete(float(srt),float(stp))
        messagebox.showinfo("提示",str(text))
        cut_win.destroy()
    cut_win = tk.Toplevel()
    cut_win.title("剪切选项")
    info1 = tk.Label(cut_win,text = "请输入你想剪切的字符\n的列和行，形式为\"行.列\"")
    info1.grid(padx = 5,pady = 5,row = 0,column = 1)
    info2 = tk.Label(cut_win,text = "起始:")
    info2.grid(row = 1,column = 0)
    info3 = tk.Label(cut_win,text = "终止:")
    info3.grid(row = 2,column = 0)
    
    en1 = tk.Entry(cut_win,width = 5)
    en1.grid(row = 1,column = 2)
    en2 = tk.Entry(cut_win,width = 5)
    en2.grid(row = 2,column = 2)
    
    yes_btn = tk.Button(cut_win,text = "确定",command = yes)
    yes_btn.grid(row = 3,column = 0)
    no_btn = tk.Button(cut_win,text = "取消",command = cut_win.destroy)
    no_btn.grid(row = 3,column = 2)
def paste() :
    text_insert.edit_separator()
    text_insert.insert("insert",text)
 
def help() :
    help_win = tk.Toplevel()
    tk.Label(help_win,text = "文档编辑器").grid(padx = 2,pady = 2)
    tk.Label(help_win,text = "您可以查看，修改，编辑文档。\n").grid()
    tk.Button(help_win,text = "关闭",command = help_win.destroy).grid(pady = 1)
    help_win.title("帮助")
def about() :
    about_win = tk.Toplevel()
    tk.Label(about_win,text = "文档编辑器",font = ("楷体",20,"normal")).grid(padx = 2,pady = 2)
    tk.Label(about_win,text = "\nCopyright 版权所有 © JoyWonderful 2022 保留所有权利\nAll Rights Served.\n").grid()
    tk.Button(about_win,text = "关闭",command = about_win.destroy).grid(pady = 1)
    about_win.title("关于")
 
 
main_menu = tk.Menu(root)
 
f_menu = tk.Menu(main_menu,tearoff = False)
f_menu.add_command(label = "新建",accelerator = "Ctrl + N")
f_menu.add_command(label = "打开...",accelerator = "Ctrl + O",command = open_file)
f_menu.add_command(label = "保存",accelerator = "Ctrl + S")
f_menu.add_command(label = "另存为...",accelerator = "Ctrl + Shift + S",command = save_as_file)
f_menu.add_separator()
f_menu.add_command(label = "退出",command = root.quit)
main_menu.add_cascade(label = "文件",menu = f_menu)
 
e_menu = tk.Menu(main_menu,tearoff = False)
e_menu.add_command(label = "撤销",accelerator = "Ctrl + B",command = text_undo)
e_menu.add_command(label = "恢复",accelerator = "Ctrl + R",command = text_redo)
e_menu.add_separator()
e_menu.add_command(label = "复制",accelerator = "Ctrl + C",command = copy)
e_menu.add_command(label = "剪切",accelerator = "Ctrl + X",command = cut)
e_menu.add_command(label = "粘贴",accelerator = "Ctrl + V",command = paste)
main_menu.add_cascade(label = "编辑",menu = e_menu)
 
h_menu = tk.Menu(root)
h_menu.add_command(label = "帮助...",accelerator = "F1",command = help)
h_menu.add_command(label = "关于...",command = about)
main_menu.add_cascade(label = "帮助",menu = h_menu)
 
 
mouse_menu = tk.Menu(root,tearoff = False)
mouse_menu.add_command(label = "复制...",accelerator = "Ctrl + C",command = copy)
mouse_menu.add_command(label = "剪切...",accelerator = "Ctrl + X",command = cut)
mouse_menu.add_command(label = "粘贴",accelerator = "Ctrl + V",command = paste)
 
def mouse_pos(event) :
    mouse_menu.post(event.x_root,event.y_root)
 
 
root.title("文本")
 
root.config(menu = main_menu)
 
root.bind("<Button-3>",mouse_pos)
root.bind("<Control - o>",open_file)
root.bind("<Control - O>",open_file)
root.bind("<Control - Shift - s>",save_as_file)
root.bind("<Control - Shift - S>",save_as_file)
root.bind("<Control - b>",text_undo)
root.bind("<Control - B>",text_undo)
root.bind("<Control - R>",text_redo)
root.bind("<Control - c>",copy)
root.bind("<Control - C>",copy)
root.bind("<Control - x>",cut)
root.bind("<Control - X>",cut)
root.bind("<Control - v>",paste)
root.bind("<Control - V>",paste)
 
root.mainloop()
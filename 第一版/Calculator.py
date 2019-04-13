# -*- coding:utf-8 -*-
import tkinter as tk
import tkinter.messagebox
import math

root = tk.Tk()
root.geometry('330x320')
root.resizable()
root.title("什么都算不出来的计算器")
#背景图片
photo= tk.PhotoImage(file=r"C:\Users\Bya\Desktop\PY\Gui\2.gif")
theLaber2 = tk.Label(root,justify=tk.LEFT,image=photo,compound=tk.CENTER)
#compound=center为混合属性
theLaber2.pack()


v = tk.StringVar(root,'')
tk.Entry(root,textvariable=v,state='readonly',font=("Arial", 12)).place(x=10,y=10,width=320,height=40)
def buttonClick(btn):
    content = v.get()
    if content.startswith('.'):
        content = '0'+content

#小数点功能还未写
    elif btn=='=':
        try:
            content = str((eval(content)))#eval可以进行浮点数运算
        except:
            tk.messagebox.showerror('出错啦','表达式错误！')
            return
    elif btn in '0123456789':
        content+=btn
    elif btn=='AC':
        content=''
    # elif btn=='Back':#回退功能还没实现
    #     if len(content)<0:
    #         tk.messagebox.showerror('出错啦', '不允许出现连续的操作符！')
    #     else:
    #



    elif btn in operators:
        if content.endswith(operators):#endswith只能接受列表或元祖
            tk.messagebox.showerror('出错啦','不允许出现连续的操作符！')
            return
        else:
            content+=btn
    elif btn=='%':
        content+=btn
    elif btn=='Sqrt':
            content = eval(content)**0.5
#平方根需完善



    v.set(content)

button = ['AC','Sqrt','%',]+list('7894561230')+['.','Back']
index = 0
for row in range(5):
    for col in range(3):
        btn = button[index]
        index+=1
        btnDigit = tk.Button(root,text=btn,command=lambda x=btn:buttonClick(x),bg="DimGray",relief='flat',font=("Arial", 16),fg='White').place(x=20+col*80,y=80+row*50,width=50,height=20)
operators = ('/','*','-','+','=')
for index,operator in enumerate(operators):#enumerate进行列表元祖的遍历，可以返回值和对应的下标
    btnOpera = tk.Button(root,text=operator,command=lambda x=operator:buttonClick(x),bg='DarkOrange',relief='raised',font=("Helvetica", 16),fg='White').place(x=250,y=80+index*50,width=50,height=20)

root.mainloop()
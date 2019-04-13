#!/usr/bin/env python
__author__: "Jhze dnowz"

import tkinter as tk
import tkinter.messagebox
import re

root = tk.Tk()
root.minsize(280, 400)
root.resizable(0, 0)
root.title('计算器')


# 数字键按钮
btn7 = tkinter.Button(root, text='7', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
        x='7': buttonClick(x))
btn7.place(x=0, y=185, width=70, height=55)
btn8 = tkinter.Button(root, text='8', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
        x='8': buttonClick(x))
btn8.place(x=70, y=185, width=70, height=55)
btn9 = tkinter.Button(root, text='9', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
        x='9': buttonClick(x))
btn9.place(x=140, y=185, width=70, height=55)

btn4 = tkinter.Button(root, text='4', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
        x='4': buttonClick(x))
btn4.place(x=0, y=240, width=70, height=55)
btn5 = tkinter.Button(root, text='5', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
        x='5': buttonClick(x))
btn5.place(x=70, y=240, width=70, height=55)
btn6 = tkinter.Button(root, text='6', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
        x='6': buttonClick(x))
btn6.place(x=140, y=240, width=70, height=55)

btn1 = tkinter.Button(root, text='1', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
        x='1': buttonClick(x))
btn1.place(x=0, y=295, width=70, height=55)
btn2 = tkinter.Button(root, text='2', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
        x='2': buttonClick(x))
btn2.place(x=70, y=295, width=70, height=55)
btn3 = tkinter.Button(root, text='3', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
        x='3': buttonClick(x))
btn3.place(x=140, y=295, width=70, height=55)
btn0 = tkinter.Button(root, text='0', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
        x='0': buttonClick(x))
btn0.place(x=70, y=350, width=70, height=55)

# 运算符号按钮
btnac = tkinter.Button(root, text='AC', bd=0.5, font=('黑体', 20), fg='orange', command=lambda \
        x='AC': buttonClick(x))
btnac.place(x=0, y=130, width=70, height=55)
btnback = tkinter.Button(root, text='←', font=('微软雅黑', 20), fg='#4F4F4F', bd=0.5, command=lambda \
        x='←': buttonClick(x))
btnback.place(x=70, y=130, width=70, height=55)
btndivi = tkinter.Button(root, text='^', font=('微软雅黑', 20), fg='#4F4F4F', bd=0.5, command=lambda \
        x='^': buttonClick(x))
btndivi.place(x=140, y=130, width=70, height=55)
btnmul = tkinter.Button(root, text='+', font=('微软雅黑', 20), fg="#4F4F4F", bd=0.5, command=lambda \
        x='+': buttonClick(x))
btnmul.place(x=210, y=130, width=70, height=55)
btnsub = tkinter.Button(root, text='-', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
        x='-': buttonClick(x))
btnsub.place(x=210, y=185, width=70, height=55)
btnadd = tkinter.Button(root, text='×', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
        x='×': buttonClick(x))
btnadd.place(x=210, y=240, width=70, height=55)
btnequ = tkinter.Button(root, text='÷', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
        x='÷':buttonClick(x))
btnequ.place(x=210, y=295, width=70, height=55)
btnequ = tkinter.Button(root, text='=', bg='orange', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5,
                        command=lambda x='=': buttonClick(x))
btnequ.place(x=210, y=350, width=70, height=55)

btnper = tkinter.Button(root, text='高级', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, )
btnper.place(x=0, y=350, width=70, height=55)
btnpoint = tkinter.Button(root, text='.', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
        x='.': buttonClick(x))
btnpoint.place(x=140, y=350, width=70, height=55)

contentVar = tk.StringVar(root, '')
contentEntry = tk.Entry(root, textvariable=contentVar, state='readonly', font=("Arial", 12))
contentEntry.place(x=0, y=90, width=280, height=40)

def buttonClick(btn):
    content = contentVar.get()
    if content.startswith('.'):  # 小数点前加0
        content = '0' + content
    if btn in '0123456789':
        content += btn
    elif btn == '.':
        lastPart = re.split(r'\+|-|\*|/', content)[-1]
        if '.' in lastPart:
            tk.messagebox.showerror('错误', 'Input Error')
            return
        else:
            content += btn

    elif btn == 'AC':
        content = ''
    elif btn == '=':
        try:
            for operat in content:
                if operat =='÷':
                    content = content.replace('÷', '/')
                elif operat == '×':
                    content = content.replace('×', '*')
            content = str(eval(content))
        except:
            tk.messagebox.showerror('错误', 'VALUE ERROR')
            return
    elif btn in operators:
        if content.endswith(operators):
            tk.messagebox.showerror('错误', 'FORMAT ERROR')
            return
        content += btn
    elif btn == '^':
        n = content.split('.')
        if all(map(lambda x: x.isdigit(), n)):
            content = eval(content) ** eval(content)
        else:
            tk.messagebox.showerror('错误', 'Input Error')
            return
    if btn =='←':                 #如果按下的是退格‘’，则选取当前数字第一位到倒数第二位
        content = content[0:-1]

    contentVar.set(content)

operators = ('÷','×','-','+','=','.')

root.mainloop()

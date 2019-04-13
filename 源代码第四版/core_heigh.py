#!/usr/bin/env python
__author__: "Jhze dnowz"
import tkinter as tk
import tkinter.messagebox
import re
from function import *


def trigger(root):
    ro = tk.Tk()
    ro.minsize(280, 345)
    ro.resizable(0, 0)
    ro.title('计算器')

    # 数字键按钮
    btnx = tkinter.Button(ro, text='X!', font=('微软雅黑', 20), bg=('#96CDCD'),fg=('#4F4F4F'), bd=0.5, command=lambda \
            x='X!': buttonClick(x))
    btnx.place(x=0, y=185, width=56, height=40)
    btn7 = tkinter.Button(ro, text='7', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
            x='7': buttonClick(x))
    btn7.place(x=56, y=185, width=56, height=40)
    btn8 = tkinter.Button(ro, text='8', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
            x='8': buttonClick(x))
    btn8.place(x=112, y=185, width=56, height=40)
    btn9 = tkinter.Button(ro, text='9', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
            x='9': buttonClick(x))
    btn9.place(x=168, y=185, width=56, height=40)

    btn4x = tkinter.Button(ro, text='1/X', font=('微软雅黑', 20), bg=('#96CDCD'), fg=('#4F4F4F'), bd=0.5, command=lambda \
            x='1/X': buttonClick(x))
    btn4x.place(x=0, y=225, width=56, height=40)
    btn4 = tkinter.Button(ro, text='4', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
            x='4': buttonClick(x))
    btn4.place(x=56, y=225, width=56, height=40)
    btn5 = tkinter.Button(ro, text='5', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
            x='5': buttonClick(x))
    btn5.place(x=112, y=225, width=56, height=40)
    btn6 = tkinter.Button(ro, text='6', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
            x='6': buttonClick(x))
    btn6.place(x=168, y=225, width=56, height=40)

    btnpi = tkinter.Button(ro, text='π', font=('微软雅黑', 20),bg=('#96CDCD'), fg=('#4F4F4F'), bd=0.5, command=lambda \
            x='π': buttonClick(x))
    btnpi.place(x=0, y=265, width=56, height=40)
    btn1 = tkinter.Button(ro, text='1', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
            x='1': buttonClick(x))
    btn1.place(x=56, y=265, width=56, height=40)
    btn2 = tkinter.Button(ro, text='2', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
            x='2': buttonClick(x))
    btn2.place(x=112, y=265, width=56, height=40)
    btn3 = tkinter.Button(ro, text='3', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
            x='3': buttonClick(x))
    btn3.place(x=168, y=265, width=56, height=40)
    btn0 = tkinter.Button(ro, text='0', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
            x='0': buttonClick(x))
    btn0.place(x=112, y=305, width=56, height=40)

    btnxsec = tkinter.Button(ro, text='sec', font=('微软雅黑', 20),bg=('#96CDCD'), fg=('#4F4F4F'), bd=0.5, command=lambda \
            x='sec': buttonClick(x))
    btnxsec.place(x=0, y=105, width=56, height=40)
    btnlog = tkinter.Button(ro, text='lg', font=('微软雅黑', 20),bg=('#96CDCD'), fg=('#4F4F4F'), bd=0.5, command=lambda \
            x='lg': buttonClick(x))
    btnlog.place(x=56, y=105, width=56, height=40)
    btnln = tkinter.Button(ro, text='㏑', font=('微软雅黑', 20),bg=('#96CDCD'), fg=('#4F4F4F'), bd=0.5, command=lambda \
            x='㏑': buttonClick(x))
    btnln.place(x=112, y=105, width=56, height=40)
    btnleft = tkinter.Button(ro, text='(', font=('微软雅黑', 20),bg=('#96CDCD'), fg=('#4F4F4F'), bd=0.5, command=lambda \
            x='(': buttonClick(x))
    btnleft.place(x=168, y=105, width=56, height=40)
    btnrigh = tkinter.Button(ro, text=')', font=('微软雅黑', 20),bg=('#96CDCD'), fg=('#4F4F4F'), bd=0.5, command=lambda \
            x=')': buttonClick(x))
    btnrigh.place(x=224, y=105, width=56, height=40)

    btncsc = tkinter.Button(ro, text='csc', font=('微软雅黑', 20),bg=('#96CDCD'), fg=('#4F4F4F'), bd=0.5, command=lambda \
            x='csc': buttonClick(x))
    btncsc.place(x=0, y=65, width=56, height=40)
    btnrad = tkinter.Button(ro, text='rad', font=('微软雅黑', 20), bg=('#96CDCD'),fg=('#4F4F4F'), bd=0.5, command=lambda \
            x='rad': buttonClick(x))
    btnrad.place(x=56, y=65, width=56, height=40)
    btnsin = tkinter.Button(ro, text='sin', font=('微软雅黑', 20), bg=('#96CDCD'),fg=('#4F4F4F'), bd=0.5, command=lambda \
            x='sin': buttonClick(x))
    btnsin.place(x=112, y=65, width=56, height=40)
    btncos = tkinter.Button(ro, text='cos', font=('微软雅黑', 20),bg=('#96CDCD'), fg=('#4F4F4F'), bd=0.5, command=lambda \
            x='cos': buttonClick(x))
    btncos.place(x=168, y=65, width=56, height=40)
    btntan = tkinter.Button(ro, text='tan', font=('微软雅黑', 20),bg=('#96CDCD'), fg=('#4F4F4F'), bd=0.5, command=lambda \
            x='tan': buttonClick(x))
    btntan.place(x=224, y=65, width=56, height=40)

    # 运算符号按钮
    btnac = tkinter.Button(ro, text='x^y', bd=0.5, font=('黑体', 20), bg=('#96CDCD'), command=lambda \
            x='x^y': buttonClick(x))
    btnac.place(x=0,y=145,width=56, height=40)
    btnac = tkinter.Button(ro, text='AC', bd=0.5, font=('黑体', 20), fg='orange', command=lambda \
            x='AC': buttonClick(x))
    btnac.place(x=56, y=145, width=56, height=40)
    btnback = tkinter.Button(ro, text='←', font=('微软雅黑', 20), fg='#4F4F4F', bd=0.5, command=lambda \
            x='←': buttonClick(x))
    btnback.place(x=112, y=145, width=56, height=40)
    btndmod = tkinter.Button(ro, text='%', font=('微软雅黑', 20), fg='#4F4F4F', bd=0.5, command=lambda \
            x='%': buttonClick(x))
    btndmod.place(x=168, y=145, width=56, height=40)
    btnmul = tkinter.Button(ro, text='+', font=('微软雅黑', 20), fg="#4F4F4F", bd=0.5, command=lambda \
            x='+': buttonClick(x))
    btnmul.place(x=224, y=145, width=56, height=40)
    btnsub = tkinter.Button(ro, text='-', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
            x='-': buttonClick(x))
    btnsub.place(x=224, y=185, width=56, height=40)
    btnadd = tkinter.Button(ro, text='×', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
            x='×': buttonClick(x))
    btnadd.place(x=224, y=225, width=56, height=40)
    btnequ = tkinter.Button(ro, text='÷', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
            x='÷': buttonClick(x))
    btnequ.place(x=224, y=265, width=56, height=40)
    btnequ = tkinter.Button(ro, text='=', bg='orange', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5,
                            command=lambda x='=': buttonClick(x))
    btnequ.place(x=224, y=305, width=56, height=40)

    btnper = tkinter.Button(ro, text='低级', font=('微软雅黑', 20), fg='orange', bd=0.5,
                            command=lambda x='低级': buttonClick(x))
    btnper.place(x=0, y=305, width=56, height=40)
    btne = tkinter.Button(ro, text='e', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5,
                            command=lambda x='e': buttonClick(x))
    btne.place(x=56, y=305, width=56, height=40)
    btnpoint = tkinter.Button(ro, text='.', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
            x='.': buttonClick(x))
    btnpoint.place(x=168, y=305, width=56, height=40)

    contentVar = tk.StringVar(ro, '')
    contentEntry = tk.Entry(ro, textvariable=contentVar, state='readonly', font=("Arial", 12))
    contentEntry.place(x=0, y=10, width=280, height=40)

    def buttonClick(btn):
        content = contentVar.get()
        if content.startswith('.'):  # 小数点前加0
            content = '0' + content
        if btn in '0123456789()':
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
                    if operat == '÷':
                        content = content.replace('÷', '/')
                    elif operat == '×':
                        content = content.replace('×', '*')
                    elif operat == '^':
                        content = content.replace('^', '**')
                if 'sin' in content:
                    content = re.findall("\d+", content)[0]
                    value = sin_t(float(content))
                    content = str(value)
                if 'cos' in content:
                    content = re.findall("\d+", content)[0]
                    value = cos_t(float(content))
                    content = str(value)
                if 'tan' in content:
                    content = re.findall("\d+", content)[0]
                    value = tan_t(float(content))
                    content = str(value)
                if 'sec' in content:
                    content = re.findall("\d+", content)[0]
                    value = sec_t(float(content))
                    content = str(value)
                if 'csc' in content:
                    content = re.findall("\d+", content)[0]
                    value = csc_t(float(content))
                    content = str(value)
                if 'lg' in content:
                    content = re.findall("\d+", content)[0]
                    value = lg_t(float(content))
                    content = str(value)
                if '㏑' in content:
                    content = re.findall("\d+", content)[0]
                    value = ln_t(float(content))
                    content = str(value)
                else:
                    value = eval(content)
                    content = str(round(value, 10))
            except:
                tk.messagebox.showerror('错误', 'VALUE ERROR')
                return
        elif btn in operators:
            if content.endswith(operators):
                tk.messagebox.showerror('错误', 'FORMAT ERROR')
                return
            content += btn
        # elif btn == '^':
        #     n = content.split('.')
        #     if all(map(lambda x: x.isdigit(), n)):
        #         content = eval(content) * eval(content)
        #     else:
        #         tk.messagebox.showerror('错误', 'Input Error')
        #         return
        elif btn == 'e':
            content = 2.7182818284
        elif btn == 'π':
            content = 3.1415926535
        elif btn == '1/X':
            content = reciprocal(float(content))
        elif btn =='X!':
            content = factorial(int(content))
        elif btn =='x^y':
            content +='^'
        elif btn =='sin':
            content +='sin('
        elif btn =='cos':
            content +='cos('
        elif btn =='tan':
            content +='tan('
        elif btn =='sec':
            content +='sec('
        elif btn =='csc':
            content +='csc('
        elif btn =='lg':
            content+='lg('
        elif btn =='㏑':
            content+='㏑('
        elif btn == '←':  # 如果按下的是退格‘’，则选取当前数字第一位到倒数第二位
            content = content[0:-1]
        elif btn == '低级':
            ro.withdraw()
            root.update()
            root.deiconify()

        contentVar.set(content)

    operators = ('÷', '×', '-', '+', '=', '.')
    ro.mainloop()

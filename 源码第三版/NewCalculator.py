# -*- coding:utf-8 -*-

import tkinter as tk
from tkinter import messagebox
import re



class BaseDesk():
    def __init__(self, master):
        self.root = master
        self.root.config()
        self.root.title('111la')
        self.root.minsize(280, 400)
        self.root.resizable(0, 0)
        Initface(self.root)


class Initface():
    def __init__(self, master=None):
        self.master = master
        self.initface = tk.Frame(self.master, ).pack()
        self.v = tk.StringVar(self.initface, '')
        self.entry = tk.Entry(self.initface, textvariable=self.v, state='readonly', font=("Arial", 12)).place(x=0, y=30,width=280, height=100)


        # 数字键按钮
        btn7 = tk.Button(self.initface, text='7', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                x='7': buttonClick(x))
        btn7.place(x=0, y=185, width=70, height=55)
        btn8 = tk.Button(self.initface, text='8', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                x='8': buttonClick(x))
        btn8.place(x=70, y=185, width=70, height=55)
        btn9 = tk.Button(self.initface, text='9', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                x='9': buttonClick(x))
        btn9.place(x=140, y=185, width=70, height=55)

        btn4 = tk.Button(self.initface, text='4', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                x='4': buttonClick(x))
        btn4.place(x=0, y=240, width=70, height=55)
        btn5 = tk.Button(self.initface, text='5', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                x='5': buttonClick(x))
        btn5.place(x=70, y=240, width=70, height=55)
        btn6 = tk.Button(self.initface, text='6', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                x='6': buttonClick(x))
        btn6.place(x=140, y=240, width=70, height=55)

        btn1 = tk.Button(self.initface, text='1', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                x='1': buttonClick(x))
        btn1.place(x=0, y=295, width=70, height=55)
        btn2 = tk.Button(self.initface, text='2', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                x='2': buttonClick(x))
        btn2.place(x=70, y=295, width=70, height=55)
        btn3 = tk.Button(self.initface, text='3', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                x='3': buttonClick(x))
        btn3.place(x=140, y=295, width=70, height=55)
        btn0 = tk.Button(self.initface, text='0', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                x='0': buttonClick(x))
        btn0.place(x=70, y=350, width=70, height=55)

        # 运算符号按钮
        btnac = tk.Button(self.initface, text='AC', bd=0.5, font=('黑体', 20), fg='orange', command=lambda \
                x='AC': buttonClick(x))
        btnac.place(x=0, y=130, width=70, height=55)
        btnback = tk.Button(self.initface, text='←', font=('微软雅黑', 20), fg='#4F4F4F', bd=0.5, command=lambda \
                x='←': buttonClick(x))
        btnback.place(x=70, y=130, width=70, height=55)
        btndivi = tk.Button(self.initface, text='^', font=('微软雅黑', 20), fg='#4F4F4F', bd=0.5, command=lambda \
                x='^': buttonClick(x))
        btndivi.place(x=140, y=130, width=70, height=55)
        btnmul = tk.Button(self.initface, text='+', font=('微软雅黑', 20), fg="#4F4F4F", bd=0.5, command=lambda \
                x='+': buttonClick(x))
        btnmul.place(x=210, y=130, width=70, height=55)
        btnsub = tk.Button(self.initface, text='-', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                x='-': buttonClick(x))
        btnsub.place(x=210, y=185, width=70, height=55)
        btnadd = tk.Button(self.initface, text='×', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                x='×': buttonClick(x))
        btnadd.place(x=210, y=240, width=70, height=55)
        btnequ = tk.Button(self.initface, text='÷', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                x='÷': buttonClick(x))
        btnequ.place(x=210, y=295, width=70, height=55)
        btnequ = tk.Button(self.initface, text='=', bg='orange', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5,
                           command=lambda x='=': buttonClick(x))
        btnequ.place(x=210, y=350, width=70, height=55)

        btnper = tk.Button(self.initface, text='高级', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=self.change)
        btnper.place(x=0, y=350, width=70, height=55)
        btnpoint = tk.Button(self.initface, text='.', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                x='.': buttonClick(x))
        btnpoint.place(x=140, y=350, width=70, height=55)

        def buttonClick(btn):
            content = self.v.get()
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
                        if operat == '÷':
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
            if btn == '←':  # 如果按下的是退格‘’，则选取当前数字第一位到倒数第二位
                content = content[0:-1]
            self.v.set(content)
    def change(self):
       # self.initface.destory()
        face=face1(self.master)
        face.mainloop()


operators = ('÷', '×', '-', '+', '=', '.')

class face1():
    def __init__(self, master):
        self.master = master
        self.face1 = tk.Frame(self.master, ).pack()
        self.v = tk.StringVar(self.face1, '')
        self.entry = tk.Entry(self.face1, textvariable=self.v, state='readonly', font=("Arial", 12)).place(x=0, y=30,width=280,height=60)


        btn7 = tk.Button(self.face1, text='7', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                x='7': buttonClick(x))
        btn7.place(x=0, y=185, width=70, height=55)
        btn8 = tk.Button(self.face1, text='8', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                x='8': buttonClick(x))
        btn8.place(x=70, y=185, width=70, height=55)
        btn9 = tk.Button(self.face1, text='9', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                x='9': buttonClick(x))
        btn9.place(x=140, y=185, width=70, height=55)

        btn4 = tk.Button(self.face1, text='4', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                x='4': buttonClick(x))
        btn4.place(x=0, y=240, width=70, height=55)
        btn5 = tk.Button(self.face1, text='5', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                x='5': buttonClick(x))
        btn5.place(x=70, y=240, width=70, height=55)
        btn6 = tk.Button(self.face1, text='6', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                x='6': buttonClick(x))
        btn6.place(x=140, y=240, width=70, height=55)

        btn1 = tk.Button(self.face1, text='1', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                x='1': buttonClick(x))
        btn1.place(x=0, y=295, width=70, height=55)
        btn2 = tk.Button(self.face1, text='2', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                x='2': buttonClick(x))
        btn2.place(x=70, y=295, width=70, height=55)
        btn3 = tk.Button(self.face1, text='3', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                x='3': buttonClick(x))
        btn3.place(x=140, y=295, width=70, height=55)
        btn0 = tk.Button(self.face1, text='0', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                x='0': buttonClick(x))
        btn0.place(x=70, y=350, width=70, height=55)
        # 运算符号按钮
        btnac = tk.Button(self.face1, text='AC', bd=0.5, font=('黑体', 20), fg='orange', command=lambda \
                x='AC': buttonClick(x))
        btnac.place(x=0, y=130, width=70, height=55)
        btnback = tk.Button(self.face1, text='←', font=('微软雅黑', 20), fg='#4F4F4F', bd=0.5, command=lambda \
                x='←': buttonClick(x))
        btnback.place(x=70, y=130, width=70, height=55)
        btndivi = tk.Button(self.face1, text='^', font=('微软雅黑', 20), fg='#4F4F4F', bd=0.5, command=lambda \
                x='^': buttonClick(x))
        btndivi.place(x=140, y=130, width=70, height=55)
        btnmul = tk.Button(self.face1, text='+', font=('微软雅黑', 20), fg="#4F4F4F", bd=0.5, command=lambda \
                x='+': buttonClick(x))
        btnmul.place(x=210, y=130, width=70, height=55)
        btnsub = tk.Button(self.face1, text='-', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                x='-': buttonClick(x))
        btnsub.place(x=210, y=185, width=70, height=55)
        btnadd = tk.Button(self.face1, text='×', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                x='×': buttonClick(x))
        btnadd.place(x=210, y=240, width=70, height=55)
        btnequ = tk.Button(self.face1, text='÷', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                x='÷': buttonClick(x))
        btnequ.place(x=210, y=295, width=70, height=55)
        btnequ = tk.Button(self.face1, text='=', bg='orange', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5,
                           command=lambda x='=': buttonClick(x))
        btnequ.place(x=210, y=350, width=70, height=55)

        btnper = tk.Button(self.initface, text='高级', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=self.back)
        btnper.place(x=0, y=350, width=70, height=55)
        btnpoint = tk.Button(self.face1, text='.', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                x='.': buttonClick(x))
        btnpoint.place(x=140, y=350, width=70, height=55)
    def back(self):
        self.face1.destroy()
        initface(self.master)








if __name__ == '__main__':
    root = tk.Tk()
    BaseDesk(root)
    root.mainloop()

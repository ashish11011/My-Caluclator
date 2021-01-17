from tkinter import *
from tkinter import messagebox
import math

screen = Tk()
screen.title("My calculator")

screen.configure(bg='blue')
screen.iconbitmap('icon.ico')
screen.maxsize(width=450, height=463)
screen.minsize(width=360, height=463)
screen.geometry('360x463')

tex = StringVar()
operator = ''


def click(number):
    global operator
    operator += str(number)
    tex.set(operator)


def clear():
    global operator
    operator = ''
    tex.set(operator)


def equal():
    global operator
    try:
        result = eval(operator)
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo(
            'Notification', 'Try again something is wrong here')


def mcsin():
    global operator
    try:
        result = math.sin(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo(
            'Notification', 'Try again something is wrong here')


def mccos():
    global operator
    try:
        result = math.cos(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo(
            'Notification', 'Try again something is wrong here')


def mctan():
    global operator
    try:
        result = math.tan(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo(
            'Notification', 'Try again something is wrong here')


def mcsqrt():
    global operator
    try:
        result = math.sqrt(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo(
            'Notification', 'Try again something is wrong here')


def mclog():
    global operator
    try:
        result = math.log10(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo(
            'Notification', 'Try again something is wrong here')


entry1 = Entry(screen, bg='light blue', font=(
    'arial', 20, 'italic bold'), bd=30, justify='right', textvariable=tex)
entry1.grid(row=0, columnspan=4)

btn7 = Button(screen, text='7', font=('arial', '18', 'italic bold'), bd=8, padx='16', pady='16',
              command=lambda: click(7),
              activebackground='red', activeforeground='yellow')
btn7.grid(row=1, column=0)

btn8 = Button(screen, text='8', font=('arial', '18', 'italic bold'), bd=8, padx='16', pady='16',
              command=lambda: click(8),
              activebackground='red', activeforeground='yellow')
btn8.grid(row=1, column=1)

btn9 = Button(screen, text='9', font=('arial', '18', 'italic bold'), bd=8, padx='16', pady='16',
              command=lambda: click(9),
              activebackground='red', activeforeground='yellow')
btn9.grid(row=1, column=2)

btnadd = Button(screen, text='+', font=('arial', '18', 'italic bold'), bd=8, padx='16', pady='16',
                command=lambda: click('+'),
                activebackground='red', activeforeground='yellow')
btnadd.grid(row=1, column=3)

btn4 = Button(screen, text='4', font=('arial', '18', 'italic bold'), bd=8, padx='16', pady='16',
              command=lambda: click(4),
              activebackground='red', activeforeground='yellow')
btn4.grid(row=2, column=0)

btn5 = Button(screen, text='5', font=('arial', '18', 'italic bold'), bd=8, padx='16', pady='16',
              command=lambda: click(5),
              activebackground='red', activeforeground='yellow')
btn5.grid(row=2, column=1)

btn6 = Button(screen, text='6', font=('arial', '18', 'italic bold'), bd=8, padx='16', pady='16',
              command=lambda: click(6),
              activebackground='red', activeforeground='yellow')
btn6.grid(row=2, column=2)

btnsub = Button(screen, text='-', font=('arial', '18', 'italic bold'), bd=8, padx='18', pady='16',
                command=lambda: click('-'),
                activebackground='red', activeforeground='yellow')
btnsub.grid(row=2, column=3)

btn1 = Button(screen, text='1', font=('arial', '18', 'italic bold'), bd=8, padx='16', pady='16',
              command=lambda: click(1),
              activebackground='red', activeforeground='yellow')
btn1.grid(row=3, column=0)

btn2 = Button(screen, text='2', font=('arial', '18', 'italic bold'), bd=8, padx='16', pady='16',
              command=lambda: click(2),
              activebackground='red', activeforeground='yellow')
btn2.grid(row=3, column=1)

btn3 = Button(screen, text='3', font=('arial', '18', 'italic bold'), bd=8, padx='16', pady='16',
              command=lambda: click(3),
              activebackground='red', activeforeground='yellow')
btn3.grid(row=3, column=2)

btnmul = Button(screen, text='*', font=('arial', '18', 'italic bold'), bd=8, padx='18', pady='16',
                command=lambda: click('*'),
                activebackground='red', activeforeground='yellow')
btnmul.grid(row=3, column=3)

btn0 = Button(screen, text='0', font=('arial', '18', 'italic bold'), bd=8, padx='16', pady='16',
              command=lambda: click(0),
              activebackground='red', activeforeground='yellow')
btn0.grid(row=4, column=0)

btnclear = Button(screen, text='c', font=('arial', '18', 'italic bold'), bd=8, padx='16', pady='16', command=clear,
                  activebackground='red', activeforeground='yellow')
btnclear.grid(row=4, column=1)

btnequal = Button(screen, text='=', font=('arial', '18', 'italic bold'), bd=8, padx='16', pady='16', command=equal,
                  activebackground='red', activeforeground='yellow')
btnequal.grid(row=4, column=2)

btndiv = Button(screen, text='/', font=('arial', '18', 'italic bold'), bd=8, padx='18', pady='16',
                command=lambda: click('/'),
                activebackground='red', activeforeground='yellow')
btndiv.grid(row=4, column=3)

# Special Buttons


btnsin = Button(screen, text='sin', font=('arial', 13, 'italic bold'), bd=8, padx='14', pady='19', command=mcsin,
                activebackground='red', activeforeground='yellow')
btnsin.grid(row=0, column=4)

btncos = Button(screen, text='cos', font=('arial', 13, 'italic bold'), bd=8, padx='14', pady='19', command=mccos,
                activebackground='red', activeforeground='yellow')
btncos.grid(row=1, column=4)

btntan = Button(screen, text='tan', font=('arial', 13, 'italic bold'), bd=8, padx='14', pady='19', command=mctan,
                activebackground='red', activeforeground='yellow')
btntan.grid(row=2, column=4)

btnsqrt = Button(screen, text='sqr', font=('arial', 13, 'italic bold'), bd=8, padx='14', pady='19', command=mcsqrt,
                 activebackground='red', activeforeground='yellow')
btnsqrt.grid(row=3, column=4)

btnlog = Button(screen, text='log', font=('arial', 15, 'italic bold'), bd=8, padx='10', pady='19', command=mclog,
                activebackground='red', activeforeground='yellow')
btnlog.grid(row=4, column=4)


# Bindings functions


def on_bindsin(e):
    btnsin.configure(bg='red')


def on_leavesin(e):
    btnsin.configure(bg='white')


def on_bindcos(e):
    btncos.configure(bg='red')


def on_leavecos(e):
    btncos.configure(bg='white')


def on_bindtan(e):
    btntan.configure(bg='red')


def on_leavetan(e):
    btntan.configure(bg='white')


def on_bindsqrt(e):
    btnsqrt.configure(bg='red')


def on_leavesqrt(e):
    btnsqrt.configure(bg='white')


def on_bindlog(e):
    btnlog.configure(bg='red')


def on_leavelog(e):
    btnlog.configure(bg='white')


def on_bind7(e):
    btn7.configure(bg='red')


def on_leave7(e):
    btn7.configure(bg='white')


def on_bind8(e):
    btn8.configure(bg='red')


def on_leave8(e):
    btn8.configure(bg='white')


def on_bind9(e):
    btn9.configure(bg='red')


def on_leave9(e):
    btn9.configure(bg='white')


def on_bindadd(e):
    btnadd.configure(bg='red')


def on_leaveadd(e):
    btnadd.configure(bg='white')


def on_bind4(e):
    btn4.configure(bg='red')


def on_leave4(e):
    btn4.configure(bg='white')


def on_bind5(e):
    btn5.configure(bg='red')


def on_leave5(e):
    btn5.configure(bg='white')


def on_bind6(e):
    btn6.configure(bg='red')


def on_leave6(e):
    btn6.configure(bg='white')


def on_bindsub(e):
    btnsub.configure(bg='red')


def on_leavesub(e):
    btnsub.configure(bg='white')


def on_bind1(e):
    btn1.configure(bg='red')


def on_leave1(e):
    btn1.configure(bg='white')


def on_bind2(e):
    btn2.configure(bg='red')


def on_leave2(e):
    btn2.configure(bg='white')


def on_bind3(e):
    btn3.configure(bg='red')


def on_leave3(e):
    btn3.configure(bg='white')


def on_bindmul(e):
    btnmul.configure(bg='red')


def on_leavemul(e):
    btnmul.configure(bg='white')


def on_bind0(e):
    btn0.configure(bg='red')


def on_leave0(e):
    btn0.configure(bg='white')


def on_bindclear(e):
    btnclear.configure(bg='red')


def on_leaveclear(e):
    btnclear.configure(bg='white')


def on_bindequal(e):
    btnequal.configure(bg='red')


def on_leaveequal(e):
    btnequal.configure(bg='white')


def on_binddiv(e):
    btndiv.configure(bg='red')


def on_leavediv(e):
    btndiv.configure(bg='white')


def on_entryone(e):
    entry1.configure(bg='red', fg='white')


def on_lentryone(e):
    entry1.configure(bg='light blue')


# Bindings


btnsin.bind('<Enter>', on_bindsin)
btnsin.bind('<Leave>', on_leavesin)

btncos.bind('<Enter>', on_bindcos)
btncos.bind('<Leave>', on_leavecos)

btntan.bind('<Enter>', on_bindtan)
btntan.bind('<Leave>', on_leavetan)

btnsqrt.bind('<Enter>', on_bindsqrt)
btnsqrt.bind('<Leave>', on_leavesqrt)

btnlog.bind('<Enter>', on_bindlog)
btnlog.bind('<Leave>', on_leavelog)

entry1.bind('<Enter>', on_entryone)
entry1.bind('<Leave>', on_lentryone)

btn7.bind('<Enter>', on_bind7)
btn7.bind('<Leave>', on_leave7)

btn8.bind('<Enter>', on_bind8)
btn8.bind('<Leave>', on_leave8)

btn9.bind('<Enter>', on_bind9)
btn9.bind('<Leave>', on_leave9)

btnadd.bind('<Enter>', on_bindadd)
btnadd.bind('<Leave>', on_leaveadd)

btn4.bind('<Enter>', on_bind4)
btn4.bind('<Leave>', on_leave4)

btn5.bind('<Enter>', on_bind5)
btn5.bind('<Leave>', on_leave5)

btn6.bind('<Enter>', on_bind6)
btn6.bind('<Leave>', on_leave6)

btnsub.bind('<Enter>', on_bindsub)
btnsub.bind('<Leave>', on_leavesub)

btn1.bind('<Enter>', on_bind1)
btn1.bind('<Leave>', on_leave1)

btn2.bind('<Enter>', on_bind2)
btn2.bind('<Leave>', on_leave2)

btn3.bind('<Enter>', on_bind3)
btn3.bind('<Leave>', on_leave3)

btnmul.bind('<Enter>', on_bindmul)
btnmul.bind('<Leave>', on_leavemul)

btn0.bind('<Enter>', on_bind0)
btn0.bind('<Leave>', on_leave0)

btnclear.bind('<Enter>', on_bindclear)
btnclear.bind('<Leave>', on_leaveclear)

btnequal.bind('<Enter>', on_bindequal)
btnequal.bind('<Leave>', on_leaveequal)

btndiv.bind('<Enter>', on_binddiv)
btndiv.bind('<Leave>', on_leavediv)

screen.mainloop()

import tkinter as tk
import math

window = tk.Tk()
window.title('Calculator')
window.config(bg='black')
ans = ''
equation = ''


def clicked_final():
    try:

        global equation
        global ans

        # eval function evaluate the expression
        # and str function convert the result
        # into string
        ans = str(eval(equation))

        # ans=str(total)

        # initialze the expression variable
        # by empty string
        equation = ""
        equation_label
        equation_label.config(text='')
        label.config(text=f'Answer is: {ans}')
    # if error is generate then handle
    # by the except block
    except:

        ans = "ERROR"
        equation = ""
        equation_label.config(text='')
        label.config(text=f'Answer is: {ans}')


def clicked(num):
    global equation
    equation += str(num)
    equation_label.config(text=equation)


def clear():
    global equation
    equation_label.config(text='')
    equation = ""


equation_label = tk.Label(text=f'{equation}', width=20, height=2, bg='black', fg='yellow')
label = tk.Label(text=f'Answer is: {ans}', width=20, height=2, bg='black', fg='yellow')

button1 = tk.Button(text='1', width=2, height=2, bg='black', fg='yellow', activebackground='#404240',
                    activeforeground='yellow', command=lambda: clicked(1))
button2 = tk.Button(text='2', width=2, height=2, bg='black', fg='yellow', activebackground='#404240',
                    activeforeground='yellow', command=lambda: clicked(2))
button3 = tk.Button(text='3', width=2, height=2, bg='black', fg='yellow', activebackground='#404240',
                    activeforeground='yellow', command=lambda: clicked(3))
button4 = tk.Button(text='4', width=2, height=2, bg='black', fg='yellow', activebackground='#404240',
                    activeforeground='yellow', command=lambda: clicked(4))
button5 = tk.Button(text='5', width=2, height=2, bg='black', fg='yellow', activebackground='#404240',
                    activeforeground='yellow', command=lambda: clicked(5))
button6 = tk.Button(text='6', width=2, height=2, bg='black', fg='yellow', activebackground='#404240',
                    activeforeground='yellow', command=lambda: clicked(6))
button7 = tk.Button(text='7', width=2, height=2, bg='black', fg='yellow', activebackground='#404240',
                    activeforeground='yellow', command=lambda: clicked(7))
button8 = tk.Button(text='8', width=2, height=2, bg='black', fg='yellow', activebackground='#404240',
                    activeforeground='yellow', command=lambda: clicked(8))
button9 = tk.Button(text='9', width=2, height=2, bg='black', fg='yellow', activebackground='#404240',
                    activeforeground='yellow', command=lambda: clicked(9))
button0 = tk.Button(text='0', width=2, height=2, bg='black', fg='yellow', activebackground='#404240',
                    activeforeground='yellow', command=lambda: clicked(0))
buttonplu = tk.Button(text='+', width=2, height=2, bg='black', fg='yellow', activebackground='#404240',
                      activeforeground='yellow', command=lambda: clicked('+'))
buttonmin = tk.Button(text='-', width=2, height=2, bg='black', fg='yellow', activebackground='#404240',
                      activeforeground='yellow', command=lambda: clicked('-'))
buttonmul = tk.Button(text='*', width=2, height=2, bg='black', fg='yellow', activebackground='#404240',
                      activeforeground='yellow', command=lambda: clicked('*'))
buttondiv = tk.Button(text='/', width=2, height=2, bg='black', fg='yellow', activebackground='#404240',
                      activeforeground='yellow', command=lambda: clicked('/'))
buttondec = tk.Button(text='.', width=2, height=2, bg='black', fg='yellow', activebackground='#404240',
                      activeforeground='yellow', command=lambda: clicked('.'))
buttonclear = tk.Button(text='clear', width=2, height=2, bg='black', fg='yellow', activebackground='#404240',
                        activeforeground='yellow', command=clear)
final_button = tk.Button(text='=', width=2, height=2, bg='black', fg='yellow', activebackground='#404240',
                         activeforeground='yellow', command=clicked_final)

buttonclear.grid(column=5, row=0)
label.grid(column=5, row=2)
equation_label.grid(column=5, row=1)
button1.grid(column=0, row=0)
button2.grid(column=1, row=0)
button3.grid(column=2, row=0)
button4.grid(column=0, row=1)
button5.grid(column=1, row=1)
button6.grid(column=2, row=1)
button7.grid(column=0, row=2)
button8.grid(column=1, row=2)
button9.grid(column=2, row=2)
button0.grid(column=0, row=3)
buttonplu.grid(column=4, row=0)
buttonmin.grid(column=4, row=1)
buttonmul.grid(column=4, row=2)
buttondiv.grid(column=4, row=3)
buttondec.grid(column=1, row=3)
final_button.grid(column=2, row=3)
window.mainloop()

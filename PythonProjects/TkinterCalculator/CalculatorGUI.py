from tkinter import *

root = Tk()
root.geometry("500x500")
root.resizable(width=0, height=0)
root.title("Calculator")

expression = ''
exp = StringVar()

entry = Entry(root, width=20, textvariable=exp, font=('Courier', 25))
entry.place(x=10,y=10,height=80,width=350)

def clear():
    global expression
    expression=''
    exp.set('')
def get_num(x):
    global expression
    expression += x
    exp.set(expression)
def result():
    global  expression
    exp.set(eval(expression))
    expression=''

btn = Button(root, text='1', width='10', height='5', fg="black", command=lambda:get_num('1') )
btn.place(x='10', y='100')
btn2 = Button(root, text='2', width='10', height='5', fg="black", command=lambda:get_num('2') )
btn2.place(x='100', y='100')
btn3 = Button(root, text='3', width='10', height='5', fg="black", command=lambda:get_num('3') )
btn3.place(x='200', y='100')
btn4 = Button(root, text='4', width='10', height='5', fg="black", command=lambda:get_num('4') )
btn4.place(x='10', y='200')
btn5 = Button(root, text='5', width='10', height='5', fg="black", command=lambda:get_num('5') )
btn5.place(x='100', y='200')
btn6 = Button(root, text='6', width='10', height='5', fg="black", command=lambda:get_num('6') )
btn6.place(x='200', y='200')
btn7 = Button(root, text='7', width='10', height='5', fg="black", command=lambda:get_num('7') )
btn7.place(x='10', y='300')
btn8 = Button(root, text='8', width='10', height='5', fg="black", command=lambda:get_num('8') )
btn8.place(x='100', y='300')
btn9 = Button(root, text='9', width='10', height='5', fg="black", command=lambda:get_num('9') )
btn9.place(x='200', y='300')
btn0 = Button(root, text='0', width='10', height='5', fg="black", command=lambda:get_num('0') )
btn0.place(x='10', y='400')
btnclr = Button(root, text='C', width='10', height='5', fg="black", command=clear )
btnclr.place(x='100', y='400')
btnres = Button(root, text='=', width='10', height='5', fg="black", command=result)
btnres.place(x='200', y='400')
btnsum = Button(root, text='+', width='10', height='5', fg="black", command=lambda:get_num('+') )
btnsum.place(x='300', y='300')
btnminus = Button(root, text='-', width='10', height='5', fg="black", command=lambda:get_num('-') )
btnminus.place(x='300', y='400')
btnmul = Button(root, text='*', width='10', height='5', fg="black", command=lambda:get_num('*') )
btnmul.place(x='300', y='100')
btndiv = Button(root, text='/', width='10', height='5', fg="black", command=lambda:get_num('/') )
btndiv.place(x='300', y='200')

root.mainloop()
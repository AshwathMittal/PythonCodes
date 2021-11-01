'''
Making a working Login And Register System With sql Database
'''

from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()

root.title("User Password")

root.geometry("400x200")

label_name = Label(root, text="Name: ", font=('Courier', 15))
label_name.place(x = 10, y = 20)
name = Entry(root, width=20)
name.place(x=100, y= 20)

label_password = Label(root, text="Password: ", font=('Courier', 15))
label_password.place(x = 10, y = 50)
password = Entry(root, width=20, show="*")
password.place(x = 120, y=50)


def login():
    u = name.get()
    p = password.get()

    name.delete(0, END)
    password.delete(0, END)

    conn = sqlite3.connect('user.db')
    #  Find user
    with conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM user WHERE name = ? AND password = ?', (u, p))
        user = cursor.fetchone()
        if user:
            messagebox.showinfo('Login', 'Login Successful')
        else:
            messagebox.showinfo('Login', 'Login Failed')

def register():
    w = Tk()

    w.title("Register")

    w.geometry("400x300")

    label_name = Label(w, text="User Name: ", font=('Courier', 15))
    label_name.place(x = 10, y = 20)
    name1 = Entry(w, width=20)
    name1.place(x=150, y= 25)

    label_password = Label(w, text="Password: ", font=('Courier', 15))
    label_password.place(x = 10, y = 50)
    password1 = Entry(w, width=20, show="*")
    password1.place(x = 120, y=55)

    label_mail = Label(w, text="E-Mail: ", font=('Courier', 15))
    label_mail.place(x = 10, y = 100)
    mail = Entry(w, width=20)
    mail.place(x = 120, y=105)
    btnreg = Button(w,text="Register", font=('Courier', 15), fg='red', command=lambda: finall(name1, password1, mail))
    btnreg.place(x = 100, y = 150)
    w.mainloop()

def finall(name1, password1, mail):
    u = name1.get()
    p = password1.get()
    m = mail.get()
    name1.delete(0, END)
    password1.delete(0, END)
    mail.delete(0, END)

    conn = sqlite3.connect('user.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS user (name TEXT, password TEXT, mail TEXT)')
        cursor.execute('INSERT INTO user (name, password, mail) VALUES (?, ?, ?)', (u, p, m))
        conn.commit()
        messagebox.showinfo('Register', 'Register Successful')


btn = Button(root,text="Login", font=('Courier', 15), fg='red', command=login)
btn.place(x = 10, y = 90)
btnreg = Button(root,text="Register", font=('Courier', 15), fg='red', command=register)
btnreg.place(x = 100, y = 90)


root.mainloop()
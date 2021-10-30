'''
use show = "*" for a password type of input
'''
from tkinter import *
from tkinter import messagebox


root = Tk()

root.title("User Password")

root.geometry("400x200")

label_name = Label(root, text="Name: ", font=('Courier', 15))
label_name.place(x = 10, y = 20)
name = Entry(root, width=20)
name.place(x=100, y= 20)

label_password = Label(root, text="address: ", font=('Courier', 15))
label_password.place(x = 10, y = 50)
password = Entry(root, width=20, show="*")
password.place(x = 120, y=50)


def save():
    u = name.get()
    p = password.get()

    name.delete(0, END)
    password.delete(0, END)

    messagebox.showinfo("Username & Passowrd", f"Username is: {u}, password is: {p}")



btn = Button(root,text="Login", font=('Courier', 15), fg='red', command=save)
btn.place(x = 100, y = 90)

root.mainloop()


import tkinter
from tkinter import *
import sqlite3

from tkinter import messagebox

root = Tk()

root.title("data insert")

root.geometry("400x200")

label_name = Label(root, text="Name: ", font=('Courier', 15))
label_name.place(x = 10, y = 20)
name = Entry(root, width=20)
name.place(x=100, y= 20)

label_address = Label(root, text="address: ", font=('Courier', 15))
label_address.place(x = 10, y = 50)
add = Entry(root, width=20)
add.place(x = 120, y=50)


def insert(a ,b):
    con = sqlite3.connect("data.db")
    c = con.cursor()
    c.execute("create table if not exists info(name text, address text)")
    c.execute(f'insert into info values(?,?)',(a,b))
    con.commit()
    con.close()
    messagebox.showinfo('Information', "Data Inserted")

def save():
    n = name.get()
    a = add.get()

    name.delete(0, END)
    add.delete(0, END)

    insert(n,a)

btn = Button(root,text="Submit", font=('Courier', 25), fg='red', command=save)
btn.place(x = 110, y = 90)

def display():
    con = sqlite3.connect("data.db")
    c = con.cursor()
    c.execute('select * from info')
    d = c.fetchall()
    # print(d)
    con.close()
    print(f'\tSno.\tname\taddress')
    for index, i in enumerate(d, start=1):
        print(f'\t{index}\t{i[0]}\t{i[1]}')

root.mainloop()

display()
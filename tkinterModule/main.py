from tkinter import *
root = Tk()

root.title("Window Title")
root.geometry('600x415') #Width X Height, Not Cumpolsory
root.resizable(width=0, height=0) #TO avoid resizing
label1 = Label(root, text="Hello World !", font=('Courier', 35), fg="red")

label1.pack(side="top", padx=50, pady=50)
def demo():
    print("Hello")
btn = Button(root, text="Click", width='10', height="1", font=('Courier', 25), command=demo)
btn.pack(side="bottom")
root.mainloop()
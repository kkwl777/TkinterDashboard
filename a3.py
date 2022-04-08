import tkinter as tk
from tkinter import *
import _tkinter

HEIGHT = 700
WIDTH = 800

root = Tk()

root.geometry("400x800")
tk.Label(root, text="Employees", fg="red", font=(None, 30)).place(x=0, y=5)
tk.Label(root, text="Employees", fg="red", font=(None, 30)).place(x=0, y=50)

e1 = Entry(root,bd=5)
e1.pack(side=RIGHT)

def backPage():
    backBtn.pack_forget()

backBtn = Button(root,text="Back",command=backPage)

w = Button(root,text="button1")
w.pack(side=RIGHT)

def amAdmin():
    print('ADMIN')
    backBtn.pack(side=LEFT)




def amEmp():
    print('EMPLOYEE')





aBtn = Button(root,text="Admin",command=amAdmin)
aBtn.pack(side=TOP)

eBtn = Button(root,text="Employee",command=amEmp)
eBtn.pack(side=TOP)

tk.Label(root, text="Employees", fg="red", font=(None, 30)).place(x=0, y=50)

root.mainloop()


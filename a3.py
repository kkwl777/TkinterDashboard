import tkinter as tk
from tkinter import *
import _tkinter
from tkinter import messagebox
from datetime import datetime
from multiprocessing import connection
import sqlite3

connection = sqlite3.connect('practice.db')

cursor = connection.cursor()
MACHINE_PASSWORD = 'serialNumber12345'

command1 = """CREATE TABLE IF NOT EXISTS employees(
            "Employee_Type" TEXT NOT NULL,
            "Employee_Name" TEXT NOT NULL,
            "Password" TEXT NOT NULL,
            "Hours" INTEGER,
            PRIMARY KEY("Employee_Name")
            )"""

cursor.execute(command1)
cursor.execute("""INSERT INTO employees ('Employee_Type', 'Employee_Name','Password' ) VALUES
                ('ADMIN', 'Owner', 'serialNumber12345')""")

HEIGHT = 700
WIDTH = 800
root = Tk()

root.geometry("400x150")

tk.Label(root, text="OFFICE CLOCK IN", fg="blue",
         font=(None, 24)).pack(side=TOP)

error1 = tk.Label(root, text="ERROR 1", fg="red",
                  font=(None, 14))


def amAdmin():
    print('ADMIN')
    backBtn.pack(side=LEFT)


def amEmp():
    print('EMPLOYEE')


# aBtn = Button(root, text="Admin", command=amAdmin)
# aBtn.pack(side=TOP)

# eBtn = Button(root, text="Employee", command=amEmp)
# eBtn.pack(side=TOP)

def login():
    cursor.execute("SELECT * FROM employees")
    results = cursor.fetchall()

    for i in results:
        print(i)
        if i[1] == 'Owner':
            print('isOwner')
            if i[2] == MACHINE_PASSWORD:
                print('Owner verified...logging into admin dashboard')
                idBtn.pack_forget()
                pwBtn.pack_forget()

                e1.pack_forget()
                e2.pack_forget()
                eBtn.pack_forget()
                backBtn.pack(side=LEFT)
    print('LOGGING IN...')
    if (len(e1.get()) < 5):
        print('invalid ID')
        messagebox.showinfo(
            "Error", "Invalid Employee #")

    elif (len(e2.get()) < 5):
        messagebox.showinfo(
            "Error", "Incorrect Password")
    else:
        print('valid id..')


eBtn = Button(root, text="LOG IN", command=login)
eBtn.pack(side=BOTTOM)


def backPage():
    backBtn.pack_forget()
    eBtn.pack(side=BOTTOM)

    idBtn.pack(side=LEFT)

    e1.pack(side=LEFT)

    e2.pack(side=RIGHT)

    pwBtn.pack(side=RIGHT)


def postID():
    print(e1.get())


backBtn = Button(root, text="Back", command=backPage)

idBtn = Button(root, text="Employee #", command=postID)
idBtn.pack(side=LEFT)
e1 = Entry(root, bd=5)
e1.pack(side=LEFT)
e2 = Entry(root, bd=5)
e2.pack(side=RIGHT)


pwBtn = Button(root, text="Password:", command=postID)
pwBtn.pack(side=RIGHT)


# tk.Label(root, text="Employees", fg="red", font=(None, 12)).place(x=0, y=50)


root.mainloop()

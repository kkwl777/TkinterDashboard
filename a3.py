#Assignment 3: Group Term Papep
#By: Kevin Li and Alexander Grozdanovski
'''
When running the application for the first time use
Employee: Owner
Password: serialNumber12345
'''
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
            "LastSeen" TEXT NOT NULL,
            PRIMARY KEY("Employee_Name")
            )"""

cursor.execute(command1)
cursor.execute("""INSERT INTO employees ('Employee_Type', 'Employee_Name','Password','LastSeen' ) VALUES
                ('ADMIN', 'Owner', 'serialNumber12345','x')""")


HEIGHT = 700
WIDTH = 800
root = Tk()

root.geometry("550x150")

Title1 = tk.Label(root, text="OFFICE CLOCK IN", fg="blue",
                  font=(None, 24))


Title1.pack(side=TOP)
TitleAdmin = tk.Label(root, text="Create Employee Accounts", fg="blue",
                      font=(None, 16))
error1 = tk.Label(root, text="ERROR 1", fg="red",
                  font=(None, 14))

a1 = Entry(root, bd=5)
a2 = Entry(root, bd=5)
newIdLabel = Button(root, text="Name")

newPwLabel = Button(root, text="Password:")


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

    if (len(e1.get()) < 3):
        print('invalid ID')
        messagebox.showinfo(
            "Error", "Invalid Employee Name")
        return
    elif (len(e2.get()) < 5):
        messagebox.showinfo(
            "Error", "Incorrect Password")
        return
    else:
        print('valid id..')

    if (e1.get() == 'Owner'):

        if e2.get() == MACHINE_PASSWORD:
            print('Loading Admin Dashboard')
            idBtn.pack_forget()
            pwBtn.pack_forget()

            e1.pack_forget()
            e2.pack_forget()
            eBtn.pack_forget()
            backBtn.pack(side=BOTTOM)
            createBtn.pack(side=BOTTOM)
            seeBtn.pack(side=BOTTOM)

            Title1.pack_forget()
            TitleAdmin.pack(side=TOP)
            newIdLabel.pack(side=LEFT)

            a1.pack(side=LEFT)
            a2.pack(side=RIGHT)
            newPwLabel.pack(side=RIGHT)

        else:
            messagebox.showinfo(
                "Error", "User/Password Incorrect or User does not exist")
    else:

        cursor.execute("SELECT * FROM employees")
        results = cursor.fetchall()

        for i in results:
            print(i)
            if i[1] == e1.get():
                print('is Employee')
                if i[2] == e2.get():
                    print('Employee verified...logging into Employee dashboard')
                    idBtn.pack_forget()
                    pwBtn.pack_forget()

                    e1.pack_forget()
                    e2.pack_forget()
                    eBtn.pack_forget()
                    backBtn.pack(side=LEFT)
                    countBtn.pack(side=TOP)

            else:
                print('error')
        print('LOGGING IN...')


eBtn = Button(root, text="LOG IN", command=login)
eBtn.pack(side=BOTTOM)


def countHours():

    cursor.execute(
        """UPDATE employees set LastSeen=(?) where Employee_Name = (?)""", ('Last Seen: ' + str(datetime.today()), e1.get()))

    messagebox.showinfo(
        "WORK HOURS UPDATED", datetime.today())


countBtn = Button(root, text="Update Hours", command=countHours)


def backPage():
    backBtn.pack_forget()
    eBtn.pack(side=BOTTOM)
    Title1.pack(side=TOP)
    idBtn.pack(side=LEFT)

    e1.pack(side=LEFT)

    e2.pack(side=RIGHT)

    pwBtn.pack(side=RIGHT)
    createBtn.pack_forget()
    a1.pack_forget()
    a2.pack_forget()
    TitleAdmin.pack_forget()
    newIdLabel.pack_forget()
    newPwLabel.pack_forget()
    countBtn.pack_forget()
    seeBtn.pack_forget()


def postID():
    print(e1.get())


def createUser():

    if len(a1.get()) < 3:
        messagebox.showinfo(
            "ERROR", "User names must be greater than 3 characters")
        return

# todo regex for password to check for special chracter requirements

    elif len(a2.get()) < 5:
        messagebox.showinfo(
            "ERROR", "Passwords must be greater than 5 characters")
        return
    try:

        cursor.execute("""INSERT INTO employees ('Employee_Type', 'Employee_Name','Password','LastSeen' ) VALUES
                        ('EMPLOYEE', (?), (?),'New Account')""", (a1.get(), a2.get()))

        messagebox.showinfo(
            "SUCCESS", "User Added")
    except sqlite3.Error:
        messagebox.showinfo(
            "ERROR", 'users already exists')


def getAllUsers():

    cursor.execute("SELECT * FROM employees")
    results = cursor.fetchall()
    print(results)
    messagebox.showinfo(
        "Employees", results)


createBtn = Button(root, text="Add Employee", command=createUser)
seeBtn = Button(root, text="See Employees", command=getAllUsers)

backBtn = Button(root, text="Back", command=backPage)

idBtn = Button(root, text="Employee", command=postID)
idBtn.pack(side=LEFT)
e1 = Entry(root, bd=5)
e1.pack(side=LEFT)
e2 = Entry(root, bd=5)
e2.pack(side=RIGHT)


pwBtn = Button(root, text="Password:", command=postID)
pwBtn.pack(side=RIGHT)


# tk.Label(root, text="Employees", fg="red", font=(None, 12)).place(x=0, y=50)


root.mainloop()

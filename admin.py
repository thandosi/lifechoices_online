from tkinter import *
import mysql.connector
from tkinter import messagebox

root = Tk()
root.geometry("600x400")
root.title("Admin")

user_id = Label(text="Username")
user_id.place(x=10, y=80)
user_id_entry = Entry()
user_id_entry.place(x=90, y=80)

user_password = Label(text="Password")
user_password.place(x=10, y=120)
user_password_entry = Entry()
user_password_entry.place(x=90, y=120)


def login():
    mydb = mysql.connector.connect(user='sql4423136', password='fDVhkgKTh6', host='sql4.freesqldatabase.com',
                                   database='sql4423136',
                                   auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()
    xy = mycursor.execute('Select * from Admin')
    for i in mycursor:
        print(i)
        if i[1] == user_password_entry.get() and i[0] == user_id_entry.get():
            messagebox.showinfo("Output", "Login")
            root.destroy()
    if i[1] != user_password_entry.get() or i[0] != user_id_entry.get():
            messagebox.showinfo("Output", "Enter correct information")

login_button = Button(text="Login", command=login)
login_button.place(x=10, y=180)

root.mainloop()

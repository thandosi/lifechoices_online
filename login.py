from tkinter import *
from tkinter import messagebox
import mysql.connector
from PIL import Image, ImageTk
from datetime import datetime

root = Tk()
root.geometry("600x600")
root.title("login")
load = Image.open("log.jpg")
loader = ImageTk.PhotoImage(load)
img = Label(root, image=loader)
img.place(x=0, y=0)

time = datetime.now()
formatted_date = time.strftime('%Y-%m-%d %H:%M:%S')
user_id = Label(text="ID No")
user_id.place(x=10, y=80)
user_id_entry = Entry()
user_id_entry.place(x=90, y=80)

password_label = Label(text="Password")
password_label.place(x=10, y=120)
password_entry = Entry()
password_entry.place(x=90, y=120)

def login():
    mydb = mysql.connector.connect(user='sql4423136', password='fDVhkgKTh6', host='sql4.freesqldatabase.com',
                                   database='sql4423136',
                                   auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()
    xy = mycursor.execute('Select * from Register')
    for i in mycursor:
        print(i)
        if i[3] == password_entry.get() and i[2] == user_id_entry.get():
            messagebox.showinfo("Output", "Login")
            root.destroy()
    if i[1] != password_entry.get() or i[0] != user_id_entry.get():
            messagebox.showinfo("Output", "Enter correct information")

    mydb = mysql.connector.connect(user='sql4423136', password='fDVhkgKTh6', host='sql4.freesqldatabase.com',
                                   database='sql4423136',
                                   auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()

    sql = "INSERT INTO logins (Identity,password,sign_in) VALUES (%s, %s, %s)"
    val = (user_id_entry.get(), password_entry.get(),formatted_date)
    mycursor.execute(sql, val)
    mydb.commit()

def register():
    messagebox.showinfo("output","please fill in the Form")

login_button = Button(text="Login", command=login)
login_button.place(x=50, y=180)

register_button = Button(text="Register", )
register_button.place(x=150, y=180)

root.mainloop()

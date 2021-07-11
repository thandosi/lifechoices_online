from tkinter import *
from tkinter import messagebox
import mysql.connector

root = Tk()
root.title("Register")
root.geometry("650x650")
root.config(bg = "white")

heading_label = Label(text="Lifechoices",fg="black",bg="white",font=100).place(x=180, y=10)
heading2_label =Label(text="Academy",fg="green",bg="white", font=100).place(x=275,y=10)

name_label = Label(root, text = 'Enter your name')
name_label.place(x= 20, y= 80)
name_entry = Entry(root)
name_entry.place(x = 150, y = 80)

surname_label = Label(root, text = 'Enter surname')
surname_label.place(x = 20 , y = 120)
surname_entry = Entry(root)
surname_entry.place(x = 150 , y = 120)

id_label = Label(root, text = 'Enter id')
id_label.place(x = 20 , y = 160)
id_entry = Entry(root)
id_entry.place(x = 150 , y = 160)

contact_label = Label(root, text = 'Enter snuber')
contact_label.place(x=20, y = 200)
contact_entry = Entry(root)
contact_entry.place(x=150, y = 200)

email_label = Label(root, text='Enter email')
email_label.place(x=20, y=240)
email_entry = Entry(root)
email_entry.place(x=150, y=240)

password_label = Label(root, text='Create password')
password_label.place(x=20, y=280)
password_entry = Entry(root)
password_entry.place(x=150 , y= 280)

kinid_label = Label(root, text = 'Kin id')
kinid_label.place(x = 20 , y = 320)
kinid_entry = Entry(root)
kinid_entry.place(x = 150 , y = 320)


def reg():

    if name_entry.get() == "" or surname_entry.get() == "" or password_entry.get() == "" or contact_entry.get() == "":
        messagebox.showwarning(title='Invalid', message='Please enter valid details.')

    else:

        mydb = mysql.connector.connect(host="sql4.freesqldatabase.com", user="sql4424049", password="szuTDDBDLa", database="sql4424049", auth_plugin = 'mysql_native_password')

        mycursor = mydb.cursor()

        sql = "INSERT INTO register (id, name, surname,email, number, password, kinId) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (id_entry.get(),name_entry.get(), surname_entry.get(),email_entry.get(),contact_entry.get(),password_entry.get(),kinid_entry.get())
        mycursor.execute(sql, val)
        mydb.commit()
        root.destroy()
        import next_of_kin


next_btn = Button(root, text = "Enter next of keen details", command = reg)
next_btn.place(x= 50, y=360)


root.mainloop()

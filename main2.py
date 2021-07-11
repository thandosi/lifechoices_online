from tkinter import *
import mysql.connector
from tkinter import messagebox
from PIL import Image, ImageTk



root = Tk()
root.geometry("600x600")
root.title("Register")
load = Image.open("reg.jpg")
loader = ImageTk.PhotoImage(load)
img = Label(root, image=loader)
img.place(x=0, y=0)

class Register():
    def __init__(self):

        self.id_no_label = Label(text="Enter your ID No")
        self.id_no_label.place(x=10, y=120)
        self.id_no_entry = Entry()
        self.id_no_entry.place(x=150, y=120)

        self.name_label = Label(text="Enter your name")
        self.name_label.place(x=10, y=60)
        self.name_entry = Entry()
        self.name_entry.place(x=150, y=60)

        self.surname_label = Label(text="Enter your surname")
        self.surname_label.place(x=10, y=90)
        self.surname_entry = Entry()
        self.surname_entry.place(x=150, y=90)

        self.email_label = Label(text="Enter your Email")
        self.email_label.place(x=10, y=280)
        self.email_entry = Entry()
        self.email_entry.place(x=150, y=280)

        self.cell_no_label = Label(text="Enter your cell no")
        self.cell_no_label.place(x=10, y=180)
        self.cell_no_entry = Entry()
        self.cell_no_entry.place(x=150, y=180)


        self.password_label = Label(text="Password")
        self.password_label.place(x=10, y=150)
        self.password_entry = Entry()
        self.password_entry.place(x=150, y=150)


        self.kin_id_label = Label(text="kin id")
        self.kin_id_label.place(x=10, y=210)
        self.kin_id_entry = Entry()
        self.kin_id_entry.place(x=150, y=210)


        self.register_button = Button(text="Next", command=self.Reg)
        self.register_button.place(x=150, y=250)

    def Reg(self):
            mydb = mysql.connector.connect(user='sql4424049', password='szuTDDBDLa', host='sql4.freesqldatabase.com',
                                   database='sql4424049',
                                   auth_plugin='mysql_native_password')
            mycursor = mydb.cursor()
            sql = "INSERT INTO register (id, name,surname, email, number, password, kinId) VALUES(%s, %s, %s,%s, %s,%s.%s)"
            val = (self.id_no_entry.get(), self.name_entry.get(), self.surname_entry.get(),self.email_entry.get(),self.cell_no_entry.get(), self.password_entry.get(), self.kin_id_entry.get())
            mycursor.execute(sql, val)
            mydb.commit()
            messagebox.showinfo("Output", "Registration Done.You can login.")


app = Register()
root.mainloop()

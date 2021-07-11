from tkinter import *
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox

root = Tk()
root.geometry("600x600")
root.title("Lifechoices")
root.config(bg="black")
load = Image.open("welcome.jpg")
loader = ImageTk.PhotoImage(load)
img = Label(root, image=loader)
img.place(x=0, y=0)


class Welcome:
    def __init__(self):
            mydb = mysql.connector.connect(user='sql4423136', password='fDVhkgKTh6',
                               host='sql4.freesqldatabase.com',
                                   database='sql4423136',
                                   auth_plugin='mysql_native_password')

            self.heading_label = Label(text="Welcome to Life Choices")
            self.heading_label.place(x=50, y=100)


            self.login_button = Button(text="Login", command=self.log)
            self.login_button.place(x=150, y=200)

            self.register_button = Button(text="Register", command=self.register)
            self.register_button.place(x=50, y=200)
            self.admin_button = Button(text="Admin user", command=self.admin)
            self.admin_button.place(x=250, y=200)


    def register(self):
        messagebox.showinfo("output","please fill in the Form")
        root.destroy()
        import reg

    def log(self):
        root.destroy()
        import login

    def admin(self):
        root.destroy()
        import admin


app = Welcome()
root.mainloop()

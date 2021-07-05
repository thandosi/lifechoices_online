from tkinter import *

root = Tk()
root.geometry("600x400")
root.title("Admin")

user_id = Label(text="Username")
user_id.place(x=10, y=80)
user_id_entry = Entry()
user_id_entry.place(x=90, y=80)

user_id = Label(text="Password")
user_id.place(x=10, y=120)
user_id_entry = Entry()
user_id_entry.place(x=90, y=120)

login_button = Button(text="Login")
login_button.place(x=10, y=180)


root.mainloop()

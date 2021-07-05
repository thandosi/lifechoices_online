from tkinter import *

root = Tk()
root.geometry("600x600")
root.title("Register")

name_label = Label(text="Enter your name")
name_label.place(x=10, y=60)
name_entry = Entry()
name_entry.place(x=150, y=60)

surname_label = Label(text="Enter your surname")
surname_label.place(x=10, y=90)
surname_entry = Entry()
surname_entry.place(x=150, y=90)

id_no_label = Label(text="Enter your ID No")
id_no_label.place(x=10, y=120)
id_no_entry = Entry()
id_no_entry.place(x=150, y=120)

cell_no_label = Label(text="Enter your cell no")
cell_no_label.place(x=10, y=150)
cell_no_entry = Entry()
cell_no_entry.place(x=150, y=150)

kin_details_label = Label(text="Next of Kin Details")
kin_details_label.place(x=10, y=190)

kin_name_label = Label(text="Name")
kin_name_label.place(x=10, y=230)
kin_name_entry = Entry()
kin_name_entry.place(x=150, y=230)


kin_no_entry = Label(text="Contact no")
kin_no_entry.place(x=10, y=260)
kin_no_entry = Entry()
kin_no_entry.place(x=150, y=260)

register_button = Button(text="complete")
register_button.place(x=150, y=320)
root.mainloop()

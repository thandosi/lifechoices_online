from tkinter import *

root = Tk()
root.title("details")
root.geometry("600x600")


kin_details_label = Label(text="Next of Kin Details")
kin_details_label.place(x=10, y=20)

kin_id_label = Label(text="Name")
kin_id_label.place(x=10, y=50)
kin_id_entry = Entry()
kin_id_entry.place(x=50, y=80)

kin_name_label = Label(text="ID")
kin_name_label.place(x=10, y=110)
kin_name_entry = Entry()
kin_name_entry.place(x=100, y=140)


kin_no_entry = Label(text="Contact no")
kin_no_entry.place(x=10, y=170)
kin_no_entry = Entry()
kin_no_entry.place(x=150, y=200)

finish_button = Button(text="Finish")
finish_button.place(x=10, y=230)

root.mainloop()

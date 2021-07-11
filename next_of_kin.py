from tkinter import *
import mysql.connector
from tkinter import messagebox

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



def finish():
    if kin_name_entry.get() == "" or kin_id_entry.get() == "" or kin_no_entry.get() == "":
        messagebox.showwarning(title='Invalid', message='Please enter valid details.')
    elif kin_name_entry.get() == " " or kin_id_entry.get() == " " or kin_no_entry == " ":
        messagebox.showwarning(title="Space", message="Please enter valid details.")

    else:
        mydb = mysql.connector.connect(host="sql4.freesqldatabase.com",
                                       user="sql4424049", password="szuTDDBDLa",
                                       database="sql4424049",
                                       auth_plugin = 'mysql_native_password')
        mycursor = mydb.cursor()
        sql = "INSERT INTO kin (numberId , name, number) Value(%s, %s, %s)"
        val = (kin_id_entry.get(), kin_name_entry.get(), kin_no_entry.get())
        mycursor.execute(sql, val)
        messagebox.showinfo("Output", "Registration Done.You can login.")
        mydb.commit()
        import login

finish_button = Button(text="Finish",command=finish)
finish_button.place(x=10, y=230)

root.mainloop()

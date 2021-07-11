from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

mydb = mysql.connector.connect(host="sql4.freesqldatabase.com",
                               user="sql4424049", password="szuTDDBDLa",
                               database="sql4424049",
                               auth_plugin='mysql_native_password')

mycursor = mydb.cursor()

root = Tk()
root.title("Login Page")
root.geometry("1000x1000")


headin_label = Label(text="My connector").place(x=400, y=5)

#labels

label1 = Label(text="id").place(x=10, y=10)
label2 = Label(text="name").place(x=10, y=40)
label3 = Label(text="surname").place(x=10, y=70)
label4 = Label(text="contact").place(x=10, y=100)
label5 = Label(text="email").place(x=10, y=130)
label6 = Label(text="password").place(x=10, y=170)
label7 = Label(text="kin id").place(x=10, y=200)


#entries

id_entry = Entry().place(x=140, y=10)
name_entry = Entry().place(x=140, y=40)
surname_entry = Entry().place(x=140, y=70)
contact_entry = Entry().place(x=140, y=100)
email_entry = Entry().place(x=140, y=130)
password_entry= Entry().place(x=140, y=170)
kin_id_entry = Entry().place(x=140, y=200)

#functions

def Add():
    identity = id_entry.get()
    name = name_entry.get()
    surname = surname_entry.get()
    password = contact_entry.get()
    kinid = kin_id_entry.get.get()
    contact = contact_entry.get()
    email = email_entry.get()
    mydb = mysql.connector.connect(host="sql4.freesqldatabase.com",
                                   user="sql4424049",
                                   password="szuTDDBDLa",
                                   database="sql4424049",
                                   auth_plugin='mysql_native_password')

    mycursor = mydb.cursor()

    xy = mycursor.execute('Select * from register')

    try:
        sql = "INSERT INTO register (id, name, surname, email, number,password,next of kinId) Values(%s,%s,%s,%s,%s,%s,%s)"
        val = (identity, name, surname, email, contact, password, kinid)
        mycursor.execute(sql, val)
        mydb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo('output''REC inserted')
        id_entry.delete(0, END)
        name_entry.delete(0, END)
        surname_entry.delete(0, END)
        contact_entry.delete(0, END)
        kin_id_entry.delete(0, END)

    except EXCEPTION as e:
        print(e)
        mydb.rollback()
        mydb.close()


def Delete():
    id_entry.delete(0, END)
    name_entry.delete(0, END)
    surname_entry.delete(0, END)
    contact_entry.delete(0, END)
    kin_id_entry.delete(0, END)
    email_entry.delete(0, END)
    password_entry.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    id_entry.insert(0, select['id'])
    name_entry.insert(0, select['name'])
    surname_entry.insert(0, select['Surname'])
    contact_entry.insert(0, select['password'])
    kin_id_entry.insert(0, select['kinId'])
    email_entry.insert(0, select['email'])
    contact_entry.insert(0, select['number'])

def Update():
    id = id_entry.get()
    name = name_entry.get()
    surname = surname_entry.get()
    password = contact_entry.get()
    email = email_entry.get()
    contact = contact_entry.get()
    kinid = kin_id_entry.get
    mydb = mysql.connector.connect(host="sql4.freesqldatabase.com",
                               user="sql4424049", password="szuTDDBDLa",
                               database="sql4424049",
                               auth_plugin='mysql_native_password')

    mycursor = mydb.cursor()
    xy = mycursor.execute('Select * register')

    try:
        sql = "Update record set id = %s, name= %s, surname=%s,email = %s, number= %s, password=%s,kinId=%s"
        val = (id, name, surname,email,contact, password, kinid)
        mycursor.execute(sql, val)
        mydb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo('output''REC UPDATED')


    except EXCEPTION as e:
        print(e)

def Show():
    mydb = mysql.connector.connect(host="sql4.freesqldatabase.com", user="sql4424049", password="szuTDDBDLa", database="sql4424049", auth_plugin = 'mysql_native_password')
    mycursor = mydb.cursor()
    mycursor.execute('SELECT id,name,surname,email,number,password,kinId FROM register')
    records = mycursor.fetchall()
    print(records)

    for i, (id, name, surname,email, number, password, kinId) in enumerate(records, start=1):
        listBox.insert("", "end", values=(id, name, surname, email, number, password, kinId))
        mydb.close()


#buttons

add_button = Button(text="add",command=Add).place(x=30, y=250)
delete_button = Button(text="delete", command=Delete).place(x=140, y=250)
update_button = Button(text="apdate", command=Update).place(x=250, y=250)

columns = ("id", "name", "surname", "email", "contact","password", "kinId")
listBox = ttk.Treeview(columns=columns, show='headings')

for col in columns:
    listBox.heading(col,text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=10,y=300)

Show()
listBox.bind('<Double-Button-1>', Delete)


root.mainloop()

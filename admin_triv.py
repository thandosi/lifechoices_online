from tkinter import *
from tkinter import ttk
import mysql.connector


mydb = mysql.connector.connect(user='sql4423136',
                               password='fDVhkgKTh6',
                               host='sql4.freesqldatabase.com',
                               database='sql4423136',
                               auth_plugin='mysql_native_password')

root = Tk()
root.title("Login Page")
root.geometry("1000x1200")

#creating frames

MainFrame = Frame( bd=10, width=770, height=700, bg="Black")
MainFrame.grid()

TitleFrame = Frame(MainFrame, bd=8, width=770, height=100, bg="black")
TitleFrame.grid(row=0, column=0)
Top_Frame = Frame(MainFrame, bd=5, width=770, height=500)
Top_Frame.grid(row=1, column=0)

LeftFrame = Frame(Top_Frame, bd=5, width=770, height=400, bg="black", padx=2)
LeftFrame.pack(side=LEFT)
LeftFrame1 = Frame(LeftFrame, bd=5, width=600, height=180, padx=2, pady=4)
LeftFrame1.pack(side=TOP, padx=0, pady=0)

RightFrame = Frame(Top_Frame, bd=5, width=100, height=400, bg="black", padx=2)
RightFrame.pack(side=RIGHT)
RightFrame1 = Frame(RightFrame, bd=5, width=90, height=300, padx=2, pady=2)
RightFrame1.pack(side=TOP)

StudentID = StringVar()
Name = StringVar()
Surname = StringVar()
IDnumber = StringVar()
Contact = StringVar()
NextOfKinName = StringVar()
NextOfKinContact = StringVar()

heading_label = Label (TitleFrame, font=('Arial', 40, 'bold'), text="Administrator", bd=7)
heading_label.grid(row=0, column=0, padx=132)

identity = Label(LeftFrame1, font=('Arial', 14, 'bold'), text="Student ID", bd=7)
identity.grid(row=1, column=0, sticky=W, padx=5)
identity = Entry(LeftFrame1, font=('Arial', 14, 'bold'), bd=5, width=44, justify='left', textvariable=StudentID)
identity.grid(row=1, column=1, sticky=W, padx=5)

Name_label = Label(LeftFrame1, font=('Arial', 14, 'bold'), text="First Name", bd=7)
Name_label.grid(row=2, column=0, sticky=W, padx=5)
Name = Entry(LeftFrame1, font=('Arial', 14, 'bold'), bd=5, width=44, justify='left', textvariable=Name)
Name.grid(row=2, column=1, sticky=W, padx=5)

Surname_label = Label(LeftFrame1, font=('Arial', 14, 'bold'), text="Surname", bd=7)
Surname_label.grid(row=3, column=0, sticky=W, padx=5)
Surname_entry = Entry(LeftFrame1, font=('Arial', 14, 'bold'), bd=5, width=44, justify='left', textvariable=Surname)
Surname_entry.grid(row=3, column=1, sticky=W, padx=5)

IDnumber_label = Label(LeftFrame1, font=('Arial', 14, 'bold'), text="Password", bd=7)
IDnumber_label.grid(row=4, column=0, sticky=W, padx=5)
IDnumber = Entry(LeftFrame1, font=('Arial', 14, 'bold'), bd=5, width=44, justify='left', textvariable=IDnumber)
IDnumber.grid(row=4, column=1, sticky=W, padx=5)

lblcontact = Label(LeftFrame1, font=('Arial', 14, 'bold'), text="Contact", bd=5)
lblcontact.grid(row=5, column=0, sticky=W, padx=5)
entcontact = Entry(LeftFrame1, font=('Arial', 14, 'bold'), bd=5, width=44, justify='left', textvariable=Contact)
entcontact.grid(row=5, column=1, sticky=W, padx=5)

lblNOKname = Label(LeftFrame1, font=('Arial', 14, 'bold'), text="Next of Kin id", bd=5)
lblNOKname.grid(row=6, column=0, sticky=W, padx=5)
entNOKname = Entry(LeftFrame1, font=('Arial', 14, 'bold'), bd=5, width=44, justify='left',  textvariable=NextOfKinName)
entNOKname.grid(row=6, column=1, sticky=W, padx=5)

#scroll bar

scroll_y=Scrollbar(LeftFrame,orient=VERTICAL)

people_records=ttk.Treeview(LeftFrame, height=12,columns=("identity","name",'surname',"password","nextofkinid"),yscrollcommand=scroll_y.set)
scroll_y.pack(side=RIGHT, fill=Y)

people_records.heading("stdid", text="studentid")
people_records.heading("stdid", text="name")
people_records.heading("stdid", text="surname")
people_records.heading("stdid", text="password")
people_records.heading("stdid", text="kinid")

people_records['show']='headings'

people_records.column("stdid", width=70)
people_records.column("stdid", width=100)
people_records.column("stdid", width=100)
people_records.column("stdid", width=100)
people_records.column("stdid", width=70)



#buttons

btnAddNew= Button(RightFrame1, font=('Arial', 16, 'bold'), text="Add New", bd=4, pady=1, padx=24, width=8, height=2).grid(row=0, column=0, padx=1)

btnDisplay = Button(RightFrame1, font=('Arial', 16, 'bold'), text="Display", bd=4, pady=1, padx=24, width=8,
                                height=2, ).grid(row=1, column=0, padx=1)

btnUpdate = Button(RightFrame1, font=('Arial', 16, 'bold'), text="Update", bd=4, pady=1, padx=24, width=8,
                                height=2, ).grid(row=2, column=0, padx=1)

btnDelete = Button(RightFrame1, font=('Arial', 16, 'bold'), text="Delete", bd=4, pady=1, padx=24, width=8,
                                height=2, ).grid(row=3, column=0, padx=1)

btnSearch = Button(RightFrame1, font=('Arial', 16, 'bold'), text="Search", bd=4, pady=1, padx=24, width=8,
                                height=2, ).grid(row=4, column=0, padx=1)

btnReset = Button(RightFrame1, font=('Arial', 16, 'bold'), text="Reset", bd=4, pady=1, padx=24, width=8,
                                height=2, ).grid(row=5, column=0, padx=1)

btnExit = Button(RightFrame1, font=('Arial', 16, 'bold'), text="Exit", bd=4, pady=1, padx=24, width=8,
                                height=2).grid(row=6, column=0, padx=1)

root.mainloop()

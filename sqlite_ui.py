from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk

import sqlite3
with sqlite3.connect("airport_db.db") as db:
    cursor = db.cursor


root = Tk()
root.title("Airport Management System")
root.geometry("1580x920")
my_tree = ttk.Treeview(root)

def refreshTable():
    for data in my_tree.get_children():
        my_tree.delete(data)

    for array in read():
        my_tree.insert(parent='', index='end', iid=array, text="", values=(array), tag="orow")

    my_tree.tag_configure('orow', background='#EEEEEE', font=('Arial', 12))
    my_tree.grid(row=12, column=0, columnspan=5, rowspan=11, padx=10, pady=20)

#placeholders for entry
ph1 = tk.StringVar()
ph2 = tk.StringVar()
ph3 = tk.StringVar()
ph4 = tk.StringVar()
ph5 = tk.StringVar()
ph6 = tk.StringVar()
ph7 = tk.StringVar()
ph8 = tk.StringVar()


#placeholder set value function
def setph(word,num):
    if num ==1:
        ph1.set(word)
    if num ==2:
        ph2.set(word)
    if num ==3:
        ph3.set(word)
    if num ==4:
        ph4.set(word)
    if num ==5:
        ph5.set(word)
    if num ==6:
        ph6.set(word)
    if num ==7:
        ph7.set(word)
    if num ==8:
        ph8.set(word)

def read():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM passenger")
    results = cursor.fetchall()
    db.commit()
    # db.close()
    return results

def add():
    passengerID = str(passengerIDEntry.get())
    name = str(nameEntry.get())
    age = str(ageEntry.get())
    sex = str(sexEntry.get())
    dateOfBirth = str(dateOfBirthEntry.get())
    address = str(addressEntry.get())
    phoneNumber = str(phoneNumberEntry.get())
    email = str(emailEntry.get())

    if (passengerID == "" or passengerID == " ") or (name == "" or name == " ") or (age == "" or sex == " ") or (dateOfBirth == "" or dateOfBirth == " ") or (address == "" or address == " ") or (phoneNumber == "" or phoneNumber == " ") or (email == "" or email == " "):
        messagebox.showinfo("Error", "Please fill up the blank entry")
        return
    else:
        try:
            cursor = db.cursor()
            cursor.execute("INSERT INTO passenger VALUES ('"+passengerID+"','"+name+"','"+age+"','"+sex+"','"+dateOfBirth+"', '"+address+"', '"+phoneNumber+"', '"+email+"') ")
            db.commit()
            # db.close()
        except:
            messagebox.showinfo("Error", "Passenger ID already exist")
            return

    refreshTable()
    

def reset():
    decision = messagebox.askquestion("Warning!!", "Delete all data?")
    if decision != "yes":
        return 
    else:
        try:
            cursor = db.cursor()
            cursor.execute("DELETE FROM passenger")
            cursor.execute("DELETE FROM payment")
            cursor.execute("DELETE FROM booking")
            db.commit()
            # db.close()
        except:
            messagebox.showinfo("Error", "Sorry an error occured")
            return

        refreshTable()

def delete():
    decision = messagebox.askquestion("Warning!!", "Delete the selected data?")
    if decision != "yes":
        return 
    else:
        selected_item = my_tree.selection()[0]
        deleteData = int(my_tree.item(selected_item)['values'][0])
        try:
            cursor = db.cursor()
            cursor.execute("DELETE FROM passenger WHERE Passenger_ID='"+str(deleteData)+"'")
            cursor.execute("DELETE FROM booking WHERE Booking_ID='"+str(deleteData)+"'")
            cursor.execute("DELETE FROM payment WHERE Booking_ID='"+str(deleteData)+"'")
            db.commit()
            # db.close()
        except:
            messagebox.showinfo("Error", "Sorry an error occured")
            return

        refreshTable()

def select():
    try:
        selected_item = my_tree.selection()[0]
        passengerID = int(my_tree.item(selected_item)['values'][0])
        name = str(my_tree.item(selected_item)['values'][1])
        age = str(my_tree.item(selected_item)['values'][2])
        sex = str(my_tree.item(selected_item)['values'][3])
        dateOfBirth = str(my_tree.item(selected_item)['values'][4])
        address = str(my_tree.item(selected_item)['values'][5])
        phoneNumber = str(my_tree.item(selected_item)['values'][6])
        email = str(my_tree.item(selected_item)['values'][7])

        setph(passengerID,1)
        setph(name,2)
        setph(age,3)
        setph(sex,4)
        setph(dateOfBirth,5)
        setph(address,6)
        setph(phoneNumber,7)
        setph(email,8)
    except:
        messagebox.showinfo("Error", "Please select a data row")

def search():
    passengerID = int(passengerIDEntry.get())
    name = str(nameEntry.get())
    age = str(ageEntry.get())
    sex = str(sexEntry.get())
    dateOfBirth = str(dateOfBirthEntry.get())
    address = str(addressEntry.get())
    phoneNumber = str(phoneNumberEntry.get())
    email = str(emailEntry.get())

    cursor = db.cursor()
    cursor.execute("SELECT * FROM passenger WHERE Passenger_ID='"+
    passengerID+"' or Name='"+
    name+"' or Age='"+
    age+"' or Sex='"+
    sex+"' or Date_of_birth='"+
    dateOfBirth+"' or Address='"+ 
    address+"' or Phone_Number='"+ 
    phoneNumber+"' or Email='"+ 
    email+ "' ")
    
    try:
        result = cursor.fetchall()

        for num in range(0,8):
            setph(result[0][num],(num+1))

        db.commit()
        # db.close()
    except:
        messagebox.showinfo("Error", "No data found")

def update():
    selectedPassengerID = ""

    try:
        selected_item = my_tree.selection()[0]
        selectedPassengerID = str(my_tree.item(selected_item)['values'][0])
    except:
        messagebox.showinfo("Error", "Please select a data row")

    passengerID = int(passengerIDEntry.get())
    name = str(nameEntry.get())
    age = str(ageEntry.get())
    sex = str(sexEntry.get())
    dateOfBirth = str(dateOfBirthEntry.get())
    address = str(addressEntry.get())
    phoneNumber = str(phoneNumberEntry.get())
    email = str(emailEntry.get())

    if (passengerID == "" or passengerID == " ") or (name == "" or name == " ") or (age == "" or sex == " ") or (dateOfBirth == "" or dateOfBirth == " ") or (address == "" or address == " ") or (phoneNumber == "" or phoneNumber == " ") or (email == "" or email == " "):
        messagebox.showinfo("Error", "Please fill up the blank entry")
        return
    else:
        try:
            cursor = db.cursor()
            cursor.execute("UPDATE passenger SET Passenger_ID='"+
            passengerID+"', Name='"+
            name+"', Age='"+
            age+"', Sex='"+
            sex+"', Date_of_birth='"+
            dateOfBirth+"', Address='"+
            address+"', Phone_Number='"+
            phoneNumber+"', Email='"+
            email+"' WHERE Passenger_ID='"+
            selectedPassengerID+"' ")
            db.commit()
            # db.close()
        except:
            messagebox.showinfo("Error", "Passenger ID already exist")
            return

    refreshTable()

def clear():
    try:
        setph("",1)
        setph("",2)
        setph("",3)
        setph("",4)
        setph("",5)
        setph("",6)
        setph("",7)
        setph("",8)
    except:
        messagebox.showinfo("Error", "Please select a data row")

def details():
    pass


# UI 

label = Label(root, text="Airport Management System", font=('Arial Bold', 30))
label.grid(row=0, column=0, columnspan=8, rowspan=2, padx=30, pady=20)

passengerIDLabel = Label(root, text="Passenger ID", font=('Arial', 15))
nameLabel = Label(root, text="Name", font=('Arial', 15))
ageLabel = Label(root, text="Age", font=('Arial', 15))
sexLabel = Label(root, text="Sex", font=('Arial', 15))
dateOfBirthLabel = Label(root, text="Date of Birth", font=('Arial', 15))
addressLabel = Label(root, text="Address", font=('Arial', 15))
phoneNumberLabel = Label(root, text="Phone Number", font=('Arial', 15))
emailLabel = Label(root, text="E-Mail", font=('Arial', 15))

passengerIDLabel.grid(row=2, column=0, columnspan=1, padx=50, pady=5)
nameLabel.grid(row=3, column=0, columnspan=1, padx=50, pady=5)
ageLabel.grid(row=4, column=0, columnspan=1, padx=50, pady=5)
sexLabel.grid(row=5, column=0, columnspan=1, padx=50, pady=5)
dateOfBirthLabel.grid(row=6, column=0, columnspan=1, padx=50, pady=5)
addressLabel.grid(row=7, column=0, columnspan=1, padx=50, pady=5)
phoneNumberLabel.grid(row=8, column=0, columnspan=1, padx=50, pady=5)
emailLabel.grid(row=9, column=0, columnspan=1, padx=50, pady=5)

passengerIDEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph1)
nameEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph2)
ageEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph3)
sexEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph4)
dateOfBirthEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph5)
addressEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph6)
phoneNumberEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph7)
emailEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph8)

passengerIDEntry.grid(row=2, column=1, columnspan=4, padx=5, pady=0)
nameEntry.grid(row=3, column=1, columnspan=4, padx=5, pady=0)
ageEntry.grid(row=4, column=1, columnspan=4, padx=5, pady=0)
sexEntry.grid(row=5, column=1, columnspan=4, padx=5, pady=0)
dateOfBirthEntry.grid(row=6, column=1, columnspan=4, padx=5, pady=0)
addressEntry.grid(row=7, column=1, columnspan=4, padx=5, pady=0)
phoneNumberEntry.grid(row=8, column=1, columnspan=4, padx=5, pady=0)
emailEntry.grid(row=9, column=1, columnspan=4, padx=5, pady=0)

addBtn = Button(
    root, text="Add", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#84F894", command=add)
updateBtn = Button(
    root, text="Update", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#84E8F8", command=update)
deleteBtn = Button(
    root, text="Delete", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#FF9999", command=delete)
searchBtn = Button(
    root, text="Search", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#F4FE82", command=search)
resetBtn = Button(
    root, text="Reset", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#F398FF", command=reset)
selectBtn = Button(
    root, text="Select", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#EEEEEE", command=select)
clearBtn = Button(
    root, text="Clear", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#EEEEEE", command=clear)

addBtn.grid(row=3, column=11, columnspan=1, rowspan=2)
updateBtn.grid(row=5, column=11, columnspan=1, rowspan=2)
deleteBtn.grid(row=7, column=11, columnspan=1, rowspan=2)
searchBtn.grid(row=9, column=11, columnspan=1, rowspan=2)
resetBtn.grid(row=11, column=11, columnspan=1, rowspan=2)
selectBtn.grid(row=13, column=11, columnspan=1, rowspan=2)
clearBtn.grid(row=15, column=11, columnspan=1, rowspan=2)

style = ttk.Style()
style.configure("Treeview.Heading", font=('Arial Bold', 15))

my_tree['columns'] = ("Passenger ID","Name","Age","Sex","Date of Birth","Address","Phone Number","E-Mail")

my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Passenger ID", anchor=W, width=135)
my_tree.column("Name", anchor=W, width=160)
my_tree.column("Age", anchor=W, width=90)
my_tree.column("Sex", anchor=W, width=90)
my_tree.column("Date of Birth", anchor=W, width=130)
my_tree.column("Address", anchor=W, width=170)
my_tree.column("Phone Number", anchor=W, width=150)
my_tree.column("E-Mail", anchor=W, width=180)

my_tree.heading("Passenger ID", text="Passenger ID", anchor=W)
my_tree.heading("Name", text="Name", anchor=W)
my_tree.heading("Age", text="Age", anchor=W)
my_tree.heading("Sex", text="Sex", anchor=W)
my_tree.heading("Date of Birth", text="Date of Birth", anchor=W)
my_tree.heading("Address", text="Address", anchor=W)
my_tree.heading("Phone Number", text="Phone Number", anchor=W)
my_tree.heading("E-Mail", text="E-Mail", anchor=W)

refreshTable()

root.mainloop()
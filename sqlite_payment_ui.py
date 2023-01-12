from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk

import sqlite3

with sqlite3.connect("airport_db.db") as db:
    cursor = db.cursor

root = Tk()
root.title("Airport Booking System")
root.geometry("1580x920")
my_tree = ttk.Treeview(root)


def refreshTable():
    for data in my_tree.get_children():
        my_tree.delete(data)

    for array in read():
        my_tree.insert(parent='', index='end', iid=array, text="", values=(array), tag="orow")

    my_tree.tag_configure('orow', background='#EEEEEE', font=('Arial', 12))
    my_tree.grid(row=12, column=0, columnspan=5, rowspan=11, padx=10, pady=20)



# placeholders for entry
ph1 = tk.StringVar()
ph2 = tk.StringVar()
ph3 = tk.StringVar()
ph4 = tk.StringVar()
ph5 = tk.StringVar()
ph6 = tk.StringVar()
ph7 = tk.StringVar()
ph8 = tk.StringVar()


# placeholder set value function
def setph(word, num):
    if num == 1:
        ph1.set(word)
    if num == 2:
        ph2.set(word)
    if num == 3:
        ph3.set(word)
    if num == 4:
        ph4.set(word)
    if num == 5:
        ph5.set(word)
    if num == 6:
        ph6.set(word)


def read():
    cursor = db.cursor()
    cursor.execute("SELECT booking.Passenger_ID, booking.Booking_ID ,booking.Booking_Date, booking.Flight_Number, payment.Payment_Type, payment.Payment_Amount, payment.Payment_Status FROM booking INNER JOIN payment ON booking.Booking_ID=payment.Booking_ID;")
    results = cursor.fetchall()
    db.commit()
    # db.close()
    return results


def add():
    passengerID = str(passengerIDEntry.get())
    bookingID = str(BookingIDEntry.get())
    bookingDate = str(BookingDateEntry.get())
    flightNumber = str(FlightNumberEntry.get())
    paymentType = str(PaymentTypeEntry.get())
    if (flightNumber == "1"):
        paymentAmount = "100000"
    else:
        paymentAmount = "50000"
    if (paymentAmount == "0"):
        paymentStatus = "PAID"
    else:
        paymentStatus = "NOT PAID"


    if (passengerID == "" or passengerID == " ") or (bookingID == "" or bookingID == " ") or (bookingDate == "" or bookingDate== " ") or (
            paymentType == "" or paymentType == " ") or (flightNumber == "" or flightNumber == " "):
        messagebox.showinfo("Error", "Please fill up the blank entry")
        return
    else:
        try:
            cursor = db.cursor()
            cursor.execute("INSERT INTO booking VALUES ('"+bookingID+"','"+bookingDate+"','"+flightNumber+"','"+passengerID+"') ")
            cursor.execute("INSERT INTO payment VALUES ('"+bookingID+"','"+paymentType+"','"+paymentAmount+"','"+paymentStatus+"') ")
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
            cursor.execute("DELETE FROM passenger WHERE Passenger_ID='" + str(deleteData) + "'")
            cursor.execute("DELETE FROM booking WHERE Booking_ID='" + str(deleteData) + "'")
            cursor.execute("DELETE FROM payment WHERE Booking_ID='" + str(deleteData) + "'")
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

        setph(passengerID, 1)
        setph(name, 2)
        setph(age, 3)
        setph(sex, 4)
        setph(dateOfBirth, 5)
        setph(address, 6)
        setph(phoneNumber, 7)
        setph(email, 8)
    except:
        messagebox.showinfo("Error", "Please select a data row")


def search():
    passengerID = str(passengerIDEntry.get())
    bookingID = str(BookingIDEntry.get())
    bookingDate = str(BookingDateEntry.get())
    flightNumber = str(FlightNumberEntry.get())
    paymentType = str(PaymentTypeEntry.get())

    cursor = db.cursor()
    cursor.execute("SELECT * FROM booking WHERE Booking_ID='" +
                   bookingID + "' or Booking_Date='" +
                   bookingDate + "' or Flight_Number='" +
                   flightNumber + "' or Passenger_ID='" +
                   passengerID + "' ")
    # cursor.execute("SELECT * FROM payment WHERE Payment_Type='" +
    #                paymentType + "' ")

    try:
        result = cursor.fetchall()

        for num in range(0, 4):
            setph(result[0][num], (num + 1))

        db.commit()
        # db.close()
    except:
        messagebox.showinfo("Error", "No data found")


def pay():
    try:
        selected_item = my_tree.selection()[0]
        passengerID = str(my_tree.item(selected_item)['values'][0])
        bookingID = str(my_tree.item(selected_item)['values'][1])

    except:
        messagebox.showinfo("Error", "Please select a data row")

    cursor = db.cursor()
    cursor.execute("SELECT * FROM booking WHERE Passenger_ID='"+
    passengerID+"' or Booking_ID='"+
    bookingID+"' ")

    if (passengerID == "" or passengerID == " ") or (bookingID == "" or bookingID == " "):
        messagebox.showinfo("Error", "Please fill up the blank entry")
        return
    else:
        try:
            cursor = db.cursor()
            cursor.execute("UPDATE payment SET Payment_Amount = 0, Payment_Status = 'PAID' WHERE Booking_ID = '"+bookingID+"'")
            db.commit()
            # db.close()
        except:
            messagebox.showinfo("Error", "An error has occured")
            return

    refreshTable()


def clear():
    try:
        setph("", 1)
        setph("", 2)
        setph("", 3)
        setph("", 4)
        setph("", 5)
        setph("", 6)

    except:
        messagebox.showinfo("Error", "Please select a data row")

# UI

label = Label(root, text="Airport Booking System", font=('Arial Bold', 30))
label.grid(row=0, column=0, columnspan=8, rowspan=2, padx=30, pady=20)

passengerIDLabel = Label(root, text="Passenger ID", font=('Arial', 15))
BookingIDLabel = Label(root, text="Booking ID", font=('Arial', 15))
BookingDateLabel = Label(root, text="Booking Date", font=('Arial', 15))
FlightNumberLabel = Label(root, text="Flight Number", font=('Arial', 15))
PaymentTypeLabel = Label(root, text="Payment Type", font=('Arial', 15))

passengerIDLabel.grid(row=2, column=0, columnspan=1, padx=50, pady=5)
BookingIDLabel.grid(row=3, column=0, columnspan=1, padx=50, pady=5)
BookingDateLabel.grid(row=4, column=0, columnspan=1, padx=50, pady=5)
FlightNumberLabel.grid(row=5, column=0, columnspan=1, padx=50, pady=5)
PaymentTypeLabel.grid(row=6, column=0, columnspan=1, padx=50, pady=5)

passengerIDEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable=ph1)
BookingIDEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable=ph2)
BookingDateEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable=ph3)
FlightNumberEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable=ph4)
PaymentTypeEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable=ph5)

passengerIDEntry.grid(row=2, column=1, columnspan=4, padx=5, pady=0)
BookingIDEntry.grid(row=3, column=1, columnspan=4, padx=5, pady=0)
BookingDateEntry.grid(row=4, column=1, columnspan=4, padx=5, pady=0)
FlightNumberEntry.grid(row=5, column=1, columnspan=4, padx=5, pady=0)
PaymentTypeEntry.grid(row=6, column=1, columnspan=4, padx=5, pady=0)

addBtn = Button(
    root, text="Add", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#84F894", command=add)
payBtn = Button(
    root, text="Update", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#84E8F8", command=pay)
searchBtn = Button(
    root, text="Search", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#F4FE82", command=search)
clearBtn = Button(
    root, text="Clear", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#EEEEEE", command=clear)

addBtn.grid(row=3, column=11, columnspan=1, rowspan=2)
payBtn.grid(row=5, column=11, columnspan=1, rowspan=2)
searchBtn.grid(row=7, column=11, columnspan=1, rowspan=2)
clearBtn.grid(row=9, column=11, columnspan=1, rowspan=2)

style = ttk.Style()
style.configure("Treeview.Heading", font=('Arial Bold', 15))

my_tree['columns'] = ("Passenger ID", "Booking ID", "Booking Date", "Flight Number", "Payment Type", "Payment Amount",
                      "Payment Status")

my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Passenger ID", anchor=W, width=135)
my_tree.column("Booking ID", anchor=W, width=160)
my_tree.column("Booking Date", anchor=W, width=90)
my_tree.column("Flight Number", anchor=W, width=90)
my_tree.column("Payment Type", anchor=W, width=130)
my_tree.column("Payment Amount", anchor=W, width=170)
my_tree.column("Payment Status", anchor=W, width=150)


my_tree.heading("Passenger ID", text="Passenger ID", anchor=W)
my_tree.heading("Booking ID", text="Booking ID", anchor=W)
my_tree.heading("Booking Date", text="Booking Date", anchor=W)
my_tree.heading("Flight Number", text="Flight Number", anchor=W)
my_tree.heading("Payment Type", text="Payment Type", anchor=W)
my_tree.heading("Payment Amount", text="Payment Amount", anchor=W)
my_tree.heading("Payment Status", text="Payment Status", anchor=W)

refreshTable()

root.mainloop()
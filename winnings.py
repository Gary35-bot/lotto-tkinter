from email.mime.text import MIMEText
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox
from email.mime.multipart import MIMEMultipart
from email_validator import validate_email, EmailNotValidError
import smtplib


root = Tk()
root.geometry("400x400")
root.title("Banking details")
root.config(bg="yellow")


class Personal:

    def __init__(self, mastery, n=StringVar):
        with open("mytext.txt") as informs:
            for line in informs:
                inform = line.split()
            user = inform
            informs.close()
            win = user[2]

        self.account_name = Label(mastery, text="Account Holder Name :", foreground="blue")
        self.account_name.place(x=10, y=10)
        self.email_account = Label(mastery, text="Email Address :", foreground ="blue")
        self.email_account.place(x=10, y=80)
        self.email_account_entry = Entry(mastery)
        self.email_account_entry.place(x=150, y=80)
        self.name_entry = Entry(mastery, width=10)
        self.name_entry.place(x=10, y=40)
        self.account_num = Label(mastery, text="Account Number:", foreground="blue")
        self.account_num.place(x=220, y=10)
        self.account_entry = Entry(mastery, width=20)
        self.account_entry.place(x=220, y=40)
        self.btn = Button(mastery, text="Proceed", foreground="blue", command=self.acc_number)
        self.btn.place(x=150, y=200)
        self.cmb_text = Combobox(root)
        self.cmb_text["values"] = ["ABSA", "NetBank", "Standard-Bank", "African-Bank"]
        self.cmb_text["state"] = "readonly"
        self.cmb_text.place(x=110, y=130, width=150)
        self.prizes_entry = Entry(mastery)
        self.prizes_entry.insert(0,win)
        self.exit_button = Button(root, text="Exit", foreground="blue", command=root.destroy)
        self.exit_button.place(x=350, y=480)

    def acc_number(self):
        try:
            int(self.account_entry.get())
        except ValueError:

            messagebox.showinfo("Error", "Account number only has numbers!")
        sender_email = 'gafrica851@gmail.com'
        receiver_email = self.email_account_entry.get()
        password = "#@Frica!2020"
        subject = "Hello User"
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        message = "Account Holder" + str(self.name_entry.get()) + "\n"
        message = message + "Account Number: " + str(self.account_entry.get()) + "\n"
        message = message + "Bank Account :" + str(self.cmb_text.get()) + "\n"
        message = message + "Prize money: " + str(self.prizes_entry.get())
        msg.attach(MIMEText(message, 'plain'))
        text = msg.as_string()
        s = smtplib.SMTP('smtp.gmail.com', 587)

        s.starttls()

        s.login(sender_email, password)

        s.sendmail(sender_email, receiver_email, text)
        s.quit()

    def bank_val(self):
        if self.cmb_text.get() == "":
            messagebox.showerror("Error", "Please select bank")
        else:
            messagebox.showinfo("Correct")


x = Personal(root)
root.mainloop()


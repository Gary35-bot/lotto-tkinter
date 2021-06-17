from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter.ttk import Combobox


root = Tk()
root.geometry("400x400")
root.title("Congratulation you won !")


class Personal:

    def __init__(self, mastery, n=StringVar):

        self.account_name = Label(mastery, text="Account Holder Name :")
        self.account_name.place(x=10, y=10)
        self.name_entry = Entry(mastery, width=10)
        self.name_entry.place(x=10, y=40)
        self.account_num = Label(mastery, text="Account Number:")
        self.account_num.place(x=220, y=10)
        self.account_entry = Entry(mastery, width=20)
        self.account_entry.place(x=220, y=40)
        self.btn = Button(mastery, text="Proceed", foreground="blue")
        self.btn.place(x=150, y=200)


cmb_text = Combobox(root)
cmb_text["values"] = ["ABSA", "NetBank", "Standard-Bank", "Bitcoin"]
cmb_text["state"] = "readonly"
cmb_text.place(x=110, y=100, width=150)

x = Personal(root)
root.mainloop()


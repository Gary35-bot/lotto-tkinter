from tkinter import *

root = Tk()
root.geometry("450x500")
root.title("Welcome to Lotto SA")



class Validate:

  def __init__(self, mastery):
    self.name_label = Label(mastery, text="Enter your name:").place(x=80, y=5)
    self.entry1 = Entry(mastery)
    self.entry1.place(x=250, y=5)
    self.id_number_label = Label(mastery, text="Enter you ID number:").place(x=80, y=50)
    self.entry2 = Entry(mastery)
    self.entry2.place(x=250, y=50)
    self.email_label = Label(mastery, text="Email Address:").place(x=80, y=100)
    self.entry3 = Entry(mastery)
    self.entry3.place(x=250, y=100)
    self.address_label = Label(mastery, text="Address:").place(x=80, y=150)
    self.entry4 = Entry(mastery)
    self.entry4.place(x=250, y=150)
    self.b1 = Button(mastery, text="Submit", foreground="blue").place(x=200, y=210)
    self.b2 = Button(mastery, text="Clear").place(x=140, y=210)


img = PhotoImage(file="lotto.png")
canvas = Canvas(root, width=300, height=200)
canvas.create_image(0, 0, anchor=NW, image=img)
canvas.place(x=110, y=250)

x = Validate(root)
root.mainloop()


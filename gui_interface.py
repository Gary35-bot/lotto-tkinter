from tkinter import *
from datetime import datetime, timedelta
import rsaidnumber
from tkinter import messagebox
from email_validator import validate_email, EmailNotValidError
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from playsound import playsound


root = Tk()
root.geometry("450x500")
root.title("Welcome to Lotto SA")
root.config(bg="yellow")

# class for tkinter (OOP)
class Validate:
    def __init__(self, mastery):
        self.name_label = Label(mastery, text="Enter your name:")
        self.name_label.place(x=80, y=5)
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
        self.b1 = Button(mastery, text="Submit", command=self.id_val, foreground="blue").place(x=200, y=210)
        self.b2 = Button(mastery, text="Clear", command=self.clr).place(x=140, y=210)
        self.entry3.insert(0, "address@mydomain.com")

    def id_val(self): # validates id
        id_number = rsaidnumber.parse(self.entry2.get())
        age = ((datetime.today() - id_number.date_of_birth) // timedelta(days=365.25))
        email = "my+address@mydomain.com"
        if age >= 18:
            messagebox.showinfo("Let's play")
        else:
            years_left = 18 - age
            messagebox.showinfo("Return in", str(years_left) + "years time")
        try:
            valid = validate_email(email)
            email = valid.email
        except EmailNotValidError:
            messagebox.showinfo("Invalid Email. Try again")

        player_id = self.entry1.get().strip() + self.entry3.get()[:3].strip() + self.entry2.get()[:3]
        sender_email = 'gafrica851@gmail.com'
        receiver_email = self.entry3.get()
        password = "#@Frica!2020"
        subject = "Hello User"
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        message = str(player_id)
        message = message
        msg.attach(MIMEText(message, 'plain'))
        text = msg.as_string()
        s = smtplib.SMTP('smtp.gmail.com', 587)

        s.starttls()

        s.login(sender_email, password)

        s.sendmail(sender_email, receiver_email, text)
        s.quit()

        my_file = open("mytext.txt", 'a')
        my_file.write('\n')
        my_file.write("Username: " + self.entry1.get())
        my_file.write('\n')
        my_file.write("Identity Number: " + self.entry2.get())
        my_file.write('\n')
        my_file.write("Email: " + self.entry3.get())
        my_file.write('\n')
        my_file.write("Address: " + self.entry4.get())
        my_file.write('\n')
        my_file.write("id_player "+player_id)
        my_file.write('\n')
        my_file.close()
        root.destroy()
        import pick_numbers_genarate

    def clr(self):
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        self.entry4.delete(0, END)



# image for login screen
img = PhotoImage(file="lotto.png")
canvas = Canvas(root, width=250, height=200)
canvas.create_image(0, 0, anchor=NW, image=img)
canvas.place(x=100, y=250)

playsound("Heavens Choir Sound Effect (mp3cut.net).mp3")

x = Validate(root)
root.mainloop()

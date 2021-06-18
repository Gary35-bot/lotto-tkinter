from tkinter import *
import random
from tkinter import messagebox

root = Tk()
root.geometry("500x500")
root.title("Welcome to Lotto SA")

img = PhotoImage(file="lotto2.png")
canvas = Canvas(root, width=350, height=150)
canvas.create_image(0, 0, anchor=NW, image=img)
canvas.place(x=60, y=10)


class NumberPicker:
    # String variables
    anything = StringVar()
    row1_num1 = StringVar()
    row1_num2 = StringVar()
    row1_num3 = StringVar()
    row1_num4 = StringVar()
    row1_num5 = StringVar()
    row1_num6 = StringVar()
    row2_num1 = StringVar()
    row2_num2 = StringVar()
    row2_num3 = StringVar()
    row2_num4 = StringVar()
    row2_num5 = StringVar()
    row2_num6 = StringVar()
    row3_num1 = StringVar()
    row3_num2 = StringVar()
    row3_num3 = StringVar()
    row3_num4 = StringVar()
    row3_num5 = StringVar()
    row3_num6 = StringVar()



    # display label variables
    List1 = []
    List2 = []
    List3 = []

    def __init__(self, mastery):
        self.counter = 1
        self.sub_content = Label(mastery, text="Enter your 6 numbers down below from 1-49 ")
        self.sub_content.place(x=120, y=200)
        self.spin1 = Spinbox(mastery, from_=1, to=49, width=5)
        self.spin1.place(x=10, y=250)
        self.spin2 = Spinbox(mastery, from_=1, to=49, width=5)
        self.spin2.place(x=90, y=250)
        self.spin3 = Spinbox(mastery, from_=1, to=49, width=5)
        self.spin3.place(x=170, y=250)
        self.spin4 = Spinbox(mastery, from_=1, to=49, width=5)
        self.spin4.place(x=250, y=250)
        self.spin5 = Spinbox(mastery, from_=1, to=49, width=5)
        self.spin5.place(x=330, y=250)
        self.spin6 = Spinbox(mastery, from_=1, to=49, width=5)
        self.spin6.place(x=410, y=250)
        self.picked_row1_num1 = Label(mastery, text="0", textvariable=self.row1_num1)
        self.picked_row1_num1.place(x=50, y=310)
        self.picked_row1_num2 = Label(mastery, text="0", textvariable=self.row1_num2)
        self.picked_row1_num2.place(x=100, y=310)
        self.picked_row1_num3 = Label(mastery, text="0", textvariable=self.row1_num3)
        self.picked_row1_num3.place(x=150, y=310)
        self.picked_row1_num4 = Label(mastery, text="0", textvariable=self.row1_num4)
        self.picked_row1_num4.place(x=200, y=310)
        self.picked_row1_num5 = Label(mastery, text="0", textvariable=self.row1_num5)
        self.picked_row1_num5.place(x=250, y=310)
        self.picked_row1_num6 = Label(mastery, text="0", textvariable=self.row1_num6)
        self.picked_row1_num6.place(x=300, y=310)
        # second row of numbers
        self.picked_row2_num1 = Label(mastery, text="0", textvariable=self.row2_num1)
        self.picked_row2_num1.place(x=50, y=340)
        self.picked_row2_num2 = Label(mastery, text="0", textvariable=self.row2_num2)
        self.picked_row2_num2.place(x=100, y=340)
        self.picked_row2_num3 = Label(mastery, text="0", textvariable=self.row2_num3)
        self.picked_row2_num3.place(x=150, y=340)
        self.picked_row2_num4 = Label(mastery, text="0", textvariable=self.row2_num4)
        self.picked_row2_num4.place(x=200, y=340)
        self.picked_row2_num5 = Label(mastery, text="0", textvariable=self.row2_num5)
        self.picked_row2_num5.place(x=250, y=340)
        self.picked_row2_num6 = Label(mastery, text="0", textvariable=self.row2_num6)
        self.picked_row2_num6.place(x=300, y=340)
        # third row of numbers
        self.picked_row3_num1 = Label(mastery, text="0", textvariable=self.row3_num1)
        self.picked_row3_num1.place(x=50, y=370)
        self.picked_row3_num2 = Label(mastery, text="0", textvariable=self.row3_num2)
        self.picked_row3_num2.place(x=100, y=370)
        self.picked_row3_num3 = Label(mastery, text="0", textvariable=self.row3_num3)
        self.picked_row3_num3.place(x=150, y=370)
        self.picked_row3_num4 = Label(mastery, text="0", textvariable=self.row3_num4)
        self.picked_row3_num4.place(x=200, y=370)
        self.picked_row3_num5 = Label(mastery, text="0", textvariable=self.row3_num5)
        self.picked_row3_num5.place(x=250, y=370)
        self.picked_row3_num6 = Label(mastery, text="0", textvariable=self.row3_num6)
        self.picked_row3_num6.place(x=300, y=370)
        self.display_num = Label(mastery, text="", textvariable=self.anything)
        self.display_num.place(x=150, y=450)
        self.lotto_result = Label(mastery, text="Lotto result :", foreground="blue", textvariable=self.display_num)
        self.lotto_result.place(x=50, y=450)
        self.btn = Button(mastery, text="Press to confirm set!", foreground="blue", border="1", command=self.pick_set)
        self.btn.place(x=330, y=310)
        self.btn1 = Button(mastery, text="Play", foreground="blue", command=self.random_numbers)
        self.btn1.place(x=350, y=350)
        self.btn2 = Button(mastery, text="Claim Prize", foreground="blue", )
        self.btn2.place(x=350, y=390)
        self.btn2 = Button(mastery, text="Play again?", foreground="blue", command=self.clr)
        self.btn2.place(x=350, y=430)

    def pick_set(self):
        if self.counter == 1:
            self.row1_num1.set(self.spin1.get())
            self.row1_num2.set(self.spin2.get())
            self.row1_num3.set(self.spin3.get())
            self.row1_num4.set(self.spin4.get())
            self.row1_num5.set(self.spin5.get())
            self.row1_num6.set(self.spin6.get())
            self.counter += 1
            self.List1 = [int(self.spin1.get()), int(self.spin2.get()), int(self.spin3.get()), int(self.spin4.get()), int(self.spin5.get()), int(self.spin6.get())]
        elif self.counter == 2:
            self.row2_num1.set(self.spin1.get())
            self.row2_num2.set(self.spin2.get())
            self.row2_num3.set(self.spin3.get())
            self.row2_num4.set(self.spin4.get())
            self.row2_num5.set(self.spin5.get())
            self.row2_num6.set(self.spin6.get())
            self.counter += 1
            self.List2 = [int(self.spin1.get()), int(self.spin2.get()), int(self.spin3.get()), int(self.spin4.get()), int(self.spin5.get()), int(self.spin6.get())]
        elif self.counter == 3:
            self.row3_num1.set(self.spin1.get())
            self.row3_num2.set(self.spin2.get())
            self.row3_num3.set(self.spin3.get())
            self.row3_num4.set(self.spin4.get())
            self.row3_num5.set(self.spin5.get())
            self.row3_num6.set(self.spin6.get())
            self.counter += 1
            self.List3 = [int(self.spin1.get()), int(self.spin2.get()), int(self.spin3.get()), int(self.spin4.get()), int(self.spin5.get()), int(self.spin6.get())]

    def random_numbers(self):
        global win
        y = 0
        lotto_nums = random.sample(range(1, 50), 6)
        self.anything.set(lotto_nums)
        for x in range(0, 6):
            if self.List1[x] == lotto_nums[x]:
                y += 1
            elif y == 6:
                win = 10000000
            elif y == 5:
                win = 8584
            elif y == 4:
                win = 2384
            elif y == 3:
                win = 100.50
            elif y == 2:
                win = 20
            elif y < 2:
                win = 0
        messagebox.showinfo("Status", "You had:" + str(y) + "correct")
        messagebox.showinfo("Winnings ", "You have won R" + str(win))

        for x in range(0, 6):
            if self.List2[x] == lotto_nums[x]:
                y += 1
            elif y == 6:
                win = 10000000
            elif y == 5:
                win = 8584
            elif y == 4:
                win = 2384
            elif y == 3:
                win = 100.50
            elif y == 2:
                win = 20
            elif y < 2:
                win = 0
        messagebox.showinfo("Status", "You had:" + str(y) + "correct")
        messagebox.showinfo("Winnings ", "You have won R" + str(win))

        for x in range(0, 6):
            if self.List3[x] == lotto_nums[x]:
                y += 1
            elif y == 6:
                win = 10000000
            elif y == 5:
                win = 8584
            elif y == 4:
                win = 2384
            elif y == 3:
                win = 100.50
            elif y == 2:
                win = 20
            elif y < 2:
                win = 0
        messagebox.showinfo("Status", "You had:" + str(y) + "correct")
        messagebox.showinfo("Winnings ", "You have won R" + str(win))

    def clr(self):
        self.spin1.delete(0, END)
        self.spin2.delete(0, END)
        self.spin3.delete(0, END)
        self.spin4.delete(0, END)
        self.spin5.delete(0, END)
        self.spin6.delete(0, END)
        self.row1_num1.set("")
        self.row1_num2.set("")
        self.row1_num3.set("")
        self.row1_num4.set("")
        self.row1_num5.set("")
        self.row1_num6.set("")
        self.row2_num1.set("")
        self.row2_num2.set("")
        self.row2_num3.set("")
        self.row2_num4.set("")
        self.row2_num5.set("")
        self.row2_num6.set("")
        self.row2_num1.set("")
        self.row2_num2.set("")
        self.row2_num3.set("")
        self.row2_num4.set("")
        self.row2_num5.set("")
        self.row2_num6.set("")
        self.row3_num1.set("")
        self.row3_num2.set("")
        self.row3_num3.set("")
        self.row3_num4.set("")
        self.row3_num5.set("")
        self.row3_num6.set("")
        self.display_num.configure(text="")


x = NumberPicker(root)
root.mainloop()


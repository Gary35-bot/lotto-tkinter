from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("Welcome to Lotto SA")

img = PhotoImage(file="lotto2.png")
canvas = Canvas(root, width=350, height=150)
canvas.create_image(0, 0, anchor=NW, image=img)
canvas.place(x=60, y=10)


class NumberPicker:
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
        self.picked_row1_num1 = Label(mastery, text="1")
        self.picked_row1_num1.place(x=50, y=310)
        self.picked_row1_num2 = Label(mastery, text="2")
        self.picked_row1_num2.place(x=100, y=310)
        self.picked_row1_num3 = Label(mastery, text="3")
        self.picked_row1_num3.place(x=150, y=310)
        self.picked_row1_num4 = Label(mastery, text="4")
        self.picked_row1_num4.place(x=200, y=310)
        self.picked_row1_num5 = Label(mastery, text="5")
        self.picked_row1_num5.place(x=250, y=310)
        self.picked_row1_num6 = Label(mastery, text="6")
        self.picked_row1_num6.place(x=300, y=310)
        # second row of numbers
        self.picked_row2_num1 = Label(mastery, text="1")
        self.picked_row2_num1.place(x=50, y=340)
        self.picked_row2_num2 = Label(mastery, text="2")
        self.picked_row2_num2.place(x=100, y=340)
        self.picked_row2_num3 = Label(mastery, text="3")
        self.picked_row2_num3.place(x=150, y=340)
        self.picked_row2_num4 = Label(mastery, text="4")
        self.picked_row2_num4.place(x=200, y=340)
        self.picked_row2_num5 = Label(mastery, text="5")
        self.picked_row2_num5.place(x=250, y=340)
        self.picked_row2_num6 = Label(mastery, text="6")
        self.picked_row2_num6.place(x=300, y=340)
        # third row of numbers
        self.picked_num3 = Label(mastery, text="10 10 10 10 10 10", bg="orange")
        self.picked_num3.place(x=50, y=370)
        self.btn = Button(mastery, text="Play!", foreground="blue", border="1")
        self.btn.place(x=350, y=310)
        self.btn1 = Button(mastery, text="Play again ?", foreground="blue")
        self.btn1.place(x=350, y=350)
        self.btn2 = Button(mastery, text="Claim Prize", foreground="blue", command=self.awe)
        self.btn2.place(x=350, y=390)

    def awe(self):
        if self.counter == 1:
            self.picked_row1_num1["text"] = self.spin1.get()
            self.picked_row1_num2["text"] = self.spin2.get()
            self.picked_row1_num3["text"] = self.spin3.get()
            self.picked_row1_num4["text"] = self.spin4.get()
            self.picked_row1_num5["text"] = self.spin5.get()
            self.picked_row1_num6["text"] = self.spin6.get()
        elif self.counter == 2:
            self.picked_row2_num1["text"] = self.spin1.get()
            self.picked_row2_num2["text"] = self.spin2.get()
            self.picked_row2_num3["text"] = self.spin3.get()
            self.picked_row2_num4["text"] = self.spin4.get()
            self.picked_row2_num5["text"] = self.spin5.get()
            self.picked_row2_num6["text"] = self.spin6.get()
        elif self.counter == 3:
            pass




x = NumberPicker(root)
root.mainloop()


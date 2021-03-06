from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import requests

root = Tk()

# StringVar
results = StringVar()
values1 = StringVar()
values2 = StringVar()

# code to add widgets and style window will go here
root.geometry("450x550")
root.title("Currency Converter")
root.config(bg="black")
root.resizable(0, 0)

img = PhotoImage(file="current.png")
canvas = Canvas(root, width=250, height=200)
canvas.create_image(0, 0, anchor=NW, image=img)
canvas.place(x=100, y=20)

information = requests.get('https://v6.exchangerate-api.com/v6/89dcd9e8cc7777ded2575ce1/latest/ZAR')
information_json = information.json()

conversion_rates = information_json['conversion_rates']

currency = []
for i in conversion_rates.keys():
    currency.append(i)

# selecting  currency
currency_cb = ttk.Combobox(root)
currency_cb['values'] = currency
currency_cb['state'] = 'readonly'
currency_cb.set('Select Currency')
currency_cb.place(x=10, y=280)

amount_label = Label(root, text='Pre-Entered Amount:', bg='purple').place(x=60, y=330)
ent1 = Entry(root, bg='white')
ent1.place(x=200, y=330)
converted_label = Label(root, text='Converted Amount:', bg='purple').place(x=65, y=380)
text_label = Label(root, text='', textvariable=results).place(x=200, y=380)

def convert(to_currency, amount):

    amount = round(amount * conversion_rates[to_currency])
    return amount

# functions
def transform():
    try:
        amount = float(ent1.get())
        to_curr = currency_cb.get()

        converted_amount = convert(to_curr, amount)

        results.set(converted_amount)
    except ValueError:
        if ent1 != int and ent1 != float:
            messagebox.showerror('Entry not valid', 'Enter numbers only')

    except requests.exceptions.ConnectionError:
        messagebox.showerror('Internet error', 'Offline Check Internet Connection')
    except KeyError:
        messagebox.showerror('ERROR!', 'Select Type of Currency')


def money():
    root.destroy()
    import winnings


def clear():
    currency_cb.set('Select Currency')
    ent1.delete(0, END)
    ent1.focus()
    results.set('')



# buttons for the currency converter

b1 = Button(root, text="Convert", bg='purple', command=transform)
b1.place(x=180, y=480)
b2 = Button(root, text="Clear", bg='white', command=clear)
b2.place(x=100, y=480)
b3 = Button(root, text="Claim", foreground="purple", command=money)
b3.place(x=280, y=480)


root.mainloop()

from tkinter import *
import random
# price = input("What is the price? $")
# percent = input("How much percentage off? ")

# new_percent = str("0.") + (percent)
# amount_off = float(price) * float(new_percent)
# total = float(price) - float(amount_off)

# print(f"${round(total, 2)}")

def solve():
  price_text = price_en.get()
  percent_text = percent_en.get()
  
  new_percent = str("0.") + (percent_text)
  amount_off = float(price_text) * float(new_percent)
  total = float(price_text) - float(amount_off)
  price_total.config(text=f"${round(total, 2)}")

window = Tk()
window.title("Percent off Calculator")
window.config(padx=20, pady=20)

price = Label(text="Price:", font=("courier", 25, "normal"))
price.grid(row=0, column=0)

price_en = Entry()
price_en.grid(row=0, column=1)
price_en.focus

percent = Label(text="Percent Off:", font=("courier", 25, "normal"))
percent.grid(row=2, column=0)

percent_en = Entry()
percent_en.grid(row=2, column=1)

price_total = Label(text="$0", font=("courier", 35, "normal"))
price_total.grid(row=3, column=1)

calculate = Button(text="Calculate", command=solve)
calculate.grid(row=4, column=1)

window.mainloop()

from tkinter import *
from tkinter.ttk import *

window = Tk()

window.title("Temperature Converter")
window.resizable(width=False, height=False)
def converter(event=None):
    fahrenheit_value = ent_fahrenheit.get()
    if fahrenheit_value:
        celicious_value = (int(fahrenheit_value) - 32) * 5/9
        celicious_value_formatted = f"{celicious_value:.2f}"
        lbl_celicious["text"] = str(celicious_value_formatted)


ent_fahrenheit = Entry(master=window, width=10)
ent_fahrenheit.grid(row=0, column=0, sticky="e", )
ent_fahrenheit.bind("<Return>", converter)

lbl_fahrenheit_symbol = Label(master=window, text="F")
lbl_fahrenheit_symbol.grid(row=0, column=1, sticky="e")

btn_convert = Button(master=window, text="-->", command=converter)
btn_convert.grid(row=0, column=2, pady=10)


lbl_celicious = Label(master=window)
lbl_celicious.grid(row=0, column=3, padx=10)

lbl_celicious_symbol = Label(master=window, text="C")
lbl_celicious_symbol.grid(row=0, column=4)

window.mainloop()
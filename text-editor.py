from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.ttk import *

window = Tk()


def open_file():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", END)

    with open(filepath, mode="r", encoding="utf-8") as input_file:
        text = input_file.read()
        txt_edit.insert(END, text)
    window.title(f"Simple Text Editor - {filepath}")


def save_file():
    filepath = asksaveasfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return

    with open(filepath, mode="w", encoding="utf-8") as output_file:
        text = txt_edit.get("1.0", END)
        output_file.write(text)
    window.title(f"Simple Text Editor - {filepath}")


window.title("Simple text editor")

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

txt_edit = Text(master=window)
txt_edit.grid(row=0, column=1, sticky="nsew")

frm_buttons = Frame(master=window, relief=RAISED)
frm_buttons.grid(row=0, column=0, sticky="ns")

btn_open = Button(master=frm_buttons, text="Open", command=open_file)
btn_save = Button(master=frm_buttons, text="Save As...", command=save_file)
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

window.mainloop()

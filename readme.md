1. Tkinter app should have the following components:

```
from tkinter import *
from tkinter.ttk import * // to import the modern styles
window = Tk() // create window instance


window.mainloop() // to run event loop to listen for clicks  or keypresses
```

2. Widgets Label/Button/Entry/Text/Frame:

the widgets accept:
```
text="" // the text to display

master="" // the master frame to which it belongs to

width=""
```

Example:
```
greeting = Label(master="window", text="Hello, Tkinter", width=10)

greeting.pack()
```


* Entry is used to accept user input, it has the following actions:
```
.get() // retrieve text

.delete(0, END) // delete the entire text from zero index till the end

.insert(0, "hello world") // insert text at the given index (zero)

```

* Text is used to enter multiline text.
has the same options as Entry

```
.get("1.0", END)  # get the entire text from the first row (1) starting at first index of the text (0) till the end (END) 
.delete("1.0", END) 
.insert("1.0", "Hello") #  insert at the first row
.insert("2.0", "\nWorld") #  insert at the second row becasue of "\n"
.insert(END, "\nText added at the end") #  to add the text at the end of the text box in a new line
```


* Frames:
```
frame = Frame(master=window)
frame.pack()
txt_label = Label(master="frame", text="Text belong to frame")
```

frames appearance can be adjusted with (relief="") and (borderwidth="")
relief options:

FLAT

SUNKEN

RAISED

GROOVE

RIDGE
```
frame = Frame(master=window, relief="FLAT", borderwidth="4") 
frame.pack()
txt_label = Label(master=frame, text="Text belong to frame")
```

3. .pack() VS .place() VS .grid()

* .pack()

```
.pack(fill=X) // fill horizontally

.pack(fill=Y) // fill vertically

.pack(fill=BOTH) // fill both

```

.pack() also takes (side="")
options are:

TOP

BOTTOM

LEFT

RIGHT

to make it completely response, use 

```
.pack(fill=BOTH, expand=True)
```

* .place()
it takes the exact x/y coordinate to place the item


```
.place(x=0, y=0)

or

.place(x=10, y=10)
```

* .grid()

split the frame into rows and columns
it takes row, column, padx, pady, sticky

```
.grid(row=0, column=0, padx=4, pady=4, sticky="n")

```

sticky takes:

"ns" to fill the cell in vertical direction

"ew" to fill the cell in horizental direction

"nsew" to fill the entire cell

to adjust how the columns and rows grow with .grid when resizing the window, use:
.columnconfigure()
.rowconfigure()

to the window object

```
window.columnconfigure(0, weight=1, minsize=60) // 0 is the column numbers

window.rowconfigure([0, 1], weight=1, minsize=30) // [0,1] are the row numbers
```


4. Binding key pressing event to an item

```
window.bind("<Key>", name_of_the_function_to_handle_the_event)
```
the function should accept an event:

```
def name_of_the_function_to_handle_the_event(event)
```

5. command

the function to be called upon pressing a button for example
```
btn_button = Button(master=window, text="Click Here", command=name_of_the_function_to_be_called)
```

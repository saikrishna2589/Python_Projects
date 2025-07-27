import tkinter as tk
from tkinter import ttk
from functools import partial
#create the window
root=tk.Tk()

#title of the window
root.title('Calculator')

#now we can add widgets. start with entry widget for input


entry_input = tk.Entry(root,font=('Helvetica',20))
#apply grid method so we can see the entry input in the root window

entry_input.grid(row=0, column=0, columnspan=2,padx =10,pady=10,sticky='ew')


# we need to add 17 buttons from 0 t0 9, C,=,+,-,.,/and *

#doesn't make sense to add ttk.button(root, text='9') and then add button_add.grid(row=1,column=0,padx=10,pady=10)  as example.
#so we do a for loop


buttons =[
    ('7',1,0),('8',1,1),('9',1,2),('/',1,3),
    ('4',2,0),('5',2,1),('6',2,2),('*',2,3),
    ('1',3,0),('2',3,1),('3',3,2),('-',3,3),
    ('0',4,0),('.',4,1),('=',4,2),('+',4,3)
]

def button_press(value):
    entry_input.insert(tk.END,value)

def equal_to():
    current_values = entry_input.get()
    output = eval(current_values)
    entry_input.delete(0,tk.END)
    entry_input.insert(tk.END, str(output))


def clear():
    entry_input.delete(0,tk.END)


for button_label, row_num , col_num in buttons:

    if button_label == '=':
        button_add = ttk.Button(root, text=button_label, command=equal_to)

    else:
        button_add = ttk.Button(root, text =button_label , command = partial(button_press,button_label))

    button_add.grid(row=row_num, column=col_num, padx=5, pady=5, sticky=tk.EW)

button_add_c = ttk.Button(root,text ='C', command=clear)
button_add_c.grid(row=9,column=0,columnspan=2,padx =5, pady =5,sticky =tk.EW)

root.mainloop()

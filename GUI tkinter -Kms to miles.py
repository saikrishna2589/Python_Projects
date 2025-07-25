import tkinter as tk
from tkinter import  ttk  #Modern widgets access

def convert():
    kilometer_input = float(entry_box.get())
    miles = 0.621 *kilometer_input
    return results_label.config(text = f"{kilometer_input:.0f} kms is {miles:.2f} miles")

root = tk.Tk()
root.title("Convert Kms to miles")

frame = ttk.Frame(root,padding="10")
frame.grid(row =0, column=0, sticky = (tk.W, tk.E, tk.W, tk.S))


label = ttk.Label(frame, text="Enter the distance in Kilometers: ")
label.grid(row=0,column=0 )

entry_box = ttk.Entry(frame,width=15)
entry_box.grid(row=0,column=1,sticky=tk.W)
entry_box.focus()

convert_button = ttk.Button(frame,text ="Convert kms to miles" , command = convert)
convert_button.grid(row=1, column=0, sticky=tk.W)


results_label =ttk.Label(frame, text = "Kms in Miles : ")
results_label.grid(row=2, column=0, columnspan=2)


root.mainloop()


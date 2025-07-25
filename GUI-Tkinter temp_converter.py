import tkinter as tk  #GUI for window app
from tkinter import ttk #Modern widgets


#need to define function before it is used in the convert button below
def convert():
    fahrenheit = float(fahrenhiet_entry.get())
    celsius = (fahrenheit - 32) * 5 / 9
    return results_label.config(text = f"Temperature in Celsius: {celsius:.2f}")


root = tk.Tk()  #main window
root.title('Fahrenheit to Celsius Converter')

frame = ttk.Frame(root, padding="10")   #frame layout for gadgets within the root
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S)) #how far the frame can occupy the root window for widgets

fahrenhiet_label = ttk.Label(frame, text="Enter the temperature in Fahrenheit: ")  #put label in the frame
fahrenhiet_label.grid(row=0, column=0, sticky=tk.S)  #put where exactly is addressed here

fahrenhiet_entry = ttk.Entry(frame, width=15)  #input of the user window
fahrenhiet_entry.grid(row=0, column=1, sticky=tk.W)
fahrenhiet_entry.focus()

convert_button = ttk.Button(frame, text="Convert", command= convert)   # convert button press what happens
convert_button.grid(row=1, column=0,sticky=tk.W)

results_label = ttk.Label(frame, text="Temperature in Celsius: ")
results_label.grid(row=2, column=0,columnspan=2)




root.mainloop()

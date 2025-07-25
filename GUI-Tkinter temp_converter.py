import tkinter as tk  # Import the base tkinter GUI module
from tkinter import ttk  # Import ttk for themed (modern looking) widgets


# -------------------- Function to perform conversion -----------------------
# This function runs when the "Convert" button is clicked
def convert():
    # Get the user input from the entry box and convert it to a float
    fahrenheit = float(fahrenhiet_entry.get())

    # Convert Fahrenheit to Celsius using the formula
    celsius = (fahrenheit - 32) * 5 / 9

    # Update the label below with the converted temperature
    results_label.config(text=f"Temperature in Celsius: {celsius:.2f}")


# ---------------------------------------------------------------------------

# Create the main application window
root = tk.Tk()
root.title('Fahrenheit to Celsius Converter')  # Title of the window

# Create a frame (a container inside the window) with padding
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
# Place the frame in the top-left of the window and let it expand in all directions

# ----------------------- Row 0: Label + Input Box -------------------------

# Create a label prompting the user to enter Fahrenheit temperature
fahrenhiet_label = ttk.Label(frame, text="Enter the temperature in Fahrenheit: ")
fahrenhiet_label.grid(row=0, column=0, sticky=tk.S)  # Place the label in row 0, column 0

# Create an entry box (input field) where the user types the temperature
fahrenhiet_entry = ttk.Entry(frame, width=15)
fahrenhiet_entry.grid(row=0, column=1, sticky=tk.W)  # Place it to the right of the label
fahrenhiet_entry.focus()  # Automatically place the cursor inside the box when app opens

# ----------------------- Row 1: Convert Button ----------------------------

# Create a button labeled "Convert" and link it to the convert() function
convert_button = ttk.Button(frame, text="Convert", command=convert)
convert_button.grid(row=1, column=0, sticky=tk.W)  # Place it in row 1, column 0

# ----------------------- Row 2: Output Label ------------------------------

# Create a label to display the result of the conversion
results_label = ttk.Label(frame, text="Temperature in Celsius: ")
results_label.grid(row=2, column=0, columnspan=2)
# Span across 2 columns so it's centered under both label + input

# ----------------------- Start the GUI Loop -------------------------------

# This keeps the window open and running, waiting for user interaction
root.mainloop()

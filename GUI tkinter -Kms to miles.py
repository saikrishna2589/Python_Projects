import tkinter as tk  # Import tkinter module to create GUI window
from tkinter import ttk  # Import ttk for modern-looking widgets


# ---------------- Function to Convert Kilometers to Miles ------------------
def convert():
    # Get the input from the user as a string, convert it to float
    kilometer_input = float(entry_box.get())

    # Multiply by 0.621 to convert km to miles
    miles = 0.621 * kilometer_input

    # Update the result label with formatted text showing km and miles
    return results_label.config(text=f"{kilometer_input:.0f} kms is {miles:.2f} miles")


# ---------------------------------------------------------------------------

# Create the main window
root = tk.Tk()
root.title("Convert Kms to miles")  # Set the window title

# Create a frame (section inside the window) to hold widgets with padding
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.W, tk.S))
# Put frame at top-left corner and make it stick to all directions

# ----------------------- Row 0: Label and Entry Box -----------------------

# Create a label to ask the user for input in kilometers
label = ttk.Label(frame, text="Enter the distance in Kilometers: ")
label.grid(row=0, column=0)  # Place the label at row 0, column 0

# Create an entry box where user types the distance
entry_box = ttk.Entry(frame, width=15)
entry_box.grid(row=0, column=1, sticky=tk.W)  # Place entry box to the right of the label
entry_box.focus()  # Automatically puts the cursor in this box when window opens

# ----------------------- Row 1: Convert Button ----------------------------

# Create a button labeled "Convert kms to miles" which runs convert() when clicked
convert_button = ttk.Button(frame, text="Convert kms to miles", command=convert)
convert_button.grid(row=1, column=0, sticky=tk.W)  # Place the button under the label

# ----------------------- Row 2: Output Label ------------------------------

# Create a label to show the result of conversion (initially placeholder text)
results_label = ttk.Label(frame, text="Kms in Miles : ")
results_label.grid(row=2, column=0, columnspan=2)
# Span across both columns so it’s centered nicely below input and button

# ----------------------- Start GUI Event Loop -----------------------------

root.mainloop()  # Keep the window open and responsive (wait for user actions)

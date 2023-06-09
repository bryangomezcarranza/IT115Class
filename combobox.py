#
import tkinter as tk 
from tkinter import ttk

# define function for event 
def onSelect(event):
    # created the event that will be selected and pass it on the print statement. 
    selected_item = event.widget.get()
    print("Selected item:", selected_item)

# Creates a root window and set title 
rootWindow = tk.Tk()
rootWindow.title("Button Example")

# Create an Array of items
items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]

# Add items into the combobox 
combo_box = ttk.Combobox(rootWindow, values=items)

# Bind selected event to the function 
combo_box.bind("<<ComboboxSelected>>", onSelect)
combo_box.pack()

# Runs main event loop for tk 
rootWindow.mainloop()
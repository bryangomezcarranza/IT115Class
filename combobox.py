#
import tkinter as tk 
from tkinter import ttk

# define function for event 
def  onSelect(event):
    # created the event that will be selected and pass it on the print statement. 
    selected_item = event.widget.get()
    print("Selected item:", selected_item)


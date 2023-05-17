# Imports tkinter library
import tkinter as tk 

# Define function for when the button is clicked
def buttonClick():
    print("Button Clicked")


# Creates a window and sets title 
root = tk.Tk()
root.title("Button Example")

# Creates Button with root window, text label, and command. 
button = tk.Button(root, text="Click Me", command=buttonClick)
button.pack()

# Runs main event loop for tk 
root.mainloop()
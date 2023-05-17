# 
import tkinter as tk 

# Define function for when the button is clicked
def buttonClick():
    print("Button Clicked")


#
root = tk.Tk()
root.title("Button Example")

# Creates Button w root window, text label, and command. 
button = tk.Button(root, text="Click Me", command=buttonClick)
button.pack()

root.mainloop()
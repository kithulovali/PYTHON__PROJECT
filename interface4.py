# this is the add window for the tracker
# author : kithulovali

import tkinter as tk
from tkinter import *
import subprocess
from tkinter import ttk

root = tk.Tk()
root.geometry("600x600")
root.title("view window " )

# Create the menu bar

menu_bar = tk.Menu(root, font=("Arial", 15))

#go back to the main menu

def go_back():
    root.destroy() 
    subprocess.run(["python", "interface3.py"]) 
    
def open_interface_add():
    root.destroy() 
    subprocess.run(["python", "interface_add.py"])
    
# Working with the menu bar

file_menu = tk.Menu(menu_bar, tearoff=0, font=("Arial", 15))
file_menu.add_command(label="Add", command=open_interface_add )
file_menu.add_command(label="back", command=go_back )

menu_bar.add_cascade(label="Menu", menu=file_menu, font=("Arial", 15))

# Set the menu bar on the root window

root.config(menu=menu_bar)

# Working with the image

Tracker_icon = tk.PhotoImage(file="tracker.png")
subsampled_icon = Tracker_icon.subsample(7, 7)  

# Create a Frame to hold the image and menu on the same level

top_frame = tk.Frame(root)
top_frame.pack(pady=10, anchor="n", padx=5)

# Display the image in the top frame

display_Icon = tk.Label(top_frame, image=subsampled_icon)
display_Icon.pack(side=tk.LEFT, padx=10)
columns = ("ID", "Column 1", "Column 2", "Column 3", "Column 4")
tree = ttk.Treeview(root, columns=columns, show="headings")

# Define column headings

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)

# Pack the table into the window

tree.pack(fill="both", expand=True)

# Auto-incrementing row counter

row_count = 0

root.mainloop()

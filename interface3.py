# this is the main window for the tracker
# author : kithulovali

import tkinter as tk
from tkinter import *
import subprocess

# Set up the main window

root = tk.Tk()
root.geometry("600x600")
root.title("Expense Tracker " )

# going to window interface 4

def open_interface4():
    root.destroy()  
    subprocess.run(["python", "interface4.py"])  

# going to interface add

def open_interface_add():
    root.destroy() 
    subprocess.run(["python", "interface_add.py"])
    
# Create the menu bar

menu_bar = tk.Menu(root, font=("Arial", 15))

# Working with the menu bar

file_menu = tk.Menu(menu_bar, tearoff=0, font=("Arial", 15))
file_menu.add_command(label="Add",command=open_interface_add )
file_menu.add_command(label="View", command=open_interface4 )

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

# The welcome frame

welcome = tk.Label(root, text="Welcome to your daily Expense Tracker", font=("Arial",21), bd=10, relief="sunken", padx=20, pady=20)
welcome.pack(pady=5)

# Create a search entry box and button

search_frame = tk.Frame(root)
search_frame.pack(pady=10)
search_entry = tk.Entry(search_frame, width=30, font=("Arial", 14), bd=3, relief="solid")
search_entry.pack(side=tk.LEFT, padx=5, pady=5)
search_entry.config(bg="#f0f0f0", relief="flat", highlightthickness=2, highlightbackground="gray")

# Create a search button

search_button = tk.Button(search_frame, text="Search", font=("Arial", 14))
search_button.pack(side=tk.LEFT, padx=5)

# creating a log out button

search_button = tk.Button(search_frame, text="Log out", font=("Arial", 14) , command="exit")
search_button.pack(padx=5)  

# Run the application
root.mainloop()

import tkinter as tk
from tkinter import ttk, PhotoImage, messagebox
import subprocess
import os

# Initialize main window
root = tk.Tk()
root.geometry("600x600")
root.title("View Window")
root.configure(bg="#f0f0f0")  # Background color

# Menu bar
menu_bar = tk.Menu(root, font=("Arial", 15))

def go_back():
    root.destroy()
    subprocess.run(["python", "InterfaceMain.py"])

def open_interface_add():
    root.destroy()
    subprocess.run(["python", "InterfaceAdd.py"])

# File menu
file_menu = tk.Menu(menu_bar, tearoff=0, font=("Arial", 15))
file_menu.add_command(label="Add", command=open_interface_add)
file_menu.add_command(label="Back", command=go_back)
menu_bar.add_cascade(label="Menu", menu=file_menu)
root.config(menu=menu_bar)

# Load and resize icon
Tracker_icon = tk.PhotoImage(file="tracker.png")
subsampled_icon = Tracker_icon.subsample(7, 7)

# Create a frame to center the image
image_frame = tk.Frame(root, bg="#f0f0f0")
image_frame.pack(pady=20)  # Adds vertical space

# Display icon (Centered)
display_Icon = tk.Label(image_frame, image=subsampled_icon, bg="#f0f0f0")
display_Icon.pack(anchor="center")  # Centering the image

# Table columns
columns = ("ID", "Column 1", "Column 2", "Column 3", "Column 4")
tree = ttk.Treeview(root, columns=columns, show="headings")

# Define column headings
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)

# Pack the table
tree.pack(fill="both", expand=True, padx=10, pady=10)

# Run the Tkinter main loop
root.mainloop()

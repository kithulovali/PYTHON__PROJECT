import tkinter as tk
from tkinter import ttk, PhotoImage, messagebox
import subprocess

# Set up the main window
root = tk.Tk()
root.geometry("600x600")
root.title("Expense Tracker")
root.configure(bg="#f0f0f0")  # Background color

# Functions to navigate between interfaces
def open_interface4():
    root.destroy()
    subprocess.run(["python", "InterfaceView.py"])

def open_interface_add():
    root.destroy()
    subprocess.run(["python", "InterfaceAdd.py"])

def open_InterfaceLogIn():
    root.destroy()
    subprocess.run(["python", "InterfaceLogIn.py"])    

# Create the menu bar
menu_bar = tk.Menu(root, font=("Arial", 15))

# Menu options
file_menu = tk.Menu(menu_bar, tearoff=0, font=("Arial", 15))
file_menu.add_command(label="Add", command=open_interface_add)
file_menu.add_command(label="View", command=open_interface4)
menu_bar.add_cascade(label="Menu", menu=file_menu)
root.config(menu=menu_bar)

# Load and resize icon
Tracker_icon = tk.PhotoImage(file="tracker.png")
subsampled_icon = Tracker_icon.subsample(7, 7)

# Frame to center elements
center_frame = tk.Frame(root, bg="#f0f0f0")
center_frame.pack(expand=True)

# Display icon (Centered)
display_Icon = tk.Label(center_frame, image=subsampled_icon, bg="#f0f0f0")
display_Icon.pack(pady=10)  # Adds space around the icon

# Welcome message (Centered)
welcome = tk.Label(center_frame, text="Welcome to your daily Expense Tracker", 
                    font=("Arial", 21), bd=10, relief="sunken", padx=20, pady=20, 
                    bg="#f0f0f0")
welcome.pack(pady=10)

# Search bar (Centered)
search_frame = tk.Frame(center_frame, bg="#f0f0f0")
search_frame.pack(pady=10)
search_entry = tk.Entry(search_frame, width=30, font=("Arial", 14), bd=3, relief="solid", bg="#ffffff")
search_entry.pack(side=tk.LEFT, padx=5, pady=5)

# Search button
search_button = tk.Button(search_frame, text="Search", font=("Arial", 14), bg="#007BFF", fg="white")
search_button.pack(side=tk.LEFT, padx=5)

# Log out button
logout_button = tk.Button(center_frame, text="Log out", font=("Arial", 14), bg="#DC3545", fg="white", command=open_InterfaceLogIn)
logout_button.pack(pady=10)

# Run the application
root.mainloop()

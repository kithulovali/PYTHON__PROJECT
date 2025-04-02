import tkinter as tk
from tkinter import messagebox
import subprocess
# Initialize main window
root = tk.Tk()
root.geometry("600x600")
root.title("CREATE ACCOUNT")
root.configure(bg="#f0f0f0")  # Background color

# Load and resize default icon
Tracker_icon = tk.PhotoImage(file="tracker.png")
subsampled_icon = Tracker_icon.subsample(7, 7)

# Function to open the main interface
def open_interface_():
    root.destroy()
    subprocess.run(["python", "InterfaceMain.py"])
def open_interface_create():
    root.destroy()
    subprocess.run(["python", "InterfaceNewAccount.py"])

top_frame = tk.Frame(root, bg="#f0f0f0")
top_frame.pack(pady=10, padx=5, fill=tk.X)

# Center the icon in the middle of the page
display_Icon = tk.Label(root, image=subsampled_icon, bg="#f0f0f0")
display_Icon.pack(expand=True)

# Welcome label
welcome = tk.Label(root, text="Welcome to Daily Expense Tracker", font=("Arial", 18, "bold"), bd=5, relief="sunken", padx=20, pady=10, bg="#ffffff")
welcome.pack(pady=5, fill=tk.X, padx=10)

# Frame for Name Entry
NameFrame = tk.Frame(root, bg="#f0f0f0")
NameFrame.pack(pady=10, fill=tk.X, padx=50)

Namelabel = tk.Label(NameFrame, text="Name", font=("Arial", 15), bg="#f0f0f0")
Namelabel.pack(side=tk.LEFT)

NameEntry = tk.Entry(NameFrame, width=25, font=("Arial", 14), bd=3)
NameEntry.pack(side=tk.RIGHT)

# Frame for Password Entry
PasswordFrame = tk.Frame(root, bg="#f0f0f0")
PasswordFrame.pack(pady=10, fill=tk.X, padx=50)

PasswordLabel = tk.Label(PasswordFrame, text="Password", font=("Arial", 15), bg="#f0f0f0")
PasswordLabel.pack(side=tk.LEFT)

PasswordEntry = tk.Entry(PasswordFrame, width=25, font=("Arial", 14), bd=3, show="*")
PasswordEntry.pack(side=tk.RIGHT)

# Button Frame
ButtonFrame = tk.Frame(root, bg="#f0f0f0")
ButtonFrame.pack(pady=20)

SubmitButton = tk.Button(ButtonFrame, text="Enter", font=("Arial", 14), bg="#007bff", fg="white", padx=10, pady=5, command=open_interface_)
SubmitButton.pack(side=tk.LEFT, padx=20)

CreateButton = tk.Button(ButtonFrame, text="New Account", font=("Arial", 14), bg="#28a745", fg="white", padx=10, pady=5, command=open_interface_create)
CreateButton.pack(side=tk.RIGHT, padx=20)

# Show initial message
messagebox.showinfo("Login", "WELCOME TO YOUR DAILY EXPENSE TRACKER\nSIGN UP OR CREATE AN ACCOUNT")

root.mainloop()

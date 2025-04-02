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
    """Close current window and go back to interface3."""
    root.destroy()
    subprocess.run(["python", "interface3.py"])

def open_interface_add():
    """Close current window and open interface_add."""
    root.destroy()
    subprocess.run(["python", "interface_add.py"])

def load_profile_image():
    """Load and display the profile image from the saved file path."""
    try:
        if os.path.exists("profile_image.txt"):
            # Read the saved image path from the file
            with open("profile_image.txt", "r") as file:
                uploaded_image_path = file.read().strip()
            
            if uploaded_image_path:  # If the path is not empty
                if os.path.exists(uploaded_image_path):  # Check if file exists
                    UserIcon = PhotoImage(file=uploaded_image_path)
                    Usericon = UserIcon.subsample(7, 7)
                    ProfileIcon.config(image=Usericon)  # Update the profile picture
                else:
                    messagebox.showwarning("Image Error", "The saved profile image path is invalid.")
            else:
                messagebox.showwarning("Image Error", "No profile image found.")
        else:
            messagebox.showwarning("File Not Found", "profile_image.txt not found!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while loading the image: {e}")

# File menu
file_menu = tk.Menu(menu_bar, tearoff=0, font=("Arial", 15))
file_menu.add_command(label="Add", command=open_interface_add)
file_menu.add_command(label="Back", command=go_back)
menu_bar.add_cascade(label="Menu", menu=file_menu)
root.config(menu=menu_bar)

# Load and resize icon
Tracker_icon = tk.PhotoImage(file="tracker.png")
subsampled_icon = Tracker_icon.subsample(7, 7)

# Top frame
top_frame = tk.Frame(root, bg="#f0f0f0")
top_frame.pack(pady=10, padx=5, fill=tk.X)

# Display icon
display_Icon = tk.Label(top_frame, image=subsampled_icon, bg="#f0f0f0")
display_Icon.pack(side=tk.LEFT, padx=10)

# Profile icon (this will be updated with the uploaded image)
ProfileIcon = tk.Label(top_frame, bg="#f0f0f0")
ProfileIcon.pack(side=tk.RIGHT, padx=10)

# Load profile image on startup
load_profile_image()

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

import tkinter as tk
from tkinter import ttk, messagebox, PhotoImage
import subprocess

# Initialize the main application window
root = tk.Tk()
root.title("Auto-Increment Table")
root.geometry("600x600")

# Functions to navigate between interfaces
def go_back():
    root.destroy()
    subprocess.run(["python", "InterfaceMain.py"])

def open_interface4():
    root.destroy()
    subprocess.run(["python", "InterfaceView.py"])


# Create the menu bar
menu_bar = tk.Menu(root, font=("Arial", 15))

file_menu = tk.Menu(menu_bar, tearoff=0, font=("Arial", 15))
file_menu.add_command(label="View", command=open_interface4)
file_menu.add_command(label="Back", command=go_back)

menu_bar.add_cascade(label="Menu", menu=file_menu)
root.config(menu=menu_bar)

# Load and display tracker icon
try:
    tracker_icon = tk.PhotoImage(file="tracker.png")
    subsampled_icon = tracker_icon.subsample(7, 7)
    icon_label = tk.Label(root, image=subsampled_icon)
    icon_label.pack(pady=5)
    icon_label.image = subsampled_icon  # Prevent garbage collection
except Exception as e:
    print(f"Warning: Tracker image file not found! Error: {e}")

# Create a Treeview widget (Table)
columns = ("ID", "DESCRIPTION", "AMOUNT", "DATE")
tree = ttk.Treeview(root, columns=columns, show="headings")

# Define column headings
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=140, anchor="center")

tree.pack(fill="both", expand=True, pady=10)

# Auto-incrementing row counter
row_count = 0

# Entry fields for editing rows
entry_col1 = tk.Entry(root, width=20)
entry_col2 = tk.Entry(root, width=20)
entry_col3 = tk.Entry(root, width=20)

entry_col1.pack(side="left", padx=5, pady=5)
entry_col2.pack(side="left", padx=5, pady=5)
entry_col3.pack(side="left", padx=5, pady=5)

# Function to add a new row
def add_row():
    global row_count
    row_count += 1
    data1 = entry_col1.get() or f"Data {row_count}-1"
    data2 = entry_col2.get() or f"Data {row_count}-2"
    data3 = entry_col3.get() or f"Data {row_count}-3"

    tree.insert("", "end", values=(row_count, data1, data2, data3))
    
    entry_col1.delete(0, tk.END)
    entry_col2.delete(0, tk.END)
    entry_col3.delete(0, tk.END)

# Function to delete selected row
def delete_row():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Warning", "Please select a row to delete.")
        return

    for item in selected_item:
        tree.delete(item)

# Function to update selected row
def update_row():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Warning", "Please select a row to update.")
        return

    new_data1 = entry_col1.get()
    new_data2 = entry_col2.get()
    new_data3 = entry_col3.get()

    if not (new_data1 and new_data2 and new_data3):
        messagebox.showwarning("Warning", "All fields must be filled to update.")
        return

    tree.item(selected_item, values=(tree.item(selected_item)["values"][0], new_data1, new_data2, new_data3))

    entry_col1.delete(0, tk.END)
    entry_col2.delete(0, tk.END)
    entry_col3.delete(0, tk.END)

# Buttons for actions
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

add_button = tk.Button(btn_frame, text="Add Row", command=add_row)
update_button = tk.Button(btn_frame, text="Update Row", command=update_row)
delete_button = tk.Button(btn_frame, text="Delete Row", fg="red", command=delete_row)  # Added the command here

add_button.pack(side="left", padx=5)
update_button.pack(side="left", padx=5)
delete_button.pack(side="left", padx=5)

# Run the application
root.mainloop()

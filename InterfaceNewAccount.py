import tkinter as tk
from tkinter import messagebox

# Initialize main window
root = tk.Tk()
root.geometry("600x600")
root.title("CREATE ACCOUNT")
root.configure(bg="#f0f0f0")  # Background color

# Load and resize default icon (logo)
Tracker_icon = tk.PhotoImage(file="tracker.png")  # Make sure this is your logo file
subsampled_icon = Tracker_icon.subsample(7, 7)

# Function to handle account creation
def create_account():
    name = NameEntry.get().strip()
    password = PasswordEntry.get().strip()
    confirm_password = ConfirmPasswordEntry.get().strip()

    if not name or not password or not confirm_password:
        messagebox.showerror("Error", "All fields are required")
        return

    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match")
        return

    messagebox.showinfo("Success", f"Account for {name} created successfully!")

# Function to show New Account Registration Form
def show_create_account_form():
    # Clear the current window
    for widget in root.winfo_children():
        widget.destroy()

    # Display Company Logo at the top center
    logo_label = tk.Label(root, image=subsampled_icon, bg="#f0f0f0")
    logo_label.pack(pady=20)

    # Display New Account form
    welcome_label = tk.Label(root, text="Create New Account", font=("Arial", 18, "bold"), bd=5, relief="sunken", padx=20, pady=10, bg="#ffffff")
    welcome_label.pack(pady=5, fill=tk.X, padx=10)

    # Frame for Name Entry
    NameFrame = tk.Frame(root, bg="#f0f0f0")
    NameFrame.pack(pady=10, fill=tk.X, padx=50)

    Namelabel = tk.Label(NameFrame, text="Name", font=("Arial", 15), bg="#f0f0f0")
    Namelabel.pack(side=tk.LEFT)

    global NameEntry  # Make NameEntry global
    NameEntry = tk.Entry(NameFrame, width=25, font=("Arial", 14), bd=3)
    NameEntry.pack(side=tk.RIGHT)

    # Frame for Password Entry
    PasswordFrame = tk.Frame(root, bg="#f0f0f0")
    PasswordFrame.pack(pady=10, fill=tk.X, padx=50)

    PasswordLabel = tk.Label(PasswordFrame, text="Password", font=("Arial", 15), bg="#f0f0f0")
    PasswordLabel.pack(side=tk.LEFT)

    global PasswordEntry  # Make PasswordEntry global
    PasswordEntry = tk.Entry(PasswordFrame, width=25, font=("Arial", 14), bd=3, show="*")
    PasswordEntry.pack(side=tk.RIGHT)

    # Frame for Confirm Password Entry
    ConfirmPasswordFrame = tk.Frame(root, bg="#f0f0f0")
    ConfirmPasswordFrame.pack(pady=10, fill=tk.X, padx=50)

    ConfirmPasswordLabel = tk.Label(ConfirmPasswordFrame, text="Confirm Password", font=("Arial", 15), bg="#f0f0f0")
    ConfirmPasswordLabel.pack(side=tk.LEFT)

    global ConfirmPasswordEntry  # Make ConfirmPasswordEntry global
    ConfirmPasswordEntry = tk.Entry(ConfirmPasswordFrame, width=25, font=("Arial", 14), bd=3, show="*")
    ConfirmPasswordEntry.pack(side=tk.RIGHT)

    # Button Frame for submitting form
    ButtonFrame = tk.Frame(root, bg="#f0f0f0")
    ButtonFrame.pack(pady=20)

    # Create Account Button
    CreateAccountButton = tk.Button(ButtonFrame, text="Create Account", font=("Arial", 14), bg="#007bff", fg="white", padx=10, pady=5, command=create_account)
    CreateAccountButton.pack(side=tk.LEFT, padx=20)

# Initial call to display the new account form
show_create_account_form()

root.mainloop()

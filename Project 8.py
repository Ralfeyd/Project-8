# Luke Duran
# 04/06/25

#step 1 creates database file and connects
import sqlite3

conn = sqlite3.connect('customers.db')  #Creates the file
cursor = conn.cursor()  # connects the file

cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        birthday TEXT,
        email TEXT,
        phone TEXT,
        address TEXT,
        contact_method TEXT
    )
''')

conn.commit() # Save changes
conn.close() # Close connection



# start of GUI code

import tkinter as tk
from tkinter import ttk, messagebox

def submit_form():
    name = name_entry.get()
    birthday = birthday_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    address = address_entry.get()
    contact_method = contact_method_var.get()

    if name.strip() == "":
        messagebox.showerror("Error", "Name is required.")
        return

    conn = sqlite3.connect('customers.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO customers (name, birthday, email, phone, address, contact_method)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (name, birthday, email, phone, address, contact_method))
    conn.commit()
    conn.close()

    # Clear the form
    name_entry.delete(0, tk.END)
    birthday_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    contact_method_var.set(contact_options[0])  # Reset dropdown

    messagebox.showinfo("Success", "Customer information submitted!")

# GUI Setup
root = tk.Tk()
root.title("Customer Information Form")

# Labels & Entries
tk.Label(root, text="Name").grid(row=0, column=0, sticky='e')
tk.Label(root, text="Birthday (YYYY-MM-DD)").grid(row=1, column=0, sticky='e')
tk.Label(root, text="Email").grid(row=2, column=0, sticky='e')
tk.Label(root, text="Phone").grid(row=3, column=0, sticky='e')
tk.Label(root, text="Address").grid(row=4, column=0, sticky='e')
tk.Label(root, text="Preferred Contact").grid(row=5, column=0, sticky='e')

name_entry = tk.Entry(root, width=30)
birthday_entry = tk.Entry(root, width=30)
email_entry = tk.Entry(root, width=30)
phone_entry = tk.Entry(root, width=30)
address_entry = tk.Entry(root, width=30)

name_entry.grid(row=0, column=1, padx=10, pady=5)
birthday_entry.grid(row=1, column=1, padx=10, pady=5)
email_entry.grid(row=2, column=1, padx=10, pady=5)
phone_entry.grid(row=3, column=1, padx=10, pady=5)
address_entry.grid(row=4, column=1, padx=10, pady=5)

# Dropdown for contact method
contact_options = ["Email", "Phone", "Mail"]
contact_method_var = tk.StringVar()
contact_method_var.set(contact_options[0])  # Default value

contact_menu = ttk.OptionMenu(root, contact_method_var, contact_options[0], *contact_options)
contact_menu.grid(row=5, column=1, padx=10, pady=5)

# Submit Button
submit_btn = tk.Button(root, text="Submit", command=submit_form)
submit_btn.grid(row=6, column=0, columnspan=2, pady=15)

root.mainloop()

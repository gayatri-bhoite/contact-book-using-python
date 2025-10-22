import tkinter as tk
from tkinter import messagebox

# Contact storage (in-memory dictionary)
contacts = {}

# --- Functions ---

def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    address = address_entry.get().strip()

    if name == "" or phone == "":
        messagebox.showwarning("Input Error", "Name and Phone Number are required!")
        return

    contacts[name] = {"Phone": phone, "Email": email, "Address": address}
    messagebox.showinfo("Success", f"Contact '{name}' added successfully!")
    clear_entries()
    display_contacts()


def display_contacts():
    contact_list.delete(0, tk.END)
    for name, info in contacts.items():
        contact_list.insert(tk.END, f"{name} - {info['Phone']}")


def search_contact():
    query = search_entry.get().strip().lower()
    contact_list.delete(0, tk.END)
    found = False
    for name, info in contacts.items():
        if query in name.lower() or query in info['Phone']:
            contact_list.insert(tk.END, f"{name} - {info['Phone']}")
            found = True
    if not found:
        contact_list.insert(tk.END, "No contact found!")


def delete_contact():
    selected = contact_list.curselection()
    if not selected:
        messagebox.showwarning("Select Contact", "Please select a contact to delete.")
        return
    contact_text = contact_list.get(selected[0])
    name = contact_text.split(" - ")[0]
    if name in contacts:
        del contacts[name]
        messagebox.showinfo("Deleted", f"Contact '{name}' deleted successfully!")
        display_contacts()


def update_contact():
    selected = contact_list.curselection()
    if not selected:
        messagebox.showwarning("Select Contact", "Please select a contact to update.")
        return
    contact_text = contact_list.get(selected[0])
    name = contact_text.split(" - ")[0]

    if name in contacts:
        contacts[name]["Phone"] = phone_entry.get().strip()
        contacts[name]["Email"] = email_entry.get().strip()
        contacts[name]["Address"] = address_entry.get().strip()
        messagebox.showinfo("Updated", f"Contact '{name}' updated successfully!")
        display_contacts()


def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)


# --- GUI Setup ---
window = tk.Tk()
window.title("📞 Contact Book")
window.geometry("500x550")
window.config(bg="#2d3436")

# Title
tk.Label(window, text="Contact Book", font=("Arial", 16, "bold"), bg="#2d3436", fg="white").pack(pady=10)

# Frame for contact form
form_frame = tk.Frame(window, bg="#2d3436")
form_frame.pack(pady=10)

tk.Label(form_frame, text="Name:", bg="#2d3436", fg="white").grid(row=0, column=0, padx=5, pady=5, sticky="w")
name_entry = tk.Entry(form_frame, width=40)
name_entry.grid(row=0, column=1, pady=5)

tk.Label(form_frame, text="Phone:", bg="#2d3436", fg="white").grid(row=1, column=0, padx=5, pady=5, sticky="w")
phone_entry = tk.Entry(form_frame, width=40)
phone_entry.grid(row=1, column=1, pady=5)

tk.Label(form_frame, text="Email:", bg="#2d3436", fg="white").grid(row=2, column=0, padx=5, pady=5, sticky="w")
email_entry = tk.Entry(form_frame, width=40)
email_entry.grid(row=2, column=1, pady=5)

tk.Label(form_frame, text="Address:", bg="#2d3436", fg="white").grid(row=3, column=0, padx=5, pady=5, sticky="w")
address_entry = tk.Entry(form_frame, width=40)
address_entry.grid(row=3, column=1, pady=5)

# Buttons
tk.Button(window, text="Add Contact", command=add_contact, bg="#00b894", fg="white", width=15).pack(pady=5)
tk.Button(window, text="Update Contact", command=update_contact, bg="#0984e3", fg="white", width=15).pack(pady=5)
tk.Button(window, text="Delete Contact", command=delete_contact, bg="#d63031", fg="white", width=15).pack(pady=5)

# Search
tk.Label(window, text="Search:", bg="#2d3436", fg="white").pack(pady=5)
search_entry = tk.Entry(window, width=30)
search_entry.pack()
tk.Button(window, text="Search Contact", command=search_contact, bg="#6c5ce7", fg="white", width=15).pack(pady=5)

# Contact List
tk.Label(window, text="Contact List:", bg="#2d3436", fg="white").pack(pady=5)
contact_list = tk.Listbox(window, width=50, height=10)
contact_list.pack(pady=10)

# Show all contacts on start
display_contacts()

# Run the GUI
window.mainloop()

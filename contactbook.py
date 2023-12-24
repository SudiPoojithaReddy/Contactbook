import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self, master):
        self.master = master
        self.master.title("Contact Book")

        # Contacts list
        self.contacts = []

        # Create widgets
        self.name_label = tk.Label(master, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=5)

        self.name_entry = tk.Entry(master, width=30)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.phone_label = tk.Label(master, text="Phone:")
        self.phone_label.grid(row=1, column=0, padx=10, pady=5)

        self.phone_entry = tk.Entry(master, width=30)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)

        self.add_button = tk.Button(master, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.contact_listbox = tk.Listbox(master, width=40, height=10)
        self.contact_listbox.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

        self.remove_button = tk.Button(master, text="Remove Contact", command=self.remove_contact)
        self.remove_button.grid(row=4, column=0, columnspan=2, pady=5)

        # Bind double click event to listbox item
        self.contact_listbox.bind('<Double-Button-1>', self.edit_contact)

        # Load contacts initially
        self.update_contact_list()

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()

        if name and phone:
            contact = {"Name": name, "Phone": phone}
            self.contacts.append(contact)
            self.update_contact_list()
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter both name and phone number.")

    def remove_contact(self):
        try:
            selected_index = self.contact_listbox.curselection()[0]
            del self.contacts[selected_index]
            self.update_contact_list()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a contact to remove.")

    def edit_contact(self, event):
        try:
            selected_index = self.contact_listbox.curselection()[0]
            selected_contact = self.contacts[selected_index]
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
            self.name_entry.insert(tk.END, selected_contact["Name"])
            self.phone_entry.insert(tk.END, selected_contact["Phone"])
            self.remove_contact()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a contact to edit.")

    def update_contact_list(self):
        self.contact_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contact_listbox.insert(tk.END, f"{contact['Name']} - {contact['Phone']}")

def main():
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()

if __name__ == "__main__":
    main()

import tkinter as tk
from tkinter import ttk, messagebox
from pymongo import MongoClient

def encrypt(plain_text, shift):
    encrypted_text = ''
    for char in plain_text:
        encrypted_char = chr((ord(char) + shift) % 1114112)
        encrypted_text += encrypted_char
    return encrypted_text

def decrypt(encrypted_text, shift):
    decrypted_text = ''
    for char in encrypted_text:
        decrypted_char = chr((ord(char) - shift) % 1114112)  
        decrypted_text += decrypted_char
    return decrypted_text

def copy_to_clipboard(password_text, app):
    try:
        output = password_text.get(1.0, tk.END).strip()  
        if output:
            app.clipboard_clear()
            app.clipboard_append(output)
            app.update()
            messagebox.showinfo("Success", "Copied to clipboard!")
        else:
            messagebox.showwarning("Warning", "No password to copy!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to copy to clipboard: {e}")

def pwd_manager_gui(root):
    client = MongoClient("mongodb://localhost:27017/")
    db = client['Semester_6_Project']
    collection = db['pass_manager']

    shift_value = 6

    def save_password():
        label = label_entry.get()
        password = password_entry.get()

        if not label or not password:
            messagebox.showerror("Error", "Both fields are required!")
            return

        encrypted_password = encrypt(password, shift_value)
        data_to_insert = {"label": label, "password": encrypted_password}
        collection.insert_one(data_to_insert)
        messagebox.showinfo("Success", f"Password for {label} saved successfully!")
        label_entry.delete(0, 'end')
        password_entry.delete(0, 'end')

    def retrieve_password():
        label = label_entry.get()

        if not label:
            messagebox.showerror("Error", "Label is required!")
            return

        result = collection.find_one({"label": label})

        if not result:
            messagebox.showerror("Error", "Label not found!")
            return

        encrypted_password = result['password']
        try:
            decrypted_password = decrypt(encrypted_password, shift_value)
            password_text.delete(1.0, tk.END)
            password_text.insert(tk.END, decrypted_password)
            messagebox.showinfo("Retrieved Password", f"Password for {label} retrieved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Decryption failed: {str(e)}")

    app = tk.Toplevel(root)
    app.title("Password Manager with Custom Cipher Encryption")
    app.geometry("500x500")
    app.configure(background="#010c25")
    app.resizable(False,False)

    btnstyle = ttk.Style()
    btnstyle.configure(
        "Custom.TButton", 
        padding=(20, 10),
        font=("Terminal",14,'bold'),
        borderwidth = '5'
    )
    btnstyle.map('Custom.TButton', foreground=[('active', '!disabled', 'green')],
                     background=[('active', 'black')])

    tk.Label(app, text="Label:", font=("Cascadia Mono Semibold", 12), foreground="#6cd656", background="#010c25").place(x=10, y=20)
    label_entry = tk.Entry(app, width=25, font=("Terminal"), bg="#6cd656", relief=tk.SUNKEN)
    label_entry.place(x=100, y=20)

    tk.Label(app, text="Password:", font=("Cascadia Mono Semibold", 12), foreground="#6cd656", background="#010c25").place(x=10, y=60)
    password_entry = tk.Entry(app, width=25, font=("Terminal"), bg="#6cd656", relief=tk.SUNKEN, show='*')
    password_entry.place(x=100, y=60)

    ttk.Button(app, text="Save Password", command=save_password, style='Custom.TButton').place(x=120, y=100)
    ttk.Button(app, text="Retrieve Password", command=retrieve_password, style='Custom.TButton').place(x=110, y=160)

    tk.Label(app, text="Retrieved Password:", font=("Cascadia Mono Semibold", 12), foreground="#6cd656", background="#010c25").place(x=10, y=220)
    password_text = tk.Text(app, height=3, width=20, font=("Terminal"), bg="#6cd656", relief=tk.SUNKEN)
    password_text.place(x=200, y=220)

    copy_button = ttk.Button(app, text="Copy to Clipboard", command=lambda: copy_to_clipboard(password_text, app), style='Custom.TButton')
    copy_button.place(x=120, y=300)

    close_button = ttk.Button(app, text="Close", command=app.destroy,style="Custom.TButton")
    close_button.place(x=150, y=390)

    app.mainloop()

    client.close()

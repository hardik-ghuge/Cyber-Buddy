import random
import string
from tkinter import *
from tkinter import ttk, messagebox

def password_generator_gui(root):
    def generate_password():
        
        try:
            length = int(length_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for the length.")
            return

        if length < 1:
            messagebox.showerror("Error", "Password length must be greater than 0.")
            return

        
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.sample(characters, length))

        
        password_entry.delete(0, END)
        password_entry.insert(0, password)

    
    window = Toplevel(root)
    window.title("Password Generator")
    window.geometry("500x300")
    window.configure(background="#010c25")
    window.resizable(False,False)
    
    btnstyle = ttk.Style()
    btnstyle.configure(
        "Custom.TButton", 
        padding=(20, 10),
        font=("Terminal",14,'bold'),
        borderwidth = '5'
        #background="LightSteelBlue3",
        #foreground="black"   
    )
    btnstyle.map('Custom.TButton', foreground = [('active', '!disabled', 'green')],
                     background = [('active', 'black')])

    
    Label(window, text="Enter Password Length:", font=("Cascadia Mono Semibold", 12),foreground="#6cd656",background="#010c25").place(x=10, y=20)
    length_entry = Entry(window, width=10, font=("Terminal"),bg="#6cd656", relief=SUNKEN)
    length_entry.place(x=220, y=20)

    
    ttk.Button(window, text="Generate Password", style="Custom.TButton", command=generate_password).place(x=180, y=60)

    
    Label(window, text="Generated Password:", font=("Cascadia Mono Semibold", 12),foreground="#6cd656",background="#010c25").place(x=10, y=120)
    password_entry = Entry(window, width=20, font=("Terminal"),bg="#6cd656", relief=SUNKEN)
    password_entry.place(x=190, y=120)

    
    def copy_password():
        window.clipboard_clear()
        window.clipboard_append(password_entry.get())
        window.update()  
        messagebox.showinfo("Success", "Password copied to clipboard!")

    ttk.Button(window, text="Copy Password", style="Custom.TButton", command=copy_password).place(x=180, y=160)

    
    close_button = ttk.Button(window, text="Close", command=window.destroy,style="Custom.TButton")
    close_button.place(x=180, y=230)

    
    window.mainloop()
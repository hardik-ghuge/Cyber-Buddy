from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from cybernova.ip_analysis import is_ip_up  

def ip_status_gui(root):
    def check_ip_status():
        website = website_entry.get().strip()

        if not website:
            messagebox.showerror("Error", "Please enter a valid website.")
            return

        try:
            if is_ip_up(website): 
                result_label.config(text="IP STATUS UP",foreground="#6cd656",background="#010c25",font=("Terminal",14))  
            else:
                result_label.config(text="IP STATUS DOWN", fg="red",background="#010c25",font=("Terminal",14))  

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    
    window = Toplevel(root)
    window.title("IP Status Checker")
    window.geometry("500x300")
    window.configure(background="#010c25")
    window.resizable(False,False)
    
    btnstyle = ttk.Style()
    btnstyle.configure(
        "Custom.TButton", 
        padding=(20, 10),
        font=("Terminal",14,'bold'),
        borderwidth = '5'
    )
    btnstyle.map('Custom.TButton', foreground = [('active', '!disabled', 'green')],
                     background = [('active', 'black')])

    
    Label(window, text="Enter Website/IP:", font=("Cascadia Mono Semibold", 12),foreground="#6cd656",background="#010c25").place(x=10, y=20)
    website_entry = Entry(window, width=20, font=("Terminal"),bg="#6cd656", relief=SUNKEN)
    website_entry.place(x=170, y=20)

    
    ttk.Button(window, text="Check IP Status", style="Custom.TButton", command=check_ip_status).place(x=180, y=60)

    
    result_label = Label(window, text="", font=("Terminal", 14), width=30,foreground="#6cd656",background="#010c25")
    result_label.place(x=130, y=160)

    
    close_button = ttk.Button(window, text="Close", command=window.destroy, style="Custom.TButton")
    close_button.place(x=210, y=200)

    window.mainloop()

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from cybernova.ip_analysis import os_fingerprinting 

def os_fingerprinting_gui(root):
    def get_os_fingerprinting():
        website = website_entry.get().strip()

        if not website:
            messagebox.showerror("Error", "Please enter a valid website.")
            return

        try:
            result = os_fingerprinting(website)
            output_label.config(text=result, font=("Terminal", 18, "bold"),foreground="#6cd656",background="#010c25")  # Display result in blue and large font

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    window = Toplevel(root)
    window.title("OS Fingerprinting")
    window.geometry("600x400")
    window.configure(background="#010c25")
    root.resizable(False,False)
    
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

    Label(window, text="Enter Website/IP:", font=("Cascadia Mono Semibold", 12),foreground="#6cd656",background="#010c25").place(x=10, y=20)
    website_entry = Entry(window, width=25, font=("Terminal"),bg="#6cd656", relief=SUNKEN)
    website_entry.place(x=170, y=20)

    ttk.Button(window, text="Get OS Fingerprinting", style="Custom.TButton", command=get_os_fingerprinting).place(x=180, y=60)

    output_label = Label(window, text="", font=("Terminal", 14), width=30, height=6,foreground="#6cd656",background="#010c25")
    output_label.place(x=30, y=120)

    close_button = ttk.Button(window, text="Close", command=window.destroy, style="Custom.TButton")
    close_button.place(x=250, y=300)

    window.mainloop()


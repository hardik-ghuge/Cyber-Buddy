import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from cybernova import get_domain_ip

def get_ip_gui(root):
    def get_ip():
        domain = domain_entry.get()
        if not domain:
            messagebox.showerror("Error", "Please enter a domain.")
            return
        
        try:
            ip_address = get_domain_ip(domain)
            output_text.config(state=NORMAL)
            output_text.delete(1.0, tk.END) 
            output_text.insert(tk.END, ip_address)  
        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch IP: {e}")
    
    def copy_to_clipboard():
        try:
            output = output_text.get(1.0, tk.END).strip() 
            window.clipboard_clear() 
            window.clipboard_append(output)  
            window.update()  
            messagebox.showinfo("Success", "Copied to clipboard!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to copy to clipboard: {e}")
    
    # Main window setup
    window = Toplevel(root)
    window.title("Domain to IP Finder")
    window.geometry("400x300")
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

    # Domain Input
    domain_label = tk.Label(window, text="Enter Domain:",font=("Cascadia Mono Semibold", 14),foreground="#6cd656",background="#010c25")
    domain_label.pack(pady=5)
    domain_entry = tk.Entry(window, width=30,font=("Terminal"),bg="#6cd656", relief=SUNKEN)
    domain_entry.pack(pady=5)

    # Output Text Box to show the IP
    output_text = tk.Text(window,width=30,height=1,font=("Terminal"),bg="#6cd656", relief=SUNKEN,state=DISABLED)
    output_text.pack(pady=10)

    # Button to get IP
    get_ip_button = ttk.Button(window, text="Get IP", command=get_ip,style="Custom.TButton")
    get_ip_button.pack(pady=5)

    # Button to copy the IP to clipboard
    copy_button = ttk.Button(window, text="Copy to Clipboard", command=copy_to_clipboard,style="Custom.TButton")
    copy_button.pack(pady=5)

    # Start the GUI
    window.mainloop()

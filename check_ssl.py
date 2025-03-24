from ssl_checker import SSLChecker
from tkinter import *
from tkinter import ttk, messagebox

def ssl_checker_gui(root):
    def check_ssl_certificate():
        host = host_entry.get().strip()

        if not host:
            messagebox.showerror("Error", "Please enter a valid host.")
            return

        try:
            
            ssl_checker = SSLChecker()
            args = {'hosts': [host]}
            result = ssl_checker.show_result(ssl_checker.get_args(json_args=args))

            
            result_text.config(state=NORMAL)
            result_text.delete(1.0, END)
            if "failed" in result:
                result_text.insert(INSERT, "SSL Certificate Invalid\n\n")
            else:
                result_text.insert(INSERT, "SSL Certificate Valid\n\n")

            
            for value in result.split(','):
                result_text.insert(INSERT, value.strip() + "\n")
            result_text.config(state=DISABLED)

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    def copy_to_clipboard():
        output = result_text.get(1.0, END).strip()
        if output:
            window.clipboard_clear()
            window.clipboard_append(output)
            window.update()
            messagebox.showinfo("Success", "SSL Certificate Info copied to clipboard!")
        else:
            messagebox.showwarning("Warning", "No SSL Certificate Info to copy.")

    
    window = Toplevel(root)
    window.title("SSL Checker")
    window.geometry("700x500")
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

    
    Label(window, text="Enter Host:", font=("Cascadia Mono Semibold", 14),foreground="#6cd656",background="#010c25").place(x=10, y=20)
    host_entry = Entry(window, width=35, font=("Terminal"),bg="#6cd656", relief=SUNKEN)
    host_entry.place(x=135, y=25)

    ttk.Button(window, text="Check SSL",style="Custom.TButton",command=check_ssl_certificate).place(x=310, y=60)
    
    
    Label(window, text="SSL Check Results:", font=("Cascadia Mono Semibold", 12),foreground="#6cd656",background="#010c25").place(x=20, y=100)
    result_text = Text(window, width=55, height=17, wrap=WORD, state=DISABLED,bg="#6cd656", relief=SUNKEN,font=("Terminal"))
    result_text.place(x=20, y=140)

    copy_button = ttk.Button(window, text="Copy to Clipboard", command=copy_to_clipboard, style="Custom.TButton")
    copy_button.place(x=110, y=440)

    close_button = ttk.Button(window, text="Close", command=window.destroy,style="Custom.TButton")
    close_button.place(x=390, y=440)

    window.mainloop()


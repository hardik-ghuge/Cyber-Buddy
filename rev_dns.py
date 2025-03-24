from tkinter import *
from tkinter import ttk, messagebox
import threading
from cybernova.dns_analysis import reverse_dns_lookup  # Ensure this function is implemented correctly

def reverse_dns_gui(root):
    def get_reverse_dns():
        ip_address = ip_entry.get().strip()

        if not ip_address:
            messagebox.showerror("Error", "Please enter a valid IP address.")
            return

        def background_task():
            try:
                window.after(0, lambda: loading_label.place(x=180, y=100))  # Show loading indicator
                
                result = reverse_dns_lookup(ip_address)  # Perform Reverse DNS Lookup

                formatted_result = result if result else "No reverse DNS found."

                window.after(0, update_output_text, formatted_result)

                window.after(0, lambda: loading_label.place_forget())  # Hide loading indicator

            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")

        threading.Thread(target=background_task, daemon=True).start()

    def update_output_text(result):
        output_text.config(state=NORMAL)
        output_text.delete(1.0, END)
        output_text.insert(INSERT, result)
        output_text.config(state=DISABLED)

    def copy_to_clipboard():
        output = output_text.get(1.0, END).strip()
        if output:
            window.clipboard_clear()
            window.clipboard_append(output)
            window.update()
            messagebox.showinfo("Success", "Reverse DNS Info copied to clipboard!")
        else:
            messagebox.showwarning("Warning", "No Reverse DNS Info to copy.")

    # GUI Setup
    window = Toplevel(root)
    window.title("Reverse DNS Lookup")
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

    Label(window, text="Enter IP Address:", font=("Cascadia Mono Semibold", 12),foreground="#6cd656",background="#010c25").place(x=10, y=20)
    ip_entry = Entry(window, width=30, font=("Terminal"),bg="#6cd656", relief=SUNKEN)
    ip_entry.place(x=170, y=20)

    fetch_button = ttk.Button(window, text="Fetch Reverse DNS", command=get_reverse_dns,style="Custom.TButton")
    fetch_button.place(x=230, y=60)

    Label(window, text="Reverse DNS Results:", font=("Cascadia Mono Semibold", 12),foreground="#6cd656",background="#010c25").place(x=20, y=100)
    output_text = Text(window, width=47, height=12, wrap=WORD, state=DISABLED,bg="#6cd656", relief=SUNKEN,font=("Terminal"))
    output_text.place(x=20, y=130)

    copy_button = ttk.Button(window, text="Copy to Clipboard", command=copy_to_clipboard, style="Custom.TButton")
    copy_button.place(x=110, y=350)

    close_button = ttk.Button(window, text="Close", command=window.destroy, style="Custom.TButton")
    close_button.place(x=390, y=350)

    loading_label = Label(window, text="Fetching Reverse DNS Info...", font=("Terminal", 12),foreground="#6cd656",background="#010c25")
    loading_label.place_forget()  # Initially hidden

    window.mainloop()
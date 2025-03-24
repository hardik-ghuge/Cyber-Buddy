from tkinter import *
from tkinter import ttk, messagebox
import threading
from cybernova.dns_analysis import fetch_dns_info  # Ensure this function is implemented correctly

def dns_info_gui(root):
    def get_dns_info():
        domain = domain_entry.get().strip()

        if not domain:
            messagebox.showerror("Error", "Please enter a valid domain.")
            return

        def background_task():
            try:
                window.after(0, lambda: loading_label.place(x=180, y=100))  # Show loading indicator
                
                result = fetch_dns_info(domain)  # Fetch DNS information
                
                formatted_result = "\n".join(result) if result else "No DNS info available."

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
            messagebox.showinfo("Success", "DNS Info copied to clipboard!")
        else:
            messagebox.showwarning("Warning", "No DNS Info to copy.")

    # GUI Setup
    window = Toplevel(root)
    window.title("Fetch DNS Info")
    window.geometry("600x400")
    window.configure(background="#010c25")
    window.resizable(False,False)

    # Styling for the buttons
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

    Label(window, text="Enter Domain:", font=("Cascadia Mono Semibold", 12),foreground="#6cd656",background="#010c25").place(x=20, y=20)
    domain_entry = Entry(window, width=30, font=("Terminal"),bg="#6cd656", relief=SUNKEN)
    domain_entry.place(x=150, y=20)

    fetch_button = ttk.Button(window, text="Fetch DNS Info", command=get_dns_info, style="Custom.TButton")
    fetch_button.place(x=180, y=60)

    Label(window, text="DNS Info Results:", font=("Cascadia Mono Semibold", 12),foreground="#6cd656",background="#010c25").place(x=20, y=100)
    output_text = Text(window, width=47, height=12, wrap=WORD, state=DISABLED,bg="#6cd656", relief=SUNKEN,font=("Terminal"))
    output_text.place(x=20, y=130)

    copy_button = ttk.Button(window, text="Copy to Clipboard", command=copy_to_clipboard, style="Custom.TButton")
    copy_button.place(x=120, y=350)

    close_button = ttk.Button(window, text="Close", command=window.destroy, style="Custom.TButton")
    close_button.place(x=390, y=350)

    loading_label = Label(window, text="Fetching DNS Info...", font=("Terminal", 12),foreground="#6cd656",background="#010c25")
    loading_label.place_forget()  # Initially hidden

    window.mainloop()
from CyberSecurityTools import SubdomainEnumerator
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import threading
import re
import webbrowser

def is_valid_subdomain(subdomain):
    """ Validate a subdomain based on standard rules. """
    pattern = re.compile(r"^(?!-)[A-Za-z0-9-]{1,63}(?<!-)$")
    return all(pattern.match(label) for label in subdomain.split("."))

def subdomain_enumerator_gui(root):
    def enumerate_subdomains():
        base_domain = domain_entry.get().strip()
        wordlist_path = wordlist_entry.get().strip()

        if not base_domain or not wordlist_path:
            messagebox.showerror("Error", "Please enter both the Base Domain and Wordlist Path.")
            return

        def background_task():
            try:
                window.after(0, lambda: loading_label.place(x=280, y=400))  # Show loading indicator
                
                subdomain_enum = SubdomainEnumerator(base_domain=base_domain)
                found_subdomains = subdomain_enum.enumerate(wordlist_path=wordlist_path)  # Store found subdomains
                
                with open(wordlist_path, "r") as file:
                    wordlist_lines = file.read().splitlines()

                scanned_subdomains.clear()  # Clear previous results

                for sub in wordlist_lines:
                    subdomain = f"{sub}.{base_domain}"
                    url = f"http://{subdomain}"

                    if any(subdomain in found for found in found_subdomains):
                        result = f"✅ Found: {url}"
                    else:
                        result = f"❌ Failed to connect to: {url}"

                    scanned_subdomains.append(result)

                    # Update output box dynamically
                    window.after(0, update_output_text)

                window.after(0, lambda: loading_label.place_forget())  # Hide loading indicator

            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")

        def update_output_text():
            """ Updates the Output Box with all scanned subdomains """
            output_text.config(state=NORMAL)
            output_text.delete(1.0, END)
            output_text.insert(INSERT, "\n".join(scanned_subdomains))
            output_text.config(state=DISABLED)

        scanned_subdomains = []
        threading.Thread(target=background_task, daemon=True).start()

    def copy_to_clipboard():
        """ Copies the text from the output box to the clipboard """
        window.clipboard_clear()
        window.clipboard_append(output_text.get(1.0, END))
        window.update()  # Required for clipboard to update properly
        messagebox.showinfo("Copied", "Results copied to clipboard!")

    def open_listlink():
        webbrowser.open("https://github.com/rbsec/dnscan/blob/master/subdomains-10000.txt")

    # GUI Window
    window = Toplevel(root)
    window.title("Subdomain Enumerator")
    window.geometry("700x500")
    window.configure(background="#010c25")
    window.resizable(False,False)

    Label(window, text="Enter Details for Subdomain Enumeration", font=("Cascadia Mono Semibold", 14),foreground="#6cd656",background="#010c25").place(x=10, y=10)
    Label(window, text="Base Domain:", font=("Cascadia Mono Semibold", 12),foreground="#6cd656",background="#010c25").place(x=10, y=50)
    domain_entry = Entry(window, width=40,font=("Terminal",12),bg="#6cd656", relief=SUNKEN)
    domain_entry.place(x=150, y=50)
    Label(window, text="Wordlist Path:", font=("Cascadia Mono Semibold", 12),foreground="#6cd656",background="#010c25").place(x=10, y=90)
    wordlist_entry = Entry(window, width=40,font=("Terminal",12),bg="#6cd656", relief=SUNKEN)
    wordlist_entry.place(x=150, y=90)

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

    enumerate_button = ttk.Button(window, text="Enumerate Subdomains", command=enumerate_subdomains, style="Custom.TButton")
    enumerate_button.place(x=150, y=115)
    Label(window,text="Get Subdomains List From",font=("Cascadia Mono Semibold",10),foreground="#6cd656",background="#010c25").place(x=420,y=130)
    herebutton = ttk.Button(window,text="here",command=open_listlink,style='Link.TButton')
    herebutton.place(x=619,y=128)

    # Single Output Box for Both Found & Failed Subdomains
    Label(window, text="Enumeration Results:", font=("Cascadia Mono Semibold", 12),foreground="#6cd656",background="#010c25").place(x=10, y=170)
    output_text = Text(window, width=55, height=12, wrap=WORD, state=DISABLED,bg="#6cd656", relief=SUNKEN,font=("Terminal"))
    output_text.place(x=10, y=200)

    # Copy Button
    copy_button = ttk.Button(window, text="Copy to Clipboard", command=copy_to_clipboard, style="Custom.TButton")
    copy_button.place(x=115, y=450)

    # Close Button
    close_button = ttk.Button(window, text="Close", command=window.destroy, style="Custom.TButton")
    close_button.place(x=380,y=450)

    # Loading Indicator
    loading_label = Label(window, text="Enumerating Subdomains...", font=("Terminal", 12),foreground="#6cd656",background="#010c25")
    loading_label.place_forget()  # Initially hidden
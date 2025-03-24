from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from cybernova.ip_analysis import whois_lookup  # Assuming this function is correct

def whois_lookup_gui(root):
    def get_whois_lookup():
        website = website_entry.get().strip()

        if not website:
            messagebox.showerror("Error", "Please enter a valid website.")
            return

        try:
            # Perform WHOIS lookup
            result = whois_lookup(website)
            output_text.config(state=NORMAL)  # Enable text field to insert result
            output_text.delete(1.0, END)  # Clear previous result
            output_text.insert(INSERT, result)  # Insert the result in the text box
            output_text.config(state=DISABLED)  # Disable the text field to prevent editing

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def copy_to_clipboard():
        # Copy the content of the text widget to the clipboard
        try:
            output = output_text.get(1.0, END).strip()  # Get the text from the text widget
            window.clipboard_clear()  # Clear the current clipboard content
            window.clipboard_append(output)  # Append the content to the clipboard
            window.update()  # Update the window to register the clipboard change
            messagebox.showinfo("Success", "Copied to clipboard!")  # Show confirmation
        except Exception as e:
            messagebox.showerror("Error", f"Failed to copy to clipboard: {e}")

    # Creating the main window
    window = Toplevel(root)
    window.title("WHOIS Lookup")
    window.geometry("600x400")
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

    # Creating GUI components
    Label(window, text="Enter Website/IP:", font=("Cascadia Mono Semibold", 12),foreground="#6cd656",background="#010c25").place(x=10, y=20)
    website_entry = Entry(window, width=27,font=("Terminal"),bg="#6cd656", relief=SUNKEN)
    website_entry.place(x=170, y=22)

    # Check WHOIS lookup button
    ttk.Button(window, text="Get WHOIS Lookup", style="Custom.TButton", command=get_whois_lookup).place(x=180, y=60)

    # Text box to display the WHOIS lookup result
    output_text = Text(window, font=("Terminal",12), width=45, height=13, wrap=WORD,bg="#6cd656", relief=SUNKEN)
    output_text.place(x=30, y=120)
    output_text.config(state=DISABLED)  # Make the text box read-only initially

    # Copy to clipboard button
    copy_button = ttk.Button(window, text="Copy to Clipboard", style="Custom.TButton", command=copy_to_clipboard)
    copy_button.place(x=120, y=350)

    # Close button
    close_button = ttk.Button(window, text="Close", command=window.destroy, style="Custom.TButton")
    close_button.place(x=380, y=350)

    window.mainloop()


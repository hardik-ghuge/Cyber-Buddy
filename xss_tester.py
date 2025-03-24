from CyberSecurityTools import XSSTester
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def xss_tester_gui(root):
    def test_xss():
        # Retrieve the URL and parameter entered by the user
        url = url_entry.get().strip()
        param = param_entry.get().strip()

        if not url or not param:
            messagebox.showerror("Error", "Please enter both the URL and parameter.")
            return

        try:
            xss_tester = XSSTester()
            vulnerable = xss_tester.test(url=url, param=param)

            # Display the result at the bottom
            result_label.config(text="Vulnerability Found" if vulnerable else "No Vulnerability Found")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    # Create the Toplevel window
    window = Toplevel(root)
    window.title("XSS Tester")
    window.geometry("500x300")
    window.configure(background="#010c25")
    window.resizable(False, False)

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


    # Heading Label
    Label(window, text="Enter Details to Test for XSS Vulnerability", font=("Cascadia Mono Semibold", 12),foreground="#6cd656",background="#010c25").place(x=10, y=10)

    # URL Entry Label and Entry Widget
    Label(window, text="Enter Target URL:", font=("Cascadia Mono Semibold", 10),foreground="#6cd656",background="#010c25").place(x=10, y=50)
    url_entry = Entry(window, width=28,bg="#6cd656", relief=SUNKEN,font=("Terminal"))
    url_entry.place(x=150, y=50)

    # Parameter Entry Label and Entry Widget
    Label(window, text="Enter Parameters:", font=("Cascadia Mono Semibold", 10),foreground="#6cd656",background="#010c25").place(x=10, y=90)
    param_entry = Entry(window, width=28,bg="#6cd656", relief=SUNKEN,font=("Terminal"))
    param_entry.place(x=150, y=90)

    # Test Button
    test_button = ttk.Button(window, text="Test XSS", command=test_xss, style="Custom.TButton")
    test_button.place(x=200, y=130)

    # Result Label at the Bottom
    result_label = Label(window, text="" ,font=("Terminal",12,'bold'), fg="red",bg="#010c25")
    result_label.place(x=150, y=200)

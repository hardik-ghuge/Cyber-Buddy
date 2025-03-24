from CyberSecurityTools import CSRFTester
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def csrf_tester_gui(root):
    def test_csrf():
        form_url = form_url_entry.get().strip()
        username = username_entry.get().strip()
        password = password_entry.get().strip()

        if not form_url or not username or not password:
            messagebox.showerror("Error", "Please enter all required fields (Form URL, Username, and Password).")
            return

        try:
            form_data = {"username": username, "password": password}
            csrf_tester = CSRFTester()
            vulnerable = csrf_tester.test(form_url=form_url, form_data=form_data)
            result_label.config(text="Vulnerability Found" if vulnerable else "No Vulnerability Found")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    window = Toplevel(root)
    window.title("CSRF Tester")
    window.geometry("500x350")
    window.configure(background="#010c25")
    window.resizable(False,False)
    

    Label(window, text="Enter Details to Test for CSRF Vulnerability", font=("Cascadia Mono Semibold", 12),foreground="#6cd656",background="#010c25").place(x=10, y=10)
    Label(window, text="Enter Form URL:", font=("Cascadia Mono Semibold",10),foreground="#6cd656",background="#010c25").place(x=10, y=50)
    form_url_entry = Entry(window, width=25,bg="#6cd656", relief=SUNKEN,font=("Terminal"))
    form_url_entry.place(x=140, y=50)
    Label(window, text="Enter Username:", font=("Cascadia Mono Semibold",10),foreground="#6cd656",background="#010c25").place(x=10, y=90)
    username_entry = Entry(window, width=25,bg="#6cd656", relief=SUNKEN,font=("Terminal"))
    username_entry.place(x=140, y=90)
    Label(window, text="Enter Password:", font=("Cascadia Mono Semibold",10),foreground="#6cd656",background="#010c25").place(x=10, y=130)
    password_entry = Entry(window, width=25, show="*",bg="#6cd656", relief=SUNKEN,font=("Terminal"))
    password_entry.place(x=140, y=130)

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

    test_button = ttk.Button(window, text="Test CSRF", command=test_csrf, style="Custom.TButton")
    test_button.place(x=200, y=170)

    result_label = Label(window, text="", font=("Terminal",12,'bold'), fg="red",bg="#010c25")
    result_label.place(x=150, y=250)

if __name__ == "__main__":
    root = Tk()
    root.withdraw()
    csrf_tester_gui(root)
    root.mainloop()
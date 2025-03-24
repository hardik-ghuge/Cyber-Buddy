from CyberSecurityTools import SQLInjectionTester
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def sql_tester_gui(root):
    def test_sql_injection():
        
        url = url_entry.get().strip()
        param = param_entry.get().strip()

        if not url or not param:
            messagebox.showerror("Error", "Please enter both the URL and parameter.")
            return

        try:
            sql_tester = SQLInjectionTester()
            vulnerable = sql_tester.test(url=url, param=param)

            
            result_label.config(text="Vulnerability Found" if vulnerable else "No Vulnerability Found")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    
    window = Toplevel(root)
    window.title("SQL Injection Tester")
    window.geometry("500x300")
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

    
    Label(window, text="Enter Details to Test for SQL Injection Vulnerability", font=("Cascadia Mono Semibold", 12),foreground="#6cd656",background="#010c25").place(x=10, y=10)

    
    Label(window, text="Enter Target URL:", font=("Cascadia Mono Semibold", 10),foreground="#6cd656",background="#010c25").place(x=10, y=50)
    url_entry = Entry(window, width=25,bg="#6cd656", relief=SUNKEN,font=("Terminal"))
    url_entry.place(x=160, y=50)

    
    Label(window, text="Enter Parameter Name:", font=("Cascadia Mono Semibold",10),foreground="#6cd656",background="#010c25").place(x=10, y=90)
    param_entry = Entry(window, width=25,bg="#6cd656", relief=SUNKEN,font=("Terminal"))
    param_entry.place(x=190, y=90)

    test_button = ttk.Button(window, text="Test SQL Injection", command=test_sql_injection, style="Custom.TButton")
    test_button.place(x=180, y=130)

    
    result_label = Label(window, text="", font=("Terminal",12,'bold'),fg="red",bg="#010c25")
    result_label.place(x=150, y=200)

from CyberSecurityTools import BrokenLinkChecker
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def broken_link_gui(root):
    def check_link():
        root.focus_force()
        
        entered_link = link_entry.get().strip()

        if not entered_link:
            messagebox.showerror("Error", "Please enter a valid link.")
            return

        try:
            
            broken_link_checker = BrokenLinkChecker()
            broken_links = broken_link_checker.check(url=entered_link)

            
            if broken_links:
                result_message = "\n".join(broken_links)
                result_text.delete(1.0, END)  
                result_text.insert(INSERT, result_message)  
            else:
                result_text.delete(1.0, END)
                result_text.insert(INSERT, "No broken links found!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    
    root = Toplevel(root)
    root.title("Broken Link Checker")
    root.geometry("500x400")
    root.configure(background="#010c25")
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

    Label(root, text="Enter A Link To Check For Broken Links", font=("Cascadia Mono Semibold",16),foreground="#6cd656",background="#010c25").place(x=10, y=10)

    
    link_entry = Entry(root, width=40,font=("Terminal"),bg="#6cd656", relief=SUNKEN)
    link_entry.place(x=10, y=50)

    
    check_button = ttk.Button(root, text="Check", command=check_link,style="Custom.TButton")
    check_button.place(x=10, y=83)

    
    Label(root, text="Broken Links Found", font=("Cascadia Mono Semibold",14),foreground="#6cd656",background="#010c25").place(x=10, y=150)

    
    result_text = Text(root, width=37, height=10, wrap=WORD,bg="#6cd656", relief=SUNKEN,font=("Terminal"),state=DISABLED)
    result_text.place(x=10, y=190)

    
    root.mainloop()
    

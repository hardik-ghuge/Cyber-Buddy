from CyberSecurityTools import NetworkVulnerabilityScanner
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def network_scanner_gui(root):
    def scan_network():
        
        target = target_entry.get().strip()

        if not target:
            messagebox.showerror("Error", "Please enter a valid target (IP or hostname).")
            return

        try:
            
            scanner = NetworkVulnerabilityScanner(target=target)
            open_ports = scanner.scan()

            
            result_text.config(state=NORMAL) 
            result_text.delete(1.0, END)  
            if open_ports:
                result_message = f"Open Ports:\n" + "\n".join(map(str, open_ports))
                result_text.insert(INSERT, result_message)
            else:
                result_text.insert(INSERT, "No open ports found.")
            result_text.config(state=DISABLED)  
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    
    window = Toplevel(root)
    window.title("Network Scanner")
    window.geometry("500x400")
    window.configure(background="#010c25")
    window.resizable(False,False)
    
    Label(window, text="Enter An IP To See Network Vulnerabilities",font=("Cascadia Mono Semibold",14),foreground="#6cd656",background="#010c25").pack(pady=10)

    
    Label(window, text="Enter Target IP :",font=("Cascadia Mono Semibold",12),foreground="#6cd656",background="#010c25").place(x=10,y=40)
    target_entry = Entry(window, width=27,bg="#6cd656", relief=SUNKEN,font=("Terminal",12))
    target_entry.place(x=160,y=45)

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

    
    scan_button = ttk.Button(window, text="Scan", command=scan_network, style="Custom.TButton")
    scan_button.place(x=250,y=73)

    
    Label(window, text="Scan Results:", font=("Cascadia Mono Semibold",12),foreground="#6cd656",background="#010c25").place(x=10,y=110)

    
    result_text = Text(window, width=39, height=12, wrap=WORD, state=DISABLED,bg="#6cd656", relief=SUNKEN,font=("Terminal",12))
    result_text.place(x=10,y=135)

    
    close_button = ttk.Button(window, text="Close", command=window.destroy, style="Custom.TButton")
    close_button.place(x=200,y=340)

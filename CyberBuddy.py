#IMPORTS
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk 
#BASIC TOOLS IMPORTS
from check_ssl import ssl_checker_gui
from pwd_generator import password_generator_gui
from check_ip_status import ip_status_gui
from fingerprint_os import os_fingerprinting_gui
from whoislookup import whois_lookup_gui
from pwd_manager import pwd_manager_gui
from get_ip import get_ip_gui
from dns_info import dns_info_gui
from rev_dns import reverse_dns_gui
#BASIC VULNERABILITY SCANNER IMPORTS
from broken_link import broken_link_gui
from nwscanner import network_scanner_gui
from sql_inject_tester import sql_tester_gui
from subdomain_enum import subdomain_enumerator_gui
from csrf_tester import csrf_tester_gui
from xss_tester import xss_tester_gui
#IMPORTS END

#MAIN CODE
#DEFINING THE ROOT
root =Tk()
root.title("Cyber-Buddy - Cyber Security Toolkit")
root.state('zoomed')
#root.attributes('-fullscreen', True)
#root.resizable(False,False)
#root.configure(bg="#010C25")

style = ttk.Style()
style.configure("TFrame", background="#010c25")
#DEFFINING THE TABS 
notebook = ttk.Notebook(root)

ww = ttk.Frame(notebook,style="TFrame")
bt = ttk.Frame(notebook,style="TFrame")
bvs = ttk.Frame(notebook,style="TFrame")
fvs = ttk.Frame(notebook,style="TFrame")

notebook.add(ww,text="Welcome Window")
notebook.add(bt,text="Basic Tools")
notebook.add(bvs,text="Basic Vulnerabiity Scanner")

notebook.pack(expand=True,fill="both")

#DEFINING THE STYLES
btnstyle = ttk.Style()
btnstyle.configure(
        "Custom.TButton", 
        padding=(20, 10),
        font=("Terminal",14,'bold'),
        borderwidth = '5'
    )
btnstyle.map('Custom.TButton', foreground = [('active', '!disabled', 'green')],
                     background = [('active', 'black')])

Label(ww,text="Welcome To Cyber Buddy",font=("Terminal",24),foreground="#6cd656",background="#010c25").place(x=550,y=10)
wimg = PhotoImage(file="D://TY-SEM 6 Project/Final/assets/logo.png")
logo = Label(ww,image=wimg)
logo.place(x=632,y=50)
Label(ww,text="Please Follow These Rules Of Usage",font=("Terminal",22),foreground="#6cd656",background="#010c25").place(x=500,y=270)
Label(ww, text="""
➡️ Educational Use Only: For learning about security and improving systems.\n
➡️ Permission Required: Always get permission before testing or scanning.\n
➡️ Respect Privacy: Do not access or exploit personal data without consent.\n
➡️ Avoid Unethical Practices: Do not attack,disrupt or harm other's systems.\n
➡️ Comply with Laws and Regulations: Follow all relevant cybersecurity laws.\n
➡️ Responsible Disclosure: Report vulnerabilities securely and responsibly.\n
➡️ Accountability: The user assumes full responsibility for their actions.\n
➡️ Ethics: Misuse of this tool for illegal purposes is strictly prohibited.\n
➡️ No Unauthorized Penetration Testing: Do not perform penetration testing on \n\tsystems you do not own or have explicit permission to test.
""", font=("Terminal",18),foreground="#6cd656",background="#010c25").place(x=10, y=300)


#BASIC TOOLS PAGE
Label(bt,text="Basic Tools",font=("Terminal",24,'bold'),foreground="#6cd656",background="#010c25").place(x=660,y=10)
##Pwd Generator
pwdg = PhotoImage(file="D://TY-SEM 6 Project/Final/assets/pwdgen.png")
pwdgen = Label(bt,image=pwdg)
pwdgen.place(x=60,y=79)
ttk.Button(bt,text="Password Generator",command=lambda:password_generator_gui(root),style="Custom.TButton").place(x=20,y=240)

##Pwd Man
ttk.Button(bt,text="Password Manager",style="Custom.TButton",command=lambda:pwd_manager_gui(root)).place(x=350,y=240)
pwdm = PhotoImage(file="D://TY-SEM 6 Project/Final/assets/pwdman.png")
pwdman = Label(bt,image=pwdm)
pwdman.place(x=385,y=79)

##Check Ip UP
ttk.Button(bt,text="Check if IP up",command=lambda:ip_status_gui(root),style="Custom.TButton").place(x=665,y=240)
ips = PhotoImage(file="D://TY-SEM 6 Project/Final/assets/ipstatus.png")
ipsta = Label(bt,image=ips)
ipsta.place(x=693,y=79)

##WHOIS
ttk.Button(bt,text="Perform WHOIS Lookup",command=lambda:whois_lookup_gui(root),style="Custom.TButton").place(x=950,y=240)
who = PhotoImage(file="D://TY-SEM 6 Project/Final/assets/whoislook.png")
whois = Label(bt,image=who)
whois.place(x=1010,y=79)

##osfingerprinting
ttk.Button(bt,text="Do OS Fingerprinting",command=lambda:os_fingerprinting_gui(root),style="Custom.TButton").place(x=1255,y=240)
osf = PhotoImage(file="D://TY-SEM 6 Project/Final/assets/osfingerprint.png")
osfg = Label(bt,image=osf)
osfg.place(x=1309,y=79)

##Get IP
geti = PhotoImage(file="D://TY-SEM 6 Project/Final/assets/findip.png")
getip = Label(bt,image=geti)
getip.place(x=60,y=360)
ttk.Button(bt,text="Get IP Address",style="Custom.TButton",command=lambda:get_ip_gui(root)).place(x=35,y=521)

##fetdns
fetd = PhotoImage(file="D://TY-SEM 6 Project/Final/assets/fetchdns.png")
fetdn = Label(bt,image=fetd)
fetdn.place(x=385,y=360)
ttk.Button(bt,text="Fetch DNS Information",style="Custom.TButton",command=lambda:dns_info_gui(root)).place(x=325,y=521)

##reverse Dns
revd = PhotoImage(file="D://TY-SEM 6 Project/Final/assets/revdns.png")
revdns = Label(bt,image=revd)
revdns.place(x=693,y=360)
ttk.Button(bt,text="Reverse DNS Lookup",style="Custom.TButton",command=lambda:reverse_dns_gui(root)).place(x=655,y=521)

##Check SSL
checs = PhotoImage(file="D://TY-SEM 6 Project/Final/assets/checkssl.png")
checkss = Label(bt,image=checs)
checkss.place(x=1010,y=360)
ttk.Button(bt,text="Check SSL Certificate",command=lambda:ssl_checker_gui(root),style="Custom.TButton").place(x=955,y=521)


#BASIC VULNERABILITY SCANNER PAGE
Label(bvs,text="Basic Vulnerability Scanner",font=("Terminal",24,'bold'),foreground="#6cd656",background="#010c25").place(x=470,y=10)
##BrokenLink
bl = PhotoImage(file = "D://TY-SEM 6 Project/Final/assets/brokenlink.png")
blink = Label(bvs,image=bl)
blink.place(x=192,y=85)
ttk.Button(bvs,text="Broken Link Checker",command=lambda:broken_link_gui(root),style="Custom.TButton").place(x=160,y=293)

###Networkvuln
nwvuln = PhotoImage(file="D://TY-SEM 6 Project/Final/assets/networkvulnsc.png")
nwvulsc = Label(bvs,image=nwvuln)
nwvulsc.place(x=670,y=85)
ttk.Button(bvs,text="Network Vuln Scanner",command=lambda:network_scanner_gui(root),style="Custom.TButton").place(x=638,y=293)

##CSRF TESTING
csrft = PhotoImage(file="D://TY-SEM 6 Project/Final/assets/csrf.png")
csrftp = Label(bvs,image=csrft)
csrftp.place(x=1136,y=85)
ttk.Button(bvs,text="CSRF Testing",style="Custom.TButton",command=lambda:csrf_tester_gui(root)).place(x=1150,y=293)

##Subdomain Enum
sube = PhotoImage(file="D://TY-SEM 6 Project/Final/assets/subdomainenum.png")
subenu = Label(bvs,image=sube)
subenu.place(x=198,y=389)
ttk.Button(bvs,text="Sub Domain Enumeration",style="Custom.TButton",command=lambda:subdomain_enumerator_gui(root)).place(x=162,y=600)


##SQLi Tester
sqli = PhotoImage(file="D://TY-SEM 6 Project/Final/assets/sqli.png")
sqlii = Label(bvs,image=sqli)
sqlii.place(x=670,y=389)
ttk.Button(bvs,text="SQL Injection Tester",style="Custom.TButton",command=lambda:sql_tester_gui(root)).place(x=638,y=600)

##XSS Tester
xs = PhotoImage(file="D://TY-SEM 6 Project/Final/assets/xss.png")
xss = Label(bvs,image=xs)
xss.place(x=1136,y=389)
ttk.Button(bvs,text="XSS Testing",style="Custom.TButton",command=lambda:xss_tester_gui(root)).place(x=1160,y=600)

##Mainloop Declaration
root.mainloop()
# Importing the required modules
from tkinter import * #Module for basic GUI elements
from tkinter import ttk #Module for GUI widgets
import platform #For identifying the OS
import sv_ttk #For custom themes on ttk
import sys #System-level functions
import pywinstyles # Customization for Windows
import darkdetect #Detects light or dark mode on system

# Path to the hosts file on operating system (change accordingly for Windows/Linux/Mac)
h_path = ""

# Redirect IP to block websites
redirect = "127.0.0.1"

# Array to store websites to block
blocked_websites = []

# Function to add entered website to the list
def web_add():
    website_text = Websites.get("1.0", END).strip()
    for site in website_text.split(","):
        blocked_websites.append(site.strip())
    print(blocked_websites) # Print the list for debugging

# Function to block websites by adding entries to the hosts file
def block():
    #reads the host files contents once.
    with open(h_path, "r+") as host_file:
        path_r = host_file.readlines()
    current_blocked_websites = [line.split()[1] for line in path_r if line.startswith(redirect)]
    websites_to_block = [website for website in blocked_websites if website not in current_blocked_websites]

    if websites_to_block:
        with open(h_path, "a") as host_file:  # Open in append mode to add new entries
            for website in websites_to_block:
                host_file.write("\n" + redirect + " " + website + "\n")
                print("Blocked:",website)  # Print for debugging
        Label(root, text="Blocked", font="arial 12 bold").place(x=210, y=220)
    else:
        Label(root, text="All websites already blocked", font="arial 12 bold").place(x=150, y=220)
    
#Function to unblock the websites by removing them from host file
def unblock():
    with open(h_path, "r+") as host_file: 
        path_r = host_file.readlines() #Reads all the lines
    lines_to_keep = [line for line in path_r if not any(website in line for website in blocked_websites)]

    with open(h_path, "w") as host_file:
        host_file.writelines(lines_to_keep)

    Label(root, text="Unblocked", font="arial 12 bold").place(x=210, y=220)

# Function to set the OS path based on dropdown selection
def set_os_path():
    global h_path
    selected_os = os_dropdown.get()  # <-- getting value directly from the dropdown
    if selected_os == "Windows":
        h_path = r"C:\Windows\System32\drivers\etc\hosts"
    elif selected_os == "Mac" or selected_os == "Linux":
        h_path = "/etc/hosts"
    else:
        h_path = ""

#GUI set up
root = Tk() #Creates main app window
root.geometry('500x400') #Size of window in pixels
root.resizable(0,0) #Disables resizing
root.title("BlockTock") #Title of app

#Customization of title
Label(root, text = 'BlockTock' , font = ("arial", 25, "bold")).pack(anchor= "n")

# Label for OS selection
Label(root, text='Select Your OS:', font=("arial", 12, "bold")).place(x=70, y=130)
#Label(frame, text='Select Your OS:', font=("arial", 12, "bold")).pack(anchor="center", pady=5)

# OS dropdown menu with values
os_dropdown = ttk.Combobox(root, values=["Windows", "Mac", "Linux"], state="readonly", width=10)
os_dropdown.place(x=175, y=125)
os_dropdown.current(0)  # Set default to Windows

# Button to confirm OS selection
os_button = Button(root, text='CONFIRM OS', font='arial 12 bold', command=set_os_path, width=10, bg='black', fg='white')
os_button.place(x=340, y=125)
#os_button = Button(frame, text='CONFIRM OS', font='arial 10 bold', command=set_os_path, width=10, bg='light blue')
#os_button.pack(pady=5)

# Label prompting user input
Label(root, text='Enter Website:', font = ("arial", 12, "bold")).pack(anchor= "center")

# Text area where user can enter one or more websites, comma-separated
Websites = Text(root, font='arial 12', height=2, width=40, wrap=WORD, padx=5, pady=5)
Websites.pack(anchor= "center")

# add_button to call web_add()
add_button = Button(root, text='ADD WEBSITE', font='arial 12 bold', command=web_add, width=12, bg='DarkOrchid1', activebackground = 'sky blue', fg='white')
add_button.place(x=185, y=125)

# Button to trigger the Blocker function
block_button = Button(root, text='BLOCK', font='arial 12 bold', command=block, width=9, bg='deep pink', activebackground='sky blue', fg = 'white')
block_button.pack(side=LEFT)
block_button.place(x= 140, y=170)

# Button to unblock websites
unblock_button = ttk.Button(root, text="Unblock", command=unblock)
unblock_button = Button(root, text='UNBLOCK', font='arial 12 bold', command=unblock, width=9, bg='deep pink', activebackground='sky blue', fg = 'white')
unblock_button.place(x=270, y=170)

# Automatically apply light/dark theme based on system settings
sv_ttk.set_theme(darkdetect.theme())

# Optional Windows customization for modern header styling (currently commented out)
if platform.system() == "Windows":
    if sys.getwindowsversion().major == 10 and sys.getwindowsversion().build >= 22000:
         if sv_ttk.get_theme() == "dark":
             pywinstyles.change_header_color(root, "#000000")

# Run the GUI event loop
root.mainloop()

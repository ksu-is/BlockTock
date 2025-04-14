# Importing the required modules
from tkinter import * #Module for basic GUI elements
from tkinter import ttk #Module for GUI widgets
import platform #For identifying the OS
import sv_ttk #For custom themes on ttk
import sys #System-level functions
import pywinstyles # Customization for Windows
import darkdetect #Detects light or dark mode on system

"""
Hosts Paths On Windows, Mac & Linux:

Windows: C:\Windows\System32\drivers\etc\hosts

Mac & Linux: /etc/hosts
"""
# Path to the hosts file on operating system (change accordingly for Windows/Linux/Mac)
h_path = "ENTER HOSTS FILE PATH HERE"

# Redirect IP to block websites
redirect = "127.0.0.1"

# Array to store websites to block
blocked_websites = []

# Function to add entered website to the list
def web_add():

    website_text = Websites.get("1.0", END).strip()
    for site in website_text.split(","):
        blocked_websites.append(site.strip())
                                    
    # blocked_websites.append(website_entry.get()) # Get text from entry box and add to array

    print(blocked_websites) # Print the list for debugging

# Function to block websites by adding entries to the hosts file
def block():
    #reads the host files contents once.
    with open(h_path, "r+") as host_file:
        path_r = host_file.readlines()
    current_blocked_websites = [line.split()[1] for line in path_r if line.startswith(redirect)]
    websites_to_block = [website for website in blocked_websites if website not in current_blocked_websites

    #path = open(h_path, "r+") # Open the hosts file in read/write mode
    #path_r = path.read() # Read its contents (not strictly needed here)

    for website in blocked_websites:

        path.write(redirect + " " + website + "\n") # Add redirect entry for each website

#Function to unblock the websites by removing them from host file
def unblock():
    
    with open(h_path, "r+") as path: 

        path_r = path.readlines() #Reads all the lines

        path.seek(0) #Moves cursor back to the beginning of file

        #Writes back all lines except for blocked websites
        for line in path_r:
        
            if not any(website in line for website in blocked_websites):

                path.write(line)
        
        path.truncate() #Removes leftover files


#GUI set up
root = Tk() #Creates main app window
root.geometry('500x300') #Size of window in pixels
root.resizable(0,0) #Disables resizing
root.title("BlockTock") #Title of app

#Customization of title
Label(root, text = 'BlockTock' , font = 'Oswald 20 bold').pack(side = TOP)

# Label prompting user input
Label(root, text='Enter Website:', font='Oswald 13 bold').place(x=5, y=60)

# Text area where user can enter one or more websites, comma-separated
Websites = Text(
    root,
    font='arial 10',
    height=2,
    width=40,
    wrap=WORD,
    padx=5,
    pady=5
)
Websites.place(x=140, y=60)

# Button to trigger the Blocker function
block_btn = Button(
    root,
    text='BLOCK',
    font='arial 12 bold',
    command=block,
    width=6,
    bg='royal blue1',
    activebackground='sky blue'
)
block_btn.place(x=230, y=150)

# Button to unblock websites
unblock_button = ttk.Button(root, text="Unblock", command=unblock)
unblock_button.pack(side=RIGHT)

# Automatically apply light/dark theme based on system settings
sv_ttk.set_theme(darkdetect.theme())

Optional Windows customization for modern header styling (currently commented out)
if platform.system() == "Windows":
    if sys.getwindowsversion().major == 10 and sys.getwindowsversion().build >= 22000:
         if sv_ttk.get_theme() == "dark":
             pywinstyles.change_header_color(root, "#000000")

# Run the GUI event loop
root.mainloop()

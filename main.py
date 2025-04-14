# Importing the required modules
from tkinter import * #Module for basic GUI elements
from tkinter import ttk #Module for GUI widgets
import platformm #For identifying the OS
import sv_ttk #For cusotm themes on ttk
import sys #System-leel functions
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
website_arr = []

# Function to add entered website to the list
def web_add():

    website_arr.append(website_entry.get()) # Get text from entry box and add to array

    print(website_arr) # Print the list for debugging

# Function to block websites by adding entries to the hosts file
def block():

    path = open(h_path, "r+") # Open the hosts file in read/write mode

    path_r = path.read() # Read its contents (not strictly needed here)

    for website in website_arr:

        path.write(f"{redirect} {website}\n") # Add redirect entry for each website

#Fuction to unblock the websites by removing them from host file
def unblock():
    
    with open(h_path, "r+") as path: 

        path_r = path.readlines() #Reads all the lines

        path.seek(0) #Moves cursor back to the beginning of file

        #Writes back all lines except for blocked websites
        for line in path_r:
        
            if not any(website in line for website in website_arr):

                path.write(line)
        
        path.truncate() #Removes leftover files

from tkinter import *
from tkinter import ttk
import platform
import sv_ttk
import sys
import pywinstyles
import darkdetect

"""
Hosts Paths On Windows, Mac & Linux:

Windows: C:\Windows\System32\drivers\etc\hosts

Mac & Linux: /etc/hosts
"""

h_path = "ENTER HOSTS FILE PATH HERE"

redirect = "127.0.0.1"

website_arr = []

def web_add():

    website_arr.append(website_entry.get())

    print(website_arr)

def block():

    path = open(h_path, "r+")

    path_r = path.read()

    for website in website_arr:

        path.write(f"{redirect} {website}\n")
    
def unblock():
    
    with open(h_path, "r+") as path:

        path_r = path.readlines()

        path.seek(0)

        for line in path_r:
        
            if not any(website in line for website in website_arr):

                path.write(line)
        
        path.truncate()

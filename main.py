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

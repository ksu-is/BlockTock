## BlockTock: A Productivity Enhancement Website Blocker App

## Overview

Are you sick of scrolling and wasting precious time? Then BlockTock is for you! This project uses Python to create a productivity app that allows users to enable/disable access to selected websites. Social media is heavily ingrained in our daily lives today, so many people struggle with time management due to excessive distractions. This is a great solution to help users stay focused on school or work, reduce screen time, and reclaim lost hours. Take back control of your time today!

## Pre-requisites

1. User must have Python 3.x installed on their machine.
2. This Python code currently works on both Windows and Mac Operating Systems and all Linux Distributions.
3. Modules that need to be installed beforehand with -m pip install:
  - sv_ttk 
  - pywinstyles (THIS MODULE IS ONLY REQUIRED FOR WINDOWS)
  - darkdetect 

## How to Use the BlockTock App

1. Launch the app — the BlockTock window will open automatically.
2. Select your Operating System from the dropdown menu and confirm.
3. Enter the website URL you want to block in the text box and click "ADD WEBSITE".
4. Click "Block" to restrict access to the website.
5. To regain access, click "Unblock" at any time.

## Notes

Comment out the following lines if you're not running this app on Windows:

Line 7: 

import pwinstyles

Lines 106 - 109: 

if platform.system() == "Windows":
    if sys.getwindowsversion().major == 10 and sys.getwindowsversion().build >= 22000:
         if sv_ttk.get_theme() == "dark":
             pywinstyles.change_header_color(root, "#000000")

## Acknowledgments and Code References

Portions of this project were developed with assistance from OpenAI's ChatGPT.
Components of this project were adapted from:
[SmashFrenzy16/Website-Blocker](https://github.com/SmashedFrenzy16/Website-Blocker), licensed under [Apache License 2.0]
[Yash-2403/Python-Website-Blocker](https://github.com/Yash-2403/Python-Website-Blocker)
[AzharAnwar9/Python-Website-Blocker](https://github.com/AzharAnwar9/Python-Website-Blocker/tree/main)

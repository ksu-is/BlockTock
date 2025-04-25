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
2. Select your Operating System from the dropdown menu and "CONFIRM OS".
3. Enter the website URL you want to block in the text box and click "ADD WEBSITE".
4. Click "BLOCK" to restrict access to the website.
5. To regain access, click "UNBLOCK" at any time.

## Notes

Comment out the following lines if you're not running this app on Windows:

Line 7: 

import pwinstyles
<img width="451" alt="Screenshot 2025-04-25 at 1 33 10 PM" src="https://github.com/user-attachments/assets/562074dd-46bb-4b10-b156-4b7df09a8d3e" />

Lines 106 - 109: 

<img width="744" alt="Screenshot 2025-04-25 at 1 33 30 PM" src="https://github.com/user-attachments/assets/e28980e3-2a54-4307-bb31-6b61c1e0d779" />

## Acknowledgments and Code References

Portions of this project were developed with assistance from OpenAI's ChatGPT.
Components of this project were adapted from:
[SmashFrenzy16/Website-Blocker](https://github.com/SmashedFrenzy16/Website-Blocker), licensed under [Apache License 2.0]
[Yash-2403/Python-Website-Blocker](https://github.com/Yash-2403/Python-Website-Blocker)
[AzharAnwar9/Python-Website-Blocker](https://github.com/AzharAnwar9/Python-Website-Blocker/tree/main)

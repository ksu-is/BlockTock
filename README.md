## BlockTock: A Productivity Enhancement Website Blocker App

## Overview

Are you sick of scrolling and wasting precious time? Then BlockTock is for you! This project uses Python to create a productivity app that allows the user to enable/disable access to selected websites for specified periods. In today's world, many people struggle with time management due to excessive distractions. This is a great solution to help users stay on task and prevent time wasted on social networking and messaging apps. Get your time back now!

## Pre-requisites

1. Python 3.x installed on machine
2. The script is currently working on Windows & Mac Operating Systems and all Linux Distributions.
3. A file containing a list of URLs/Domains must be present in the same folder as the application.
4. The script is required to be executed in admin mode(see details in the How to Use section).

## How It Works

Once the app is executed, BlockTock will ask the user to accept if they want to enable the filtering mode with the following prompt: (Y/y or N/n). The app will then prompt the user to input which websites they wish to block with the proper URLs. Next, the user will determine how long they wish to block the website for in the user prompt. Once the filtering mode has been selected and the user has provided the above information, default content filtering will be enabled until the user manually disables it in the app or the allotted time runs out. The user can press cancel any time on the app, and the filtering will be automatically removed. Filtering will not be executed unless the user manually enables the website blocking.

## How to Use

1. The project maintains a separate file for a list of URLs/Domains, so anytime you want to add any new URL/s or remove existing URL/s you just need to edit that text file and add a new URL on a new line, and the script is ready for use. This simple text file can be updated anytime and script will automatically fetch the details from the file and filter the websites provided.
2. The script will automatically detect the underlying Operating System to determine the host file's directory.
3. Once the script is executed successfully and the prompt is accepted, the chosen websites will be blocked for the full time duration input, unless the filtering is canceled manually.
4. Even if by mistake, the cancel command will be sent to the script for termination of filtering, and a prompt will be displayed to confirm the disable action.
5. Upon disabling the content filtering, normal functioning on the browser will apply automatically, and the user won't need to verify that website access has been granted again.



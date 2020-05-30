"""
Name: Mr. Callaghan
Date: 9/5/17
Filename: unit1_notes.py  (or) unit1Notes.py  TALK ABOUT FILE NAMING STANDARDS & SAVING
    .py is the Python file extension
Title: Unit 1: Getting Started
Description: Demonstrates Python basics and how to print to the screen.
""" 
# This is a single-line comment in Python. It will not show up on our output.  
#   The header of the document is a multi-line comment (surrounded by """)
#   Comments help us mark up our code with notes to ourselves and others.

# Python has many features that make it desirable:
#   - clean, simple syntax make it popular with beginners 
#   - high-level programming language (further from machine code)
#   - platform independent
#   - open source
#   - practical due to its wide adoption and variety of libraries

# IDLE is the default Python IDE. We will use repl.it, a cloud IDE.

'''
The PYTHON SHELL is the window that has the Python version number in  repl.it. 
It is where we see the output after we run a program.
Use it to test code snippets immediately; not meant to write and save programs. 

The CODE EDITOR is the main window where we write and save our programs.
The file name defaults to main.py when you open a new repl.it project.
'''

# print function: use to display text on output screen

print("Hello, World.") # print() = function ; "Hello, World." = argument(string value)

# FUNCTION - mini-program that goes and accomplishes some task for us
# ARGUMENT - information you send into a function
# STRING - series of characters enclosed in quotes (more to come...)

"""
CHALLENGE: print the following:
Hello, World.
(blank line)
My name is <your name>.
"""

print("Hello, World.")
print() #blank line
print("Nice to meet you, Python!")
print()

# Python:
#   ignores blank lines and spaces (for the most part)
#   cares about indentation
#   is case sensitive

# SYNTAX ERROR: Python does not recognize something (usually a typo). RED!!!
#   e.g. 
#   #prnt()

# last line of code - include on ALL programs to keep console window open when finished.
# SHOW EXAMPLE OF RUNNING A PROGRAM OUTSIDE IDLE

input("\nPress enter to exit.") 
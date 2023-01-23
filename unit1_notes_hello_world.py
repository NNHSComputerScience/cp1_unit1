# hello_world.py  (name of the current file we are writing in)
# import hello_world  (how we run our code; the hello_world.py file, from the main.py file in replit; main.py will always be executed when you press "run")
# Python files end in the .py file extension and should not include any spaces in the filename

"""
Name: Mr. Callaghan
Title: Hello, world.
Description: Demonstrates Python basics and how to print to the screen.
""" 

# Python has many features that make it desirable:
#   - clean, simple syntax make it popular with beginners 
#   - high-level programming language (further from machine code)
#   - platform independent
#   - open source
#   - practical due to its wide adoption and variety of libraries

# IDLE is the default Python IDE. We will use repl.it, a cloud IDE.

'''
The PYTHON SHELL (or CONSOLE) is the window that has the Python version number in  repl.it. 
It is where we see the output after we run a program.
Use it to test code snippets immediately; not meant to write and save programs. 

The CODE EDITOR is the main window where we write and save our programs.
The file name defaults to main.py when you open a new repl.it project.
'''

# in order to run a file in replit

# print function: use to display text on output screen

print("Hello, World.") # print() = function ; "Hello, World." = argument(string value)

# FUNCTION - sub-routine, or mini-program, that goes and accomplishes some task for us (e.g. print())
# ARGUMENT - information you send into a function (e.g. "Hello, World.")
# STRING - series of characters enclosed in quotes (more to come...) (e.g. "Hello, World")

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
#   cares about indentation (IndentationError: unexpected indent)
#   is case sensitive (NameError: name 'Print' is not defined)

# SYNTAX ERROR: Python does not recognize something as valid (usually a typo). RED!!!
#   e.g. 
#   #prnt() # NameError: name 'prnt' is not defined

# forgeting to close parentheses is a common syntax error
#		e.g. SyntaxError: invalid syntax with a misleading line number
# print("Hello, world"

print("Hello again.")

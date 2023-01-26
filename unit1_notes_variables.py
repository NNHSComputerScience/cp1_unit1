"""
Name: 
Title: Math, Variables, User Input, & Types
Description: Working with fundametal data types and operations in Python. Storing data in variables. Interacting with a user.
"""

# VARIABLE - a user-defined name in a program, which provides a way to access information stored in a computer's memory.
#   Follow all variable naming rules and conventions:

# Rules for legal variable names:
#  - Contain only numbers, letters, and underscores
#  - Can’t start with a number
#  - Can’t be a reserved keyword in Python (print, input, type, etc.)

# Guidelines for good variable names:
#  - Be descriptive of a variable's contents
#  - Be consistent with formatting
#  - Follow conventions: 
#     - names that begin with an underscore have a special meaning
#     - don’t begin with a capital letter 
#  - Consider the trade-off of long names
#   !!! Instructor note: review slides on variables

name = "Monty"  # read as: assign the string value "Monty" to variable "name"

# Reassigning to a variable to update its value
name = "Python" # we can't get "Monty" back!
#print(name) 

# ASSIGNMENT STATEMENT: assigns a value to a variable; creates (INITIALIZES) variable if necessary
# ASSIGNMENT OPERATOR: = (equals sign); assigns values from right to left ONLY 

result = "0"	# string
print(result)
result = 3 # int
print(result)

# !!! Instructor note: Do peer instrution question #1

# INPUT function - Pauses program execution and gets typed text from the user of our program. Returns it to you as a string.
#    Only accepts 1 string argument, which should be a prompt to the user on what to type. User presses 'Enter" when done typing.
#    Tip: Including a space at the end of your string argument makes the prompt more user-friendly.
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
print("Printed with a comma:", first_name, last_name)

# CONCATENATION: Two strings combined into one using the plus sign.

name = first_name + " " + last_name
print("Printed with concatenation:", name)

# string repetition
print("happy" * 100)

# !!! Instructor note: Do Peer instruction 2.1 & 2.2

# expressions will always be evaluated before they are passed into a function
print("\nWelcome to the calculator program", name + "!")

# using a comma - separates arguments & inserts a space
# using concatenation - doesn't insert a space & combines strings

# Numbers in Python - 2 new TYPES:
#   INTEGER(int) - whole numbers, no decimal point 
#   FLOATING POINT NUMBER (float) - decimal number
result = 0		# integer
result = 0.0	# float
print("\nThe starting result is:", result)

# Built-in functions to convert types:
#   str() converts to a string
#   int() converts to an int
#   float() converts to a float
num1 = input("\nPlease enter your first number: ") # string
num1 = int(num1)  # integer

# nesting functions: putting one function inside another
num2 = float(input("Please enter your second number: ")) # float

input("\n\nPress enter to process calculations...")
print("---------------------------------------")
# Math Operators:
#   + , - , / , //, * , ** , % 

# addition
result = num1 + num2
print(num1, "+", num2, "=", result)  
# subtraction
result = num1 - num2
print(num1, "-", num2, "=", result)	
# true (floating point) division
result = num1 / num2
print(num1, "/", num2, "=", result)	 
# integer division - leaves off remainder
result = num1 // num2
print(num1, "//", num2, "=", result)  
# multiplication
result = num1 * num2
print(num1, "*", num2, "=", result)	 
# exponents
result = num1 ** num2
print(num1, "**", num2, "=", result)   
# modulus - gives the remainder
result = num1 % num2
print(num1, "%", num2, "=", result)

# STATEMENT - a complete thought in a programming language (equivalent to one complete line of code)
#       e.g. print(2+2)
# EXPRESSION - code that can be evaluated to a new value (like a math operation)
#       e.g. 2+2

print("\nThanks for using the Python calculator. Re-run program for new numbers.")

# !!! Instructor note: do variable tracing programs using slides

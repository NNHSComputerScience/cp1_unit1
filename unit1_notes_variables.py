"""
Mr. Callaghan
Date
unit1_notes.py
Unit 1 Notes: Math, Variables, User Input, & Types
"""

print("--- DAY 3 --------------------------------------------")
# Math operators, variables, user input, & types

# CONCATENATION: 2 strings combined into 1
print ("cup")
print ("cake")
print ("cup" + "cake")
print ()

# string repetition
print ("happy")
print ("happy" * 100)    # can't divide or subtract a string
print ()

# Numbers in Python (2 new 'types' of values):
#   INTEGER(int) - whole numbers, no decimal point 
#   FLOATING POINT NUMBER (float) - decimal number
# Math Operators:
#   + , - , / , //, * , ** , % #CHALLENGE: predict what will happen and run
print (2+2)
print (5-2)
print (19/4)    # true division
print (19//4)   # integer division - leaves off remainder
print (2*7)
print (3**3)    # exponents
print (11%3)    # modulus - gives the remainder
 
# STATEMENT - a complete thought in programming (usually one complete line of code)
#       e.g. print(2+2)
# EXPRESSION - code that can be evaluated to a new value (like a math operation)
#       e.g. 2+2

# VARIABLE - a user-defined name in a program, which provides a way to access
#   information stored in a computer's memory.
#   Follow all variable naming rules and conventions.
#   !!! review slides on variables: 

name = "Monty"  # read as: assign the string value "Monty" to variable "name"

print(name) 

# ASSIGNMENT STATEMENT: assigns a value to a variable;
#   creates (INITIALIZES) variable if necessary
# ASSIGNMENT OPERATOR: = (equals sign); assigns values from right to left ONLY 

# Reassigning to a variable to update its value
name = "Python" # we can't get "Monty" back!
print(name)

# input function - Pauses program execution and gets typed text from the user of our program. Returns it to you as a string.
#    Only accepts 1 string argument, which should be a prompt to the user on what to type. User presses 'Enter" when done typing.
#    Tip: Including a space at the end of your string argument makes the prompt more user-friendly.
name = input("What is your name? ")
                              
num = 7 # int
num2 = 7.7 # float
print(name, num, num2) # we can save any type of value in a variable

# CHALLENGE: Store the user's first, middle, and last names in 3 separate 
#       variables and then print the following: "Hello, <FIRST> <MIDDLE> <LAST>!"

first = input("Enter your first name: ") 
middle = input("Enter your middle name: ") 
last = input("Enter your last name: ") 

print("Hello," , first , middle , last + "!")

# using a comma - inserts a space & separates arguments 
# using concatenation - doesn't insert a space & combines strings

# TYPES we know in Python: String values, Int values, and Float values 
# Built-in functions to convert types:
#   str() converts to a string
#   int() converts to an int
#   float() converts to a float

num = int(input("Enter a number: "))    # nesting functions - one inside another
# num = int(num)
# num = float(num)
print(num + num)

# !!! do variable tracing programs using slides
 
input("\nPress enter to exit.")

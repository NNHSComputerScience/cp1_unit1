"""
Mr. Callaghan
Date
ch2_notes.py
Ch. 2 Notes: Types, Variables, & Simple I/O
"""

print("--- DAY 1 --------------------------------------------")
# Printing String Values

# printing quotes
print ("Mr. C said, 'Hello, class'!")
print ('Mr. C said, "Hello, class!"')
# see more below
print ()

# triple quoted string: displays text WITH my typed formatting
print ("""This is a triple-quoted string
and is displays text with my typed
formatting included!""") 
print ("""Mr. C said, 'Hello, class'!""")
print ()

# line continuation
print ("This is line 1, ", end="") #end="" removes the new line in a print 
print ("This is line 2")
print ()

# escape sequences (for strings): 
#   \t , \n , \\" (see page 24) 
print ("Name\tAge\tJob\t")
print ("Matt Callaghan\t32\tTeacher")
print ("Insert new line below!\n")
print ("Line 2")
print ("MM\\DD\\YYYY")
print ("Mr. C said, \"Hello, class!\"")
print ()

# continuing a print (you should never need to scroll to the right!)
print ("This is a really long string and you should never have" \
"to scroll to the right when writing code because it is really" \
"annoying.")
print ()

# CHALLENGE: Go back and re-try the challenge prompts

# Using math operators

# CONCATENATION: 2 strings combined into 1
print ("cup")
print ("cake")
print ("cup" + "cake")
print ()

# string repetition
print ("happy")
print ("happy" * 100)    # can't divide or subtract a string
print ()

# Numbers in Python:
#   integer(int) - whole numbers, no decimal point
#   floating point number (float) - decimal number
# Math Operators:
#   + , - , / , //, * , ** , % (page 29)
print (2+2)
print (5-2)
print (19/4)    # true division
print (19//4)   # integer division
print (2*7)
print (3**3)    # exponents
print (11%3)    # modulus - gives the remainder

print("\n-- day 2 ---------------------------------------------------\n")

# VARIABLE - a name to represent a value; provides a way to get at
#   information in a computer's memory.

# ASSIGNMENT STATEMENT - assigns a value to a variable;
#   creates (INITIALIZES) variable if necessary

name = "Monty"  # read as: assign the string value "Monty" to variable "name"

print ("Monty")
print (name)

# using a comma - inserts space & separates arguments
print ("Hi,", name)

# using concatenation
print ("Hi, " + name + "!")

# getting info from the user
name = input("What is your name?")   # input function always returns a string

print ("The variable 'name' is now", name)

# How many variables exist in these notes? 

print("\n-- day 3 ---------------------------------------------------\n")

# STRING METHODS
# dot notation (object.method)
#   OBJECT = thing you are running the method on (possibly a variable)
#   METHOD = function you are running on the object - don't forget functions need ()
name = "Monty Python"
print (name.upper())
print (name.lower())
print (name.title())
print (name.swapcase())

# user input with string method
name = input("What is your name: ").title()
print(name)

# Test Question 1 - In the assignment statement above, identify the argument.
#   "What is your name: "
# Test Question 2 - In the assignment statement above, identify the method.
#   title()
# Test Question 3 - In the assignment statement above, identify the return value.
#   Whatever the user types in

# round method - built in Python function
var = 3.3333333333333333333
round(var, 2)

# AUGMENTED ASSIGNMENT OPERATORS
total = 0
total = total + 10
print (total)
print()
 
total += 10     # same as total = total + 10
print (total)
total *= 10
print (total)
total -= 10
print(total)

# Test question: What is total printed at the end of the following code?
# value1 = 5
# value2 = 10
# total = 0
# total += value1   # 5
# total *= value2   # 50
# print (total)


input("\n\nPress enter to exit.")


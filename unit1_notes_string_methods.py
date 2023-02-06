"""
Name: Mr. Callaghan
Title: String methods & augmented assignment operators
Description: Running methods on strings and better ways to write operators.
"""

# OBJECT - an entity in a program that can be manipulted using methods (String in this case) 
# METHOD - procedure you are calling on an object to manipulate it (parentheses are required) 
# STRING METHODS - methods that allows us to obtain new string values from existing string values
# DOT NOTATION - <object>.<method>(<potential arguments>)

name = "Monty python"
print(name)
name_upper = name.upper()
print(name_upper)
name_lower = name.lower()
print(name_lower)
name_title = name.title()
print(name_title)
name_swap = name.swapcase()
print(name_swap)
name_replace = name.replace("o", "i")
print(name_replace)
print("Original name:", name)
# name remains its original value; methods return new strings rather than changing the exisiting string
# RETURN VALUE - value received back after calling a function or method. 

'''  OPTIONAL TO SHOW IN SHELL
Type in shell:
>>> name = "Monty python"
>>> name
'Monty python'
>>> name.upper()
'MONTY PYTHON'
>>> name.lower()
'monty python'
>>> name.title()
'Monty Python'
>>> name.swapcase()
'mONTY PYTHON'
>>> name.replace("o", "i")
'Minty pythin'
>>> name
'Monty python'    # name remains its original value; methods return new strings rather than changing the exisiting string
>>> name = name.upper()
>>> name
'MONTY PYTHON'
''' 

# handling user input with string methods
name = input("What is your name: ").title() # chaining methods can save some typing
#name.title() # must assing the new string!
# name = name.title()
print(name)

# !!! DO PEER INSTRUCTION #4

# Python Documentation for The Python Standard Library (python.org) is the official reference for language features.
#   Google 'python docs' followed by the documentation you are looking for. (e.g. "Python docs String")

# STRING FORMATTING - .format() method and f-strings improves the ability to work with strings 
#   and other data types. Python has fill-in-the-braces format, similar to 
#   fill-in-the-blank questions.

# INPUTS
origPrice = float(input('Enter the original price: $'))
discount = float(input('Enter discount percentage: '))

# !!! Fill in the rest and have students try to figure out the formula for this calculation in pairs on scratch paper.
# !!!    Suggest working with sample values (e.g. $100 discounted by 20% is $80)
# CALCULATIONS
newPrice = (1 - discount/100) * origPrice

# OUTPUT

# Formatting currency in Python
#  , is thousands separator; .2f stands for two decimal float

# The .format() string method has been upgraded in recent versions of Python with f-strings.
calculation = f'${origPrice:,.2f} discounted by {discount}% is ${newPrice:,.2f}.'
print(calculation) 

print(f"\nf-strings can even evaluate expressions!: {10 * 10}")

# Python has certain built-in functions which are always available (google "Python docs built-in functions")
#    e.g. print, input, int, float, str, round, and abs can be used in any program
num = -3.3333333333333333333
num = round(num, 2)  # round function - rounds float to a specified number of decimal places
num = abs(num)       # absolute value function - returns absolute value of a number
print(num)

# AUGMENTED ASSIGNMENT OPERATORS - shortcut ways to combine math operators
#   and assignment operator
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
total /= 10
print(total)
total //= 10
print(total)
total %= 10
print(total)


# !!! DO PEER INSTRUCTION #5

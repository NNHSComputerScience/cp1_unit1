"""
Name: Mr. Callaghan
Date:
Title: Unit 1 Notes: String methods & augmented assignment operators
Description: Running methods on strings and better ways to write operators.
"""

# OBJECT - an entity in a program that can be manipulted using methods (String in this case) 
# METHOD - procedure you are calling on an object to manipulate it (parentheses are required) 
# STRING METHODS - methods that allows us to obtain new string values from existing string values
# DOT NOTATION: <object>.<method name>(<potential arguments>)

my_string = "hello, world."
my_string = my_string.upper()
print(my_string)

'''
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

# RETURN VALUE - value received back after calling a function or method. 

# handling user input with string methods
name = input("What is your name: ").title() # chaining methods can save some typing
#name.title() # must assing the new string!
# name = name.title()
print(name)

# DO THE FOLLOWING IN PEAR DECK:
'''
Test Question 1 - In the assignment statement above, identify the argument. 
   "What is your name: " 
 Test Question 2 - In the assignment statement above, identify the method. 
   .title() 
 Test Question 3 - In the assignment statement above, identify the return value. 
    whatever the user types in converted to title format; the input function
    returns whatever the user types in and the string method returns that value
    converted to title format and assigns it to name.
'''

# Python Documentation for The Python Standard Library (python.org) is the official reference for language features.
#   Google 'python docs' followed by the documentation you are looking for. (e.g. "Python docs String")

# STRING FORMATTING - .format() method improves the ability to work with strings 
#   and other data types. Python has fill-in-the-braces format, similar to 
#   fill-in-the-blank questions.
origPrice = float(input('Enter the original price: $'))
discount = float(input('Enter discount percentage: '))
newPrice = (1 - discount/100)*origPrice
calculation = '${} discounted by {}% is ${}.'.format(origPrice, discount, newPrice)
print(calculation) 

# Formatting currency in Python
#  , is thousands separator; .2f stands for two decimal float
amount = 123456.78
currency = "${:,.2f}".format(amount)  
print(currency)

# The .format() string method has been upgraded in recent versions of Python with f-strings.
calculation = f'${origPrice:,.2f} discounted by {discount}% is ${newPrice:,.2f}.'
print(calculation) 
print(f"f-strings can even evaluate expressions: {10 * 10}")

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

# DO THE FOLLOWING IN PEAR DECK:
'''
Test Question 4: What is total printed at the end of the following code? 
value1 = 5 
value2 = 10 
total = 0 
total += value1   # 5
total -= total    # 0
total *= value2   # 0 
# print (total)
'''

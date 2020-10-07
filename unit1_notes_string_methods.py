"""
Mr. Callaghan
Date
unit1_notes_string_methods.py
Unit 1 Notes: String methods & augmented assignment operators
"""
 
print("\n-- Day 4 ---------------------------------------------------\n")
# String methods & augmented assignment operators

# OBJECT = the thing (String in this case) on which you call the method (referenced by a variable) 
# METHOD = procedure you are calling on an object to manipulate it (parentheses are required) 
# STRING METHODS - methods that allows us to obtain new string values from existing string values
# DOT NOTATION: <object variable name>.<method name>(<potential arguments>)

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
calculation = '${:.2f} discounted by {}% is ${:.2f}.'.format(origPrice, discount, newPrice)
print(calculation) 

# ROUND and ABSOLUTE VALUE FUNCTIONS are additional built-in functions (google "Python docs built-in functions")
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


input("\nPress enter to exit.") 


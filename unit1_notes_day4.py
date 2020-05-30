"""
Mr. Callaghan
Date
unit1_note_day4.py
Unit 1 Notes: Types, Variables, & Simple I/O
"""
 
print("\n-- Day 4 ---------------------------------------------------\n")
# String methods & augmented assignment operators

# STRING METHODS - methods that allows us to obtain new string values 
# DOT NOTATION: <object variable>.<method name>()
#   OBJECT = the thing on which you call the method (referenced by a variable) 
#   METHOD = procedure you are calling on an object (parentheses are needed) 

# RETURN VALUE - value received back from calling a function or method 
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
'Monty python' # name remains original value; methods return new strings 
''' 

# handling user input with string methods
name = input("What is your name: ").title()
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

# Python Documentation - The Python Standard Library (python.org)
#   Google 'python docs' followed by the ducumentation you are looking for.

# ROUND and ABSOLUTE VALUE FUNCTIONS
num = -3.3333333333333333333
num = round(num, 2)  # round function - rounds float to a specified number of decimal places
num = abs(num)       # absolute value function - returns absolute value of a number
print(num)

# STRING FORMATTING - .format() method improves the ability to work with strings 
#   and other data types. Python has fill-in-the-braces format, similar to 
#   fill-in-the-blank questions.
origPrice = float(input('Enter the original price: $'))
discount = float(input('Enter discount percentage: '))
newPrice = (1 - discount/100)*origPrice
calculation = '${:.2f} discounted by {}% is ${:.2f}.'.format(origPrice, discount, newPrice)
print(calculation) 

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


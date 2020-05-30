# Trust Fund Buddy - Good
# Intro to debugging - demonstrates a logical error

# SYNTAX ERROR - you have broken Python's rules; usually just a typo
#   e.g. forgot to close your parentheses
# RUNTIME ERROR - an error is encountered while running the program; also called EXCEPTIONS
#   e.g. tried to divide by zero
# LOGICAL ERROR - code is runs fine, but does not produce the expected result; also called SEMANTIC ERRORS
#   e.g. concatenating strings when you meant to add numbers
# TYPE ERROR - you used the wrong type of value somewhere in an expression or as an argument

print(
"""
Trust Fund Buddy

Totals your monthly spending so that your trust fund doesn't run out
(and so you aren't forced to get a real job).

Please enter the requested, monthly costs.  Since you're rich, ignore pennies
and use only whole dollar amounts.

""")

car = int(input("Lamborghini Tune-Ups: "))
rent = int(input("Manhattan Apartment: "))
jet = int(input("Private Jet Rental: "))
gifts = int(input("Extravegant Gifts: "))
food = int(input("Dining Out: "))
staff = int(input("Staff (butler, chef, driver, assistant): "))
guru = int(input("Personal Guru and Coach: "))
games = int(input("Computer Games: "))

total = car + rent + jet + gifts + food + staff + guru + games

print ("\nGrand Total: $" + str(total))

input("\n\nPress the enter key to exit.")


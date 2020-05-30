# Trust Fund Buddy - Good
# Intro to debugging - demonstrates a logical error

# LOGICAL ERROR - code runs fine, but does not produce the expected result
# SYNTAX ERROR - usually a typo, means you are not conforming to Python's rules
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


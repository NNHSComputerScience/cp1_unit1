# Trust Fund Buddy - Bad
# trust_fund_bad.py
# Intro to debugging - demonstrates a syntax, runtime, and logical errors
# Instructions: Step through this program line-by-line, as if you were the Python interpreter.
#		As you identify errors, categorize them as Syntax Errors, Runtime Errors, or Logic Errors.
#		Run the program to see how Python reacts to the error and then debug them so the program 
#		works as intended.

print(
"""
Trust Fund Buddy

Totals your monthly spending so that your trust fund doesn't run out
(and so you aren't forced to get a real job).

Please enter the requested monthly costs.  Since you're rich, ignore pennies
and use only whole dollar amounts.

""")

name = input("What is your name? ")

car = input("Lamborghini Tune-Up(s): "))
rent = input("Manhattan Apartment: ")
jet = input("Private Jet Rental: ")
gifts = input("Extravegant Gifts: ")
food = input("Dining Out: ")
staff = input("Staff (butler, chef, driver, assistant): 
guru = input("Personal Guru and Coach: ")
games = input("Computer Games: ")

car + rent + jet + gift + food + staff + guru + games = total

prinf()
print(name.title(), "'s Total Monthly Expenses: $" + total)
              
input("/n/nPress the enter key to exit.")


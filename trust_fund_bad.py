# Trust Fund Buddy - Bad
# trust_fund_bad.py
# Intro to debugging - demonstrates a logical error

print(
"""
Trust Fund Buddy

Totals your monthly spending so that your trust fund doesn't run out
(and so you aren't forced to get a real job).

Please enter the requested, monthly costs.  Since you're rich, ignore pennies
and use only whole dollar amounts.

""")

car = input("Lamborghini Tune-Ups: ")
rent = input("Manhattan Apartment: ")
jet = input("Private Jet Rental: ")
gifts = input("Extravegant Gifts: ")
food = input("Dining Out: ")
staff = input("Staff (butler, chef, driver, assistant): ")
guru = input("Personal Guru and Coach: ")
games = input("Computer Games: ")

total = car + rent + jet + gifts + food + staff + guru + games

print ("\nGrand Total: " + total)

input("\n\nPress the enter key to exit.")


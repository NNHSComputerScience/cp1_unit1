"""
# COMPLETE COMMENT HEADER
Name: 
Date:
Title: Pizza Program, pizza_program.py
Description: Asks the user for how many pizzas they wold like to order
    and calculates the total cost.  Displays the information in nice format.
"""

# welcome message to the program
print('Welcome to the "Pizza Program"')

# initialize variables and get user input
cost = 10.0
name = input("What is your name?: ")
phone = input("What is your phone number " + name + "?: ")
amount = int(input("Pizzas cost $" + str(cost) + ". How many pizzas would you like?: ")) # convert string input into an integer

# cost calculation
total_cost = cost*amount

# display output in a nice format
print (name, "-", phone, ": Has ordered", amount, "pizzas.")
print("The total cost is $" + str(total_cost) + ".")


input("\n\nPress enter to exit.")

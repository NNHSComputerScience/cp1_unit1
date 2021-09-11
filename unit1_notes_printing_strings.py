"""
Name: Mr. Callaghan
Date:
Title: Unit 1 notes - printing strings
Description: Printing strings and escape sequences
"""

# Printing String Values
# STRING = Our first 'type' of value in Python.  It is a series of characters
#       surrounded by single, double, or triple quotes.
type("test string") # in shell

# printing quotes
print ("Mr. C said, 'Hello, class'!")
print ('Mr. C said, "Hello, class!"')
# see more below
print ()

# triple quoted string: displays text WITH typed formatting
print ("""This is a triple-quoted string
and is displays text with my typed
formatting included!""") 

# ASCII art example:
print(
"""
       _.---._    /\\
    ./'       "--`\//
  ./              o \          .-----.
 /./\  )______   \__ \        ( help! )
./  / /\ \   | \ \  \ \       /`-----'
   / /  \ \  | |\ \  \7--- ooo ooo ooo ooo ooo ooo
"""
)
print ()
print ("""Mr. C said, 'Hello, class'!""")

# line continuation; continuing a print (you should never need to scroll to the right!)
#   repl.it will wrap lines for you if you enable that feature
print ("This is line 1, ", end="") #end="" removes the new line in a print 
print ("This is line 2")
print ()

# adding more than 1 argument
#   some functions can accept more than 1 argument
#   print() can accept unlimited arguments; input() only accepts 1 argument
print("Hello, World." , "How are you?")
# input("Press enter to exit." , "Please.")

# ESCAPE SEQUENCES - characters used inside of strings to gain more control over the behavior of the text.
#   \t (tab)
print ("Name\tAge\tJob\t")
print ("Matt Callaghan\t32\tTeacher")

# \n (new line)
print ("Insert new line below!\n")
print ("Line 2")

# \\ (backslash)
print ("MM\\DD\\YYYY")

# \"  \' (quotation)
print ("Mr. C said, \"Hello, class!\"")
print ()

# CHALLENGE: Go back and re-try the printing challenge prompts 

input("\n\nPress enter to exit.") 

"""
Name: Mr. Callaghan
Title: Unit 1 notes - printing strings
Description: Printing strings to the console and escape sequences
"""

# Printing String Values
# STRING - Our first 'type' of value in Python.  It is a series of characters surrounded by single, double, or triple quotes.
# TYPE - A category of data in a programming langauge that determines what kinds of operations can be performed.
#      Classes, like the Turtle class, are types.
# The type() function will return the type of a value
#      e.g.,
type("test string") # in shell

print("Hello, world.") # printing a string

# printing quotes
print ("Mr. C said, 'Hello, class'!")
print ('Mr. C said, "Hello, class!"')
print ("""Mr. C said, 'Hello, class'!""")
print()

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

# line continuation; continuing a print on the same line (you should never need to scroll to the right!)
#   repl.it will wrap lines for you if you enable that feature
#   including end="" as the final argument in a print function removes the implicit new line character included in a print statement
# e.g.,
print ("This is line 1, ", end="") 
print ("This is line 2,", end=' ')
print ("This is line 3.")
print("This is line 4.")

# input function - pauses execution and waits for the user to type and press enter
#      unlike print(), input() accepts only one arguement
input("Press enter to comtinue...")
# input("Press enter to continue..." , "Please.") # error

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

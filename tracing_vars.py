# Mr. Callaghan
# DATE
# tracing_vars.py
# Create tracing programs to demonstrate how variable values can change

# initialize variables
x = 5
y = 10
z = 2

# tracer program #1
x = x+5
z = y+10
x = x+5
y = x+10
z = z*2

print (x)
print (y)
print (z)

print ("\n----------------------------------------------\n")

# initialize variables
x = 5
y = 10
z = 2

# tracer program #2
y = 2*10+x-5
x = z*x+(x-3)
y = 2*x-3
z = 1
x = x*2+1

print (x)
print (y)
print (z)

print ("\n----------------------------------------------\n")

# initialize variables
x = 5
y = 10
z = 2

# tracer program #3
x = x**2
y = x+y
z = y+x
x = z-y+x
y = y//4
y = y**3
z = y-x+z

print (x)
print (y)
print (z)

print ("\n----------------------------------------------\n")

# initialize variables
x = 5
y = 10
z = 2

# tracer program #4
x = x-3
y = x+y
y = y+x
z = x
x = z-x
y = z

print (x)
print (y)
print (z)

input("\nPress enter to exit.")
    

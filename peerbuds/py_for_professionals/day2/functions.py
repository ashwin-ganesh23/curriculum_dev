"""
Functional Programming in Python

Topics include:
	-Warm-up Exercise
	-Functions, Modules and Classes
	-Intro to File Object

Part 2 : Functions

"""

# Functions or methods are defined blocks of resuable code that accept input parameters and output a return value
# In python3, functions are followed by parentheses as we noticed when using print()

# In order to define a function, one must use the def keyword followed by the function name, parentheses and a colon

def first_function():
	print("No parameters and no return values")

# Now let's look at an example involving an input parameters

def welcome_name(name):
	print("Welcome to the wonderful world of programming {}!".format(name))

welcome_name("Ashwin")

# Return values can be used when we have a value or values that we want to use later in our programm

def return_sum(a, b):
	return(a + b)

total = return_sum(6, 4)	#function call can be substituted with the return value
print(total)

# Note: if there are no return values, the default return value is None
# None is a representation of the absence of value

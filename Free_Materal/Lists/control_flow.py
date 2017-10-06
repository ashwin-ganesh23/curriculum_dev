"""
Introduction to Operators and Decision Making

We will cover three types of operators: Comparison, Arithmetic, and Logical Operators

We will also cover three conditional statements: if, elif, and else statements

"""

num1 = 45

num2 = 15

str1 = "python"

str2 = "rocks!"

# Comparison Operators - >, >=, <, <=, ==, !=
#print(num1 > num2)



# Arithmetic Operators - +, -, *, /, %, **
#print(num1 / num2)
# print((str1 + " ") * 3)



# bool1 = True
# bool2 = False

# Logical Operators -
# print( bool1 and True )
#
# print( bool2 or False )


# Decision Making - allows program to react to conditions and execute code appropriately

str1 = 'hungry'
str2 = 'full'
budget = True

if str1 == 'hungry':
	if budget:
		print("lets get MCDS")
	else:
		print("lets get chipotle")
elif str2 == "full":
	print("how about a beer?")
else:
	print("sleep")
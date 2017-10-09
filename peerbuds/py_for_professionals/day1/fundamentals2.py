	"""
Fundamentals of Python

Topics include:
	-Variables and Data Types
	-Control Flow
	-Data Structures


Part 2 : Control Flow

"""

# Comparison Operators ( > , >= , < , <= , == , != )
# 	note: we cannot compare unlike types, for example str and int/float

print( 100 > 15 )


# Conditional Statements - if / elif / else

password = "feedyoursoul"


#	if condition is true, execute the following block
#		syntax note: after a statement that ends with a colon, :
#		every line that is indented is included in the executed block
if password == "feedyourcuriosity":
	print("Connected to Peerbuds 5G! Enjoy your connection")


#	if statements can be optionally followed by an else statement
if password == "feedyourcuriosity":
	print("Connected to Peerbuds 5G! Enjoy your connection")
else:
	print("Incorrect password")

#	elif statements are introduced when there are one of many possible routes
#	they must be associated with a preceding if statement

file_mode = 'append'

if file_mode == 'read':
	print("Our file is in read mode")
elif file_mode == 'write':
	print("Our file is in write mode")
elif file_mode == 'append':
	print("Our file is in append mode")
else:
	print("What else is there...?")

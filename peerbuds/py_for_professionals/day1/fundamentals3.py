"""
Fundamentals of Python

Topics include:
	-Variables and Data Types
	-Control Flow
	-Data Structures


Part 3 : Control Flow - Loops

"""

# while loops
# example:
# while condition:
#

counter_var = 10
while counter_var >= 0:
	print(counter_var)
	counter_var -= 1


# for .. in .. loops
# for loops in python iterate through a sequence
# the most common example of sequence is a list

name_list = ["Sal", "Surag", "Chris", "Ashwin"]

for name in name_list:
	print("Hello my name is {}".format(name))


# another way for/in loops are commonly used is in conjunction with the range() function
# range(stop)
# range(start, stop[, step])

for num in range(0, 21, 2):
	print(num)

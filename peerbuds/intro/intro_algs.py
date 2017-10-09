"""
Introduction to Algorithms

Algorithms are problem-solving methods used by software engineers

They can be thought of as step by step directions to solving a problem

"""

# write an block of code that asks for an input number from the user
# and print whether the number is even or not

not_complete = True

while not_complete:
	user_num = input("Enter a whole number of your choosing: ")
	try:
		int(user_num)
		if user_num % 2 == 0:
			print("Your number is even")
		else:
			print("Your number is odd")
		not_complete = False
	except ValueError:
		print("Not an integer")

# write a block of code that iterates through a string entered from input and prints the number of letters entered

input_str = input("Enter a message: ")
for letter in input_str:
	count += 1

print(str(count) + " letters entered")

#or

# print(len(input_str) + " letters entered")

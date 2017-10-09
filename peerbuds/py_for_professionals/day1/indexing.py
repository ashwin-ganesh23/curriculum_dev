"""
Fundamentals of Python

Topics include:
	-Variables and Data Types
	-Control Flow
	-Data Structures

Part 5 : Indexing and Slicing Sequences

"""


# Now that we understand the BASICS of control flow and data structures,
# 	let's take a look at accessing values in sequences

# the first value always starts at index 0

int_list = [1, 2, 4, 8, 16, 32, 64, 128]

for num in range(len(int_list)):
	print(int_list[num])

print(int_list[0:4])

print(int_list[4:8])

print(int_list[0:7:2])

print(int_list[1:8:2])


# We can also use strings or tuples instead of lists
sentence = "Let's learn to slice this string!"

first_word = sentence[:5]
print(first_word)

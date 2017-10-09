"""
Fundamentals of Python

Topics include:
	-Variables and Data Types
	-Control Flow
	-Data Structures


Part 4 : Control Flow - Data Structures

"""


# We briefly covered lists in the last exercise with for loops
# Lets look deeper into lists - a sequential data structure

many_types_lst = [1, 2.0, 3, 'a', True]	# lists are characterized as having square brackets and elements separated by commas



# Tuples are another sequential data structure but differ from lists by being immmutable
# It may be tough to see the need for tuples when we have a dynamic data structure such as lists but,
# they are extremely useful for holding a format and return multiple values within a function

py_facts_tupl = (1991, 3.6, "high-level", "multi-purpose")	# Note: parentheses are not required but are standard



# Sets are mutable data structures that contain a collection of elements without duplicates

color_set = {"blue", "green", "purple", "blue", "pink"}

print(color_set)


# Sets can also be used with strings

next_concept = "dictionaries"

print(set(next_concept))


# Dictionaries are mutable data types that contained unordered collections of key, value pairs

main_concepts = {'Day 1': "Fundamentals of Python", 'Day 2': "Functional Programming", 'Day 3': "File and OS", 'Day 4': "Regex and Formats"}

for key, value in main_concepts.items():
	print("In {}, we will be covering {}".format(key, value))

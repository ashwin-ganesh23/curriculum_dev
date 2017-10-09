"""
Functional Programming in Python

Topics include:
	-Warm-up Exercise
	-Functions, Modules and Classes
	-Intro to File Object

Part 5 : Introduction to File Objects

"""

# In the final section for today we will be learning how to read, write, and append files

# The first step is to open() the file object with the appropriate file mode (r, w, a)
# 	note: the default file mode is read

file_object = open("file.txt", "w")	# note: file is created if it does not exist

file_object.write("Writing to our first file! Remember to close the file and include a \n at the end!\n")

file_object.close()

# Now we will open a file in it's default read mode and read the entire contents of the file

file_object = open("file.txt")

file_str = file_object.read()

print(file_str)

file_object.close()

# Finally we will append to the end of the file

file_object = open("file.txt", "a+")	# open for appending and reading

file_object.write("Now we can append whatever text stream we would like to the end of this file\n")

file_str = file_object.read()

print(file_str)

file_object.close()

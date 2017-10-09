"""
Functional Programming in Python

Topics include:
	-Warm-up: File Objects
	-OS Module
	-Intro to Regular Expressions

Part 1 : File Objects Warm-up

"""

# define a function that accepts two parameters, filename (str) and contents (str)
#

def new_file(filename, contents):
	fo = open(filename, 'w')
	fo.write(contents)
	fo.close()

def read_file(filename):
	if os.path.isfile(filename):
		fo = open(filename)
		contents = fo.read()
		fo.close()
		return contents
	else:
		return None

def append_file(filename, contents):
	fo = open(filename, 'a')
	fo.write(contents)
	fo.close()

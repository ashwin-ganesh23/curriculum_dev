"""
Functional Programming in Python

Topics include:
	-Warm-up Exercise
	-Functions, Modules and Classes
	-Intro to File Object

Part 1 : String Warm-up Exercises

"""

import string

# Write a Python program to store the character frequency of a string in a dictionary
def char_freq(s):
	lc = {}
	for char in s:
		if lc.get(char) != None:
			lc[char] += 1
		else:
			lc[char] = 1
	return (lc)

# Write a Python program to count the number of word occurences in a string in a dictionary

def remove_punctuation(s):
	final = ""
	for char in s:
		if char not in string.punctuation:
			final += char
	return (final)

def word_freq(s):
	wc = {}
	for word in s.split():
		w = remove_punctuation(word)
		if wc.get(w) != None:
			wc[w] += 1
		else:
			wc[w] = 1
	return (wc)

print(word_freq("whats going on homie on. test! mfer?"))

"""
Converting Data Types

Now that we have used our four data types, let's learn how to convert one data type to another

int()
float()
str()
bool()

This can be especially useful when using the input() function as its return value is a string.
We may want to convert our string into a number value to perform calculations!

"""

your_name = input("What is your name?")

your_age = input("How old are you?")

your_height = input("How tall are you? (in inches) ")


your_age = int(your_age)

your_height = float(your_height)

print(your_height)

height_feet = your_height / 12.0

print(height_feet)

print("Hello " + your_name + ", welcome to Peerbuds Innovation Lab")

str_age = str(your_age)

print("You're " + your_age + " years old, which is the perfect age to start coding!")

str_height = str(height_feet)

print("You're " + str_height + " feet tall")

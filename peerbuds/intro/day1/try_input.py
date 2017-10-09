"""
Using the input() method and Standard Input

input([prompt])

always returns a string

"""



name = input("What is your name?")
age = int(input("How old are you?"))
height = float(input("How tall are you in feet?"))


print("Hello World!")
print("Hello %s" % name)
print("Hello {}".format(name))



print(name, age, height, sep=' ')

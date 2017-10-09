"""
Decision Making / Control Flow / Conditional Statements

if / elif / else Statements

evaluates conditions and selects an according path within the programs flow


syntax example)

if condition:
	execute block
	...
elif condition2:
	execute block2
	...
elif condition3:
	excute ...
...
...
else:
	execute final option
	...

more code here

"""

answer = input("What service would you like to perform? (write, read, or append)")
name = input("What is the name of your file? (.txt will be appended) ")
name = name + ".txt"

if answer == "write":
	fo = open(name, 'w')
	message = input("Write your message here: ") + '\n'
	fo.write(message)
	fo.close()
elif answer == "read":
	fo = open(name, 'r')
	print(fo.read())
	fo.close()
elif answer == "append":
	fo = open(name, 'a')
	message = input("Write your message here: ") + '\n'
	fo.write(message)
	fo.close()
else:
	print("not recognized")

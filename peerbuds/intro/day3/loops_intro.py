"""
Introduction to Loops

While Loops and For Loops

while condition:
	block of code

for element in iterable:
	body

"""

import time


count = 0

while count <= 30:
	time.sleep(1)
	print(count)
	count += 1


project_grades = [78, 120, 56, 100, 88, 34, 150]

for grade in project_grades:
	total += grade
average = total / len(project_grades)



for number in range(1000, 100001, 4):
	if (number % 7 == 0 and number % 6 == 0)
		print(number)
		break

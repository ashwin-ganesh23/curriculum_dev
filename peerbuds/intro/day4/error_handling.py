"""
Introduction to Error Handling

Error or Exception Handling is used to catch unexpected circumstances

"""

data = input("Enter a numeric value: ")

def toFloat(data):
	try:
		data = float(data)
	except ValueError:
		raise ValueError('Parameter has invalid value')
toFloat(data)


# number1 = 15
# number2 =

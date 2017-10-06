a = float(input("enter a number"))
b = float(input("enter a number"))
operator = input('enter an operator (+, -, *, or /)')
if a > b:
	print('{:.2f} is greater than {:.2f}'.format(a, b))
elif a < b:
	print('{} is greater than {}'.format(b, a))
else:
	print('they are equal')

# + - * /
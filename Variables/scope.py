"""
@author - Ashwin Ganesh
Topic - Variable Scope
LEGB - Local, Enclosing, Global, Built-in
"""






var = 'global variable'

def outer():
	var = 'outer variable'

	def inner():
		nonlocal var
		var = 'inner variable'
		print(var)
	inner()
	print(var)
outer()
print(var)
"""
My answers to challenge problems


"""

# reverse a list

def reverse_lst(lst_in):
	new_lst = lst_in[::-1]
	print(new_lst)

# reverse_lst([1, 2, 3, 4, 5])


# list prime factors of a number in a list

def prime_factors(num):
	f = []
	i = 2
	while i <= num:
		while num % i == 0:
			f.append(i)
			num /= i
		print(i)
		i += 1
	print(f)
prime_factors(1324)


# take a list and create a string that separates all orginal elements by a comma and a space. the last element should have a comma, space, and an and

def lst_str(in_lst):
	ret = ""
	for i in range(len(in_lst)):
		ret += str(in_lst[i])
		if i < len(in_lst) - 2:
			ret += ", "
		elif i == len(in_lst) - 2:
			ret += ", and "
	print(ret)
# lst_str([1, 2, 3, 4, 5])


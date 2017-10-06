"""
Introduction to Lists

Lists are a built-in Class in python. Lists are referential structures that store sequences of objects

They are array-based sequences and are zero indexed, which means a list of length n has elements indexed from 0 to n-1

"""

#lst_name[start:stop:step]

# num_list = [0, 1, 2, 3, 4]

# print(num_list[1::2])
# count = 0
# for var in num_list:
# 	count = count + 1
# print(count)
# print(len(num_list))

# lst = ['a', 'b', 'c']
# final_str = ''
#
# for letter in lst:
# 	print(letter)
#
# for x in range(len(lst)):
# 	final_str += lst[x] + " "
# 	print(str(x) + " iteration")
#
# print(final_str)



# print(num_list[::2])
#
# name_list = ['Ashwin', 'Surag', 'Sahil', 'Chris']
#
# print(num_list + name_list)
#
# for num in num_list:
# 	print(num)

list_len = [1123123, 2, 3234, 43.0]
list_two = [2, 3, 5, 1]

list_len.sort()

print(list_len)

list_len += list_two
# print(list_len)

# list_len.insert(5, 3)
# list_len.append(100000)
# del list_len[-2:]
# print(list_len)
# def lst_len(lst):
# 	for i in list_len:
# 		count = count + 1\
# 	return(count)

# print("Swish! All money!!!!", len(list_len))




# name_list = []
#
# range_list = list(range(10))		#range(start, stop, step)
#
# print(range_list)


# len(lst) returns the number of elements in lst

# .insert(index, value) or .append(value) or .extend(sequence) methods can be used to build up a list. + or * operator can also be used

# lst[i] - accesses element at index i

# lst[start:stop:step] - returns elements from start up till stop with steps incrementing the index

# containment checks - in or not in



new_lst = sorted(list_len)
print(new_lst)

# .reverse()

# .sort()


# .index(value) / .remove() / var = lst.pop(index) / del lst[x:y]

# min(), max(), len(), sum()
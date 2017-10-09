"""
List Functions




"""


new_lst = ['words', "phrases", "numbers", 19, 27, -15.01, True, None, False]

new_lst.append("new value!!")

print(new_lst)

print(new_lst.insert(9, True))

print(len(new_lst))

print(new_lst.count(True))

del new_lst[:3]

new_lst.remove(None)

store_pop = new_lst.pop(3)
print(store_pop)

del new_lst[3:]

print(new_lst)

new_lst.sort()

print(new_lst)

new_lst.reverse()

print(new_lst)

"""
Built-in Python Operators - Comparison, Logical, Arithmetic, Assignment

Operators are constructs which can affect the value of its operands

Comparison Operators ( <, <=, >, >=, ==, !=)

Logical Operators ( and, or, not)

Arithmetic Operators ( +, -, *, /, //, %, ** )

"""

int1 = 42
int2 = 23

float1 = 42.0
float2 = 11.5

str1 = "Python is cool"
str2 = "It has so many uses and its ez"

bool1 = True
bool2 = False

#Python has a number of built-in operators

# Comparison Operators - compare the two operands and return a boolean value of True or False depending on the result of the Comparison
print(int1 > int2)
print(int1 == float1)
print(float2 < float1)
print(str1 > str2)


# Logical Operators - evaluates two boolean values and returns the resulting boolean value True or False
print(bool1 and bool2)
print(bool2 or bool1)
print(bool1 and True)
print(bool2 or False)


# Arithmetic Operators - perform some arithmetic operation involving two integer or float operands
print(int1 + float1)
print(str1 + ' ' + str2)

print(int1 - int2)
print(float2 - int2)
print(int2 - float2)

print(int1 * float1)
print(float2 * int2)
print(str1 * 3)

print(int1 / int2)
print(int1 // float1)
print(int1 % int2)

print(int1 ** 2)

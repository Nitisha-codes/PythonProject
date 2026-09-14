# Math Function
# built-in functions used to perform mathematical calculation

# round() : rounds a number to a specified number of decimals.

x = 3.14
new_x = round(x)
print(new_x)

# abs() : removes any negative sign, essentially telling you how far a number is from zero.

y = -4
new_y = abs(y)
print(new_y)

# pow() : raises a number to the power of another number (exponentiation).

exp = pow(2,3)
print(exp)

# max() :  returns the largest item in an iterable (like a list) or the largest of two or more arguments.

z = 7
max = max(x,y,z)
print(max)

# min() : returns the smallest item in an iterable (like a list) or the smallest of two or more arguments.

min = min(x,y,z)
print(min)

# Some special Math function


import math

print(math.pi)
print(math.e)
a = 9.9
print(math.ceil(a))
print(math.floor(a))
b = 8
print(math.sqrt(b))
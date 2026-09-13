# User input
# It enables the program to take data from the user
# "input()" is used
from Day01.variables import quantity

name = input("What is your name?:")
age = input("How old are you?:")

print(f"Hi {name}! You are {age} years old.")

# age = age + 1
# print(age)
# Error occurs if you run this syntax
# Because whatever is obtained from the user in the "input()" command, is stored as a string.

# Therefore, the correct syntax is


new_age = age + "1"
print(new_age)

# You can even make the integer a string by writing it inside "", but it won't be useful in mathematical calculation

age = int(age)
age = age + 1
print(age)

# Using typecasting, change the default string type into integer type to perform mathematical calculation.


# For simpler structure

sides = int(input("How many sides a polygon have?:"))
sides = sides + 1
print(f"There are {sides} in a polygon.")
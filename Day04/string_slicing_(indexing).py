# String slicing : a way to grab a specific piece (a "slice") of a string, similar to cutting a slice of bread from a whole loaf.
#                 indexing[] or slice[]


# Indexing : accessing a single, specific item from a collection (like a string, list, or tuple) by using its position number.
# [start:stop:step]

# start index : the exact position where your string slice begins
# stop index : stops right before that number, the character at the stop index is not included in your final result

name = "Nitisha Karna"
first_name = name[:7]
print(first_name)

# if nothing is written in the 'start' index then python defaulty understand it as 0 or the beginning of the string
# the 'start' index is inclusive and 'stop' index is exclusive

last_name = name[8:]
print(last_name)

# if nothing is written in the 'stop' index then python defaulty understand it as the end of the string


# step index : tells Python how many characters to jump forward each time

bleh = name[::3]
print(bleh)

# if 2 is written in 'step' index then it chooses the python jumps 2 character at a time

# Reversed string

reversed_name = name[::-1]
print(reversed_name)

# -1 in 'step index' changes the direction of your movement to backward (from right to left) instead of the normal forward direction (left to right).
# Positive step (1): Means "move 1 step forward" (Normal reading order).
# Negative step (-1): Means "move 1 step backward" (Reverse reading order).




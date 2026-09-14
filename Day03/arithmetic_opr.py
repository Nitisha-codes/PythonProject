# Arithmetic operator in Python
# special symbols used to perform common mathematical calcultion

# There is a difference in way we use arithmetic operators in Python and C
# In C, we did

# total = 0
# total = total + 1

# But now we do this instead.

# For addition

print("a = 0")
friends = 0
friends += 2
print("a += 2")
print(friends)

# For subtraction

print("a = 0")
num = 0
num -= 3
print("a -= 3")
print(num)

# For multiplication

print("a = 3")
mul = 3
mul *= 4
print("a *= 4")
print(mul)

# For division

print("a = 364")
div = 364
div /= 4
print("a /= 4")
print(div)

# For exponentiation

print("a = 5")
exp = 5
exp **= 2
print("a **= 2")
print(exp)

# In QBASIC, we have MOD for remainder
# In Python,

print("a = 5")
rem = 5
rem = rem % 2
print("a %= 2")
print(rem)
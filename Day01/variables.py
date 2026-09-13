# This is my 1st Python program and its about me.

# Using print statement

print("Hi! I am Nitisha Karna.")
print("I study in Grade 12.")
print("I love watching anime.")
print("My Favorite anime is Haikyuu!!.")

# Variables
# A container for value (string, integer, float, boolean)

# Strings

college_name = "Sagarmatha"
print(college_name)

fav_food = "Dosa"
fav_color = "Black"
current_anime = "One piece"
email = "nitishakarna1@gmail.com"

# String Variables using F-string

print(f"I study in {college_name}.")
print(f"You love eating {fav_food}.")
print(f"You look great in {fav_color}.")
print(f"You are currently watching {current_anime}.")
print(f"Your gmail is : {email}.")


# Integer

age = 16
quantity = 4
num_of_stds = 15

# Integer Variables in F-string

print(f"You are {age} years old.")
print(f"You bought {quantity} items.")
print(f"Your class has {num_of_stds} students.")

#Float

price = 49.89
length = 7.5
weight = 52.97
gpa = 3.93

# Float Variables in F-string

print(f"The price is ${price}.")
print(f"The pen is {length}mm long.")
print(f"You are {weight} kilograms.")
print(f"My GPA is {gpa}.")


# Boolean

is_online = False
is_logged_in = True

# Boolean Variables in F-string

print(f"Are you logged in? : {is_logged_in}.")
print(f"Are you online? : {is_online}.")

# Use of If statement (snippet)

if is_logged_in:
    print("You are logged in.")

else:
    print("You are NOT logged in.")

if is_online:
    print("You are online.")

else:
    print("You are NOT online.")



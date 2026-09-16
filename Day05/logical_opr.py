# Logical operator : keywords used to combine or modify conditional statements, returning a Boolean value (True or False) based on the truth evaluation of those conditions.
# 'and' and 'or' operator

# 'and' operator

marks = int(input("Enter your marks : "))

if marks >= 90 and marks <= 100:
    print("You got an A+!")
    print("Congrats for your outstanding perfomance!")
elif marks >= 80 and marks < 90:
    print("You got an A!")
    print("Congrats for your excellent perfomance!")
elif marks >= 70 and marks < 80:
    print("You got a B+!")
    print("Congrats for very good perfomance!")
elif marks >= 60 and marks < 70:
    print("You got a B!")
    print("Congrats for your good perfomance!")
elif marks >= 50 and marks < 60:
    print("You got a C+!")
    print("Your performance was above average!")
elif marks >= 40 and marks < 50:
    print("You got a C!")
    print("Your performance was average!")
elif marks >= 30 and marks < 40:
    print("You got a D!")
    print("Sorry. Your performance was below average!")
elif marks >= 20 and marks < 30:
    print("You got an E!")
    print("Sorry. Your performance was insufficient!")
else:
    print("You are not graded!")
    print("Sorry. You failed!")
    print("Better luck next time!")





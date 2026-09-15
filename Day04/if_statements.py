# if statement : executes a specific block of code only if a specified condition is true.

marks =  int(input("Enter your marks: "))

if marks >= 90:
    print("Congrats! You got an A.")
elif marks > 80 :
    print("You got a B!")
elif marks > 70 :
    print("You got a C!")
else:
    print("Sorry, Better Luck Next time!")


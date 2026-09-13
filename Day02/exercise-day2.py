# Exercise-1
# Calculate area of rectangle
# Area = Length * breadth

length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))
area = length * breadth
print(f"The area of rectangle is {area} cm^2.")

# Exercise-2
# A Shopping Cart program

item = input("What would you like to buy today?: ")
price = float(input("How much does it costs?: "))
quantity = int(input("How many would you like?: "))
total = price * quantity
print(f"You ordered {quantity} {item}/s.")
print(f"Your total is: ${total}")
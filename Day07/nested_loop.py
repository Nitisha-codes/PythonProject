# Nested loop : a loop placed inside the body of another loop
# The 'inner loop' will finish all of it's iterations before finishing one iteration of the 'outer loop'

# Creating a 4 sided polygon using a symbol

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter the symbol: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end=" ")

    print()




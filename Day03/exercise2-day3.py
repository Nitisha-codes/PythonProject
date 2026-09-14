# Calculate the area of the circle
# A = pi * r ^ 2

import math
r = float(input("Enter the radius of the circle: "))
r **= 2
area = math.pi *r
print(f"The area of the circle is {round(area,3)}cm².")
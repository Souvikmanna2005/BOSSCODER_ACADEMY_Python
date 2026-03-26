'''Calculate the area and circumference of a circle given its 
radius'''

#Area of a Circle [A = πr**2]
#Circumference of a circle [C = 2πr]
# π = math.pi

import math

radius = float(input("Enter radius: "))

area = math.pi * radius * radius
circumference = 2 * math.pi * radius

print("Area:", area)
print("Circumference:", circumference)
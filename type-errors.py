# Area Calculator 📏

import math

base = 20
height = 30
area = int(base * height / 2) # added int() to convert the result to an integer

print("The triangle area is", area)

length = 2
width = 12
area = int (length * width) # added int() to convert the result to an integer

print("The rectangle area is", area)  # Added a comma after the string

radius = 36
area = math.pi * radius * radius

print("The circle area is", area)

"""
This script demonstrates the usage of list comprehension to double the positive numbers and triple the negative numbers in a given list.
"""

numbers = [2, -1, 79, 33, -45]
doubled = [num * 2 if num < 0 else num * 3 for num in numbers]
print(doubled)
numbers = [1, -1, 79, 33, -45]
doubled = [num * 2 if num < 0 else num * 3 for num in numbers ]
print(doubled)
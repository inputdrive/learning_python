'''
Write a new function called get_length() that takes a string as an input and returns the number of characters in that string. Do this by iterating through the string. Do not use the len() function!
'''

def get_length(string):
    count = 0
    for char in string:
        count += 1
    return count
print(get_length("test"))
"""
This script takes a string input from the user and reverses it
using Python's efficient slicing technique.
"""
# Prompt the user for input. No need for explicit str() cast as input() returns a string by default.
my_string = input("Enter any string: ")

# The [::-1] syntax creates a slice of the string starting from the end
# and moving backwards to the start with a step of -1.
reversed_string = my_string[::-1]

# Output the result to the console
print("Reversed string:", reversed_string)
"""
This script evaluates whether a user-provided integer is greater than 7.
It demonstrates basic conditional logic and function calls in Python.
"""

def is_bigger_than(number):
    # Compare the input number to the threshold value of 7
    if number > 7:
        # If the condition is met, print True as a string
        print("True")
    else:
        # If the number is 7 or less, print False as a string
        print("False")

# Get user input and convert the string input to an integer
user_input = int(input("Enter a number: "))

# Execute the function with the processed user input
is_bigger_than(user_input)

"""
This script checks if a user-provided integer is divisible by five.
It utilizes the modulo operator to determine if there is a remainder
when the number is divided by 5.
"""

def is_divisible_by_five(number):
    # Use the modulo operator (%) to check the remainder of division by 5
    if number % 5 == 0:
        # If the remainder is 0, the number is divisible by 5
        print("True")
    else:
        # If there is any remainder, the number is not divisible by 5
        print("False")

# Get input from the user and cast it to an integer
user_input = int(input("Enter a number: "))
# Call the function with the user's input
is_divisible_by_five(user_input)

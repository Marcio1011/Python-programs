"""
This script prints a sequence of numbers from the user's input down/up to zero.
It handles both positive and negative integers by adjusting the range step.
"""

# Get user input and convert to integer
try:
    user_input = int(input("Input a number: "))

    if user_input > 0:
        # Range parameters: (start, stop, step)
        # We start at user_input, stop at 0, and move by -1 each time.
        for num in range(user_input, 0, -1):
            print(num)

    elif user_input < 0:
        # We start at user_input, stop at 0, and move by +1 each time.
        for num in range(user_input, 0, 1):
            print(num)

    else:
        print("The number is already zero.")

except ValueError:
    print("Please enter a valid whole number.")







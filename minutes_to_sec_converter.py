"""
This script provides a utility to convert time duration from minutes to seconds.
It takes a numeric input from the user and outputs the equivalent value in seconds.
"""
def converter(minutes):
    # Multiplication by 60: Each minute consists of 60 seconds
    seconds = minutes * 60

    # Output the result using a formatted print statement
    print("The number of seconds is:", seconds)

# Main Execution Flow:
# Get user input and cast the string input to an integer to allow mathematical operations
user_input = int(input("Enter the number of minutes: "))

# Execute the function passing the validated user input as an argument
converter(user_input)

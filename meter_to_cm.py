def conver_to_cm(meters):
    # Multiplication by 60: Each minute consists of 60 seconds
    cm = meters * 100

    # Output the result using a formatted print statement
    print("The number of cm is:", cm)

# Main Execution Flow:
# Get user input and cast the string input to an integer to allow mathematical operations
user_input = int(input("Enter the number of meters: "))

# Execute the function passing the validated user input as an argument
conver_to_cm(user_input)
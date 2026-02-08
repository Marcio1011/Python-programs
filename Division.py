# This script prompts the user for two numbers and
# calculates their integer and float divisions.

# Request the first integer from the user and convert the string input to an int
first_number = int(input("Enter the first number: "))

# Request the second integer from the user and convert the string input to an int
second_number = int(input("Enter the second number: "))

#The result of the integer division
Integer_division = int(first_number / second_number)
#The result of the float division
float_division = float(first_number / second_number)

print(Integer_division)
print(float_division)

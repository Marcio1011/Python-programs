
# This script captures an integer from the user and applies
# a series of conditional checks to determine if the number is "Weird" or "Not weird"
# based on its parity (even/odd) and specific ranges.

# Prompt the user for input, convert the string to an integer, and store it in 'user_number'
user_number = int(input("Enter a number: "))

# Check if the number is even AND falls within the inclusive range of 2 to 5
if user_number % 2 == 0 and 2 <= user_number <= 5:
    # If both conditions are met, the number is categorized as "Not weird"
    print("Not weird")
# If the number is either odd OR outside the 2-5 range, proceed to this block
else:
    # Check if the number is even AND falls within the range of 6 up to 20 (not including 20)
    if user_number % 2 == 0 and 6 <= user_number < 20:
        # If both conditions are met, the number is categorized as "Weird"
        print("Weird")

# Check if the number is even AND is 20 or greater
if user_number % 2 == 0 and user_number >= 20:
        # If even and 20+, it is categorized as "Not Weird"
        print("Not Weird")
# If the number is odd OR is less than 20, proceed to this block
else:
    # Check specifically if the number is odd (remainder is not 0 when divided by 2)
    if user_number % 2 != 0:
        # Every odd number, regardless of range, is categorized as "Weird"
        print("Weird")

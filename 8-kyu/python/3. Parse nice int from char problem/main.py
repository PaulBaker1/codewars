# You ask a small girl,"How old are you?" She always says,
#  "x years old", where x is a random number between 0 and 9.

# Write a program that returns the girl's age (0-9) as an integer.

# Assume the test input string is always a valid string. For example,
#  the test input may be "1 year old" or "5 years old". The first character in the string is always a number.

def extract_age(input_str):
    # Extract the first character of the string, which is a digit
    age_char = input_str[0]

    # Convert the character to an integer and return
    return int(age_char)

# Example usage
input1 = "3 years old"
input2 = "7 years old"


age1 = extract_age(input1)
age2 = extract_age(input2)

print("Extracted Age 1:", age1)  # Output: Extracted Age 1: 3
print("Extracted Age 2:", age2)  # Output: Extracted Age 2: 7
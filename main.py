# VERGEL, CHEAN BERNARD V.
# VERGEL, CHEAN BERNARD V.
# LAB1 NO2
# DUPLICATE REMOVER

# Import the remove_duplicates
from duplicate_remover import remove_duplicates

# Get the number of strings as input
n = int(input("Enter the number of strings that you wanted to input: "))

# Initialize a list to store the input strings
input_strings = []

# Loop to get N strings from the user
for i in range(n):
    input_str = input(f"Enter string {i + 1}: ")
    input_strings.append(input_str)

# Iterate through the list of input strings and remove duplicates
for input_str in input_strings:
    result_str = remove_duplicates(input_str)
    print(f"Result: {result_str}")
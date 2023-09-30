# VERGEL, CHEAN BERNARD V.
# LAB1 NO2
# DUPLICATE REMOVER

# Import the remove_duplicates
from duplicate_remover import RemoveDuplicates

# Create a header.
import pyfiglet
print("")
print("=" * 80)
print("")
welcome = pyfiglet.figlet_format("Welcome to my space".center(57, " "), font = "digital" )
print(welcome)
print("")
print("=" * 80)
print("\033[33mHi, I am Chean Bernard V. Vergel a second year college student at Polytechnic University of the Philippines.\033[0m")
print("")

# Ask for the name of the user.
name_of_user = input("\033[35mHow about you what is your name?\U0001F917\033[0m ")
print("")
print("=" * 80)
print("")

# Make a greeting message for the user.
print("\033[23mGood day,",name_of_user,"this program will ask you to input some words and delete numbers and the letters that are being repeated.\033[0m")
print("")


# Ask if the user wants to continue.
agreement = str(input("\033[96mDo you want to continue answering this program? Type \033[0m\033[40m\033[33mYES\033[0m\033[96m if you want to continue and type \033[0m\033[40m\033[33mNO\033[0m\033[96m if not.\033[0m "))
print("")
print("=" * 80)
print("")

# If user wants to continue, ask the user to input characters.
if agreement.upper() == "YES":


# Get the number of strings as input
    n = int(input("Enter the number of strings that you want to input: "))

# Initialize a list to store the input strings
    input_strings = []

# Loop to get N strings from the user
for i in range(n):
    input_str = input(f"Enter string {i + 1}: ")
    duplicate_removed = RemoveDuplicates.remove_chars(input_str)
    input_strings.append(input_str)
    input_strings.append(duplicate_removed.replace(" ", ""))

# Iterate through the list of input strings and remove duplicates
for input_str in input_strings:
    print(f"Result: {input_str}")
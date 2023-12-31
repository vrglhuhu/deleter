# VERGEL, CHEAN BERNARD V.
# LAB1 NO2
# DUPLICATE REMOVER

# Create class called RemoveDuplicates
class RemoveDuplicates:

    @staticmethod
    # Function to remove duplicate characters from a string
    def remove_chars(input_str):
        # Create an empty set to keep track of unique characters
        unique_chars = set()

        # Create an empty string to store the result
        result_str = ""

        # Iterate through each character in the input string
        for char in input_str:
            # Check if the character is not in the unique_chars set, not a digit,
            # and the count of the character in the input_str is 1
            if not char.isdigit() and input_str.count(char) == 1 and char not in unique_chars:
                # Add the character to the unique_chars set
                unique_chars.add(char)
                # Append the character to the result string
                result_str += char

        # use join method to return the result
        return result_str
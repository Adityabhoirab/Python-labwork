#Write a Program to Accept a String and Replace All Spaces with Hash (#) Symbol

def replace_spaces_with_hash(s):
    return s.replace(' ', '#')


# Input string
input_string = input("Enter a string: ")

# Replace spaces with hash symbol
modified_string = replace_spaces_with_hash(input_string)
print(f"Modified string: {modified_string}")

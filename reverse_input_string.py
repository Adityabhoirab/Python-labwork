#Write a Program to Reverse a Given String

def reverse_string(s):
    return s[::-1]


# Input string
input_string = input("Enter a string: ")

# Reverse the string
reversed_string = reverse_string(input_string)
print(f"Reversed string: {reversed_string}")

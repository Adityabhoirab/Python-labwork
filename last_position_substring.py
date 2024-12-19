#Write a Program to Find the Last Position of a Given Substring
def last_position_of_substring(string, substring):
    return string.rfind(substring)


# Input string and substring
main_string = input("Enter the main string: ")
sub_string = input("Enter the substring to find: ")

# Find last position of substring
position = last_position_of_substring(main_string, sub_string)

if position != -1:
    print(f"The last position of '{sub_string}' is: {position}")
else:
    print(f"'{sub_string}' not found in the string.")

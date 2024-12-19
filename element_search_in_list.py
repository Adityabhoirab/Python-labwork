#WAP to search a element in list and display proper result if found.

# Function to search for an element in the list
def search_element(lst, element):
    # Check if the element is in the list
    if element in lst:
        return f"Element {element} found in the list."
    else:
        return f"Element {element} not found in the list."


# Example list
my_list = [12, 7, 45, 3, 19, 56, 23, 88]

# Element to search
element_to_search = 19

# Call the function and store the result
result = search_element(my_list, element_to_search)

# Output the result
print(result)

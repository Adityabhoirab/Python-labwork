# Function to remove duplicates and sort the list
def remove_duplicates_and_sort(lst):
    # Convert the list to a set to remove duplicates, then back to a list
    unique_lst = list(set(lst))
    
    # Sort the list in ascending order
    unique_lst.sort()
    
    # Return the sorted list with duplicates removed
    return unique_lst


# Example list with duplicate elements
my_list = [12, 7, 45, 3, 19, 45, 7, 56, 88, 3]

# Call the function to remove duplicates and sort the list
result = remove_duplicates_and_sort(my_list)

# Print the result
print("List after removing duplicates and sorting:", result)

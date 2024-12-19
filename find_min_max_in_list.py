#WAP to find minimum and Maximum element of a list.
# Function to find the minimum and maximum elements in a list
def find_min_max(lst):
    # Check if the list is empty
    # If the list is empty, we return None for both minimum and maximum
    if not lst:
        return None, None
    
    # Initialize the first element of the list as both the minimum and maximum
    min_element = lst[0]  # Set the first element as the initial minimum
    max_element = lst[0]  # Set the first element as the initial maximum

    # Iterate through the list to find the min and max elements
    for num in lst:
        # If the current element is smaller than the current min, update the min
        if num < min_element:
            min_element = num
        
        # If the current element is larger than the current max, update the max
        if num > max_element:
            max_element = num
    
    # Return the final minimum and maximum values as a tuple
    return min_element, max_element


# Example list
my_list = [12, 7, 45, 3, 19, 56, 23, 88]

# Call the function to get the minimum and maximum values
min_value, max_value = find_min_max(my_list)

# Output the results
print("Minimum element:", min_value)  # Print the minimum element found
print("Maximum element:", max_value)  # Print the maximum element found

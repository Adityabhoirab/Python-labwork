#WAP to find second smallest element of a list.

# Function to find the second smallest element in the list
def second_smallest(lst):
    # Check if the list has at least two elements
    if len(lst) < 2:
        return None  # Return None if there aren't enough elements

    # Initialize the first and second smallest values
    first_smallest = second_smallest = float('inf')  # Set both to infinity initially

    # Loop through the list to find the first and second smallest
    for num in lst:
        if num < first_smallest:
            # Update both first and second smallest
            second_smallest = first_smallest
            first_smallest = num
        elif num < second_smallest and num != first_smallest:
            # Update second smallest only if the current num is smaller than second_smallest but not equal to first_smallest
            second_smallest = num
    
    # If second smallest is still infinity, it means there was no valid second smallest
    if second_smallest == float('inf'):
        return None
    
    return second_smallest


# Example list
my_list = [12, 7, 45, 3, 19, 56, 23, 88]

# Get the second smallest element
second_min = second_smallest(my_list)

# Output the result
if second_min is None:
    print("No second smallest element found.")
else:
    print("Second smallest element:", second_min)

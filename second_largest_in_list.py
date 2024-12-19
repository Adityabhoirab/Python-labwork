#Write a Python program to find the second largest number in a list.
my_list = [10, 20, 30, 5, 15]

# Sort the list in descending order
my_list.sort(reverse=True)

# Print the sorted list
print("Sorted list in descending order:", my_list)

# Check if there are at least two elements
if len(my_list) > 1:
    # Print the second largest element
    print("Second largest number from the list:", my_list[1])
else:
    print("List does not have a second largest number.")

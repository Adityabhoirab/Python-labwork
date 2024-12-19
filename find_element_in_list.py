#wap to search particular element in list 
# List of fruits
fruits = ["apple", "banana", "cherry", "date"]

# Target fruit to search for
target = "banana"

# Traverse the list of fruits
for fruit in fruits:
    # Check if the current fruit matches the target
    if fruit == target:
        # If match is found, print a message
        print("Found it!")
        # Exit the loop since we found the target fruit
        break

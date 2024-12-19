#WAP to print triangular  pattern
# Outer loop for the number of rows (1 to 4)
for i in range(1, 5):
    # First part: print stars (*)
    for j in range(1, i + 1):
        print("*", end=" ")

    # Adding spaces to separate the two parts
    print(" " * (5 - i) * 2, end="")

    # Second part: print numbers
    for j in range(1, i + 1):
        print(j, end=" ")

    # Adding spaces to separate the numbers
    print(" " * (5 - i) * 2, end="")

    # Third part: print the same number i, i times (like 'i i i i')
    for j in range(i):
        print(i, end=" ")

    # Move to the next line after completing the row
    print()

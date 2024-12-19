#Q.4)Create a while loop to print the Fibonacci series up to n terms.

# Get the number of terms from the user
n = int(input("Enter the number: "))

# Initialize the first two Fibonacci numbers
a, b = 0, 1
sum1 = 0

# Print Fibonacci series using while loop
while sum1 < n:
    print(a, end=" ")
    a, b = b, a + b  # Update to the next Fibonacci numbers
    sum1 += 1

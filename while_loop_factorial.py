#Q.1)WAP to get factorial of a number using while loop.
# Get input
num1 = int(input("Enter a number: "))

# Initialization 
result = 1
i = 1

# Calculate factorial
while i <= num1:
    result *= i  # multiply result by i
    i += 1  # increment i by 1

# Print the result
print(f"The factorial of {num1} is {result}.")

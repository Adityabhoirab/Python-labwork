#Q.2)WAP to get factorial of a number

# Taking user input
num = int(input("Enter a number to calculate its factorial: "))

# initialization fac as 1 
fac= 1

# Using for loop to calculate factorial
for i in range(1, num + 1):
    fac *= i  # Multiply fac by i in each iteration

# Display the result
print(f"The factorial of {num} is {fac}")

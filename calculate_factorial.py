#Q.1)WAP to get factorial of a number using function

# Taking user input for the number to calculate its factorial
num = int(input("Enter a number to calculate its factorial: "))

# Function to calculate the factorial of a given number
def fact(num):
    # Initialize the factorial result as 1 
    fac = 1

    # Using a for loop to calculate factorial
    # The loop runs from 1 to the given number (num), multiplying each number with fac
    for i in range(1, num + 1):
        fac *= i  # Multiply fac by i in each iteration to calculate the factorial

    # Display the result after the loop is finished
    print(f"The factorial of {num} is {fac}")

# Call the function to calculate and display the factorial
fact(num)


#Q.2)WAP to find maximum among two number

def find_max(num1, num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else:
        return "Both numbers are equal"

# Get user input for the two numbers
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

# Call the function to find the maximum number
result = find_max(number1, number2)

# Output the result
print(f"The result is: {result}")


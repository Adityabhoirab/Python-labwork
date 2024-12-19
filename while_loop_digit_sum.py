#Q.3)Write a while loop to calculate the sum of digits of a given number.

# Get input from the user
num = int(input("Enter a number: "))

#Initialize sum variable
sum1 = 0

#Calculate the sum of digits using a while loop
while num > 0:
    sum1 += num % 10  # Add the last digit to the sum
    num //= 10  # Remove the last digit

#Print the result
print("The sum of the digits is:",sum1)




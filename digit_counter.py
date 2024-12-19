#Q.2)Write a while loop that counts the number of digits in a given number
#Get input from the user
num = int(input("Enter a number: "))

# Initialization 
count = 0
#Count digits using a while loop
while num > 0:
    count += 1  # Increase by 1
    num //= 10  # Remove  last digit

# Print the result
print("The number of digits is:", count)

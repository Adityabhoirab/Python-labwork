#Q.4)WAP to get table of a number using function
# Function to print the multiplication table
def print_table(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

# Get user input for the number
num = int(input("Enter a number to get the table: "))

# Call the function to print the table
print_table(num)


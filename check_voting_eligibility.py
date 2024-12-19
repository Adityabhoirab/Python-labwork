#Q.3)WAP to check whether person can vote or not using function

# Taking user input for the age
age = int(input("Enter your age: "))  # Prompting the user to enter their age. We use int() to convert input into an integer.

# Defining a function to check voting eligibility
def vote(age):
    # Inside the function, check if the age is 18 or more
    if age >= 18:
        # If the age is 18 or greater, the person is eligible to vote
        print("You are eligible to vote.")
    else:
        # If the age is less than 18, the person is not eligible to vote
        print("You are not eligible to vote.")

# Calling the function with the user's age as the argument
vote(age)  #This line calls the vote() function and passes the entered age to it


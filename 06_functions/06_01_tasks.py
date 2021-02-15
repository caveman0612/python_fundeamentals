'''

Write a script that completes the following tasks.

'''

# define a function that determines whether the number is divisible by 4 or 7 and returns a boolean

# define a function that determines whether a number is divisible by both 4 and 7 and returns a boolean

# take in a number from the user between 1 and 1,000,000,000

# call your functions, passing in the user input as the arguments, and set their output equal to new variables 

# print your new variables to display the results

def divisible4or7(number):
    if number % 4 == 0 or number % 7 == 0:
        return True
    else:
        return False

def divisible4and7(number):
    if number % 4 == 0 and number % 7 == 0:
        return True
    else:
        return False


users_number = int(input("input number"))
print(divisible4or7(users_number))
print(divisible4and7(users_number))


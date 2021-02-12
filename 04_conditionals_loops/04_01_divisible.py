'''
Write a program that takes a number between 1 and 1,000,000,000
from the user and determines whether it is divisible by 3 using an if statement.
Print the result.

'''

num = input("input number here: ")
num = int(num)
if num % 3 == 0:
    print("it is divisible by 3")
else:
    print("it is not divisible by 3")
'''
Create a script that asks a user to input an integer, checks for the
validity of the input type, and displays a message depending on whether
the input was an integer or not.

The script should keep prompting the user until they enter an integer.

'''

while True:
    try:
        num1 = input("input integer")
        num = int(num1)
        if not isinstance(num, int):
            print("that is not an integer")
        else:
            print("thank you for the integer")
    except ValueError:
        print("that is not an integer")



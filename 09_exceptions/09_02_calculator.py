'''
Write a script that takes in two numbers from the user and calculates the quotient. Using a try/except,
the script should handle:

- if the user enters a string instead of a number
- if the user enters a zero as the divisor

Test it and make sure it does not crash when you enter incorrect values.

'''

while True:
    try:
        num = int(input("input num"))
        divisor = int(input("input divisor"))
        print(num/divisor)
    except ZeroDivisionError:
        print("Sorry you can't divide by zero")
    except ValueError:
        print("Sorry cant divide by strings")
    except Exception as e:
        print(f"{e} has occurred")

# num = int(input("input num"))
# divisor = int(input("input divisor"))
# print(num/divisor)
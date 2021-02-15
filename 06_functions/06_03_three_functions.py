'''
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.

'''
def plus(num1, num2):
    return num1 + num2

def multiple(num1, num2):
    return num1 * num2

def power(num1, num2):
    return num1 ** num2

print(power(plus(2, 2), multiple(2, 2)))
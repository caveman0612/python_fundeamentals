'''
Write a script that prints out all the squares of numbers from 1- 50

Use a for loop that demonstrates the use of the range function.

'''

for i in range(1, 51):
    for x in range(1, i):
        if x * x == i:
            print(i)

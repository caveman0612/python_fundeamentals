'''
Write a script that takes three strings from the user and prints them together with their length.

Example Output:

5, hello
5, world
9, greetings

CHALLENGE: Can you edit to script to print only the string with the most characters? You can look
           into the topic "Conditionals" to solve this challenge.

'''

first = input("first string")
second = input("second string")
third = input("third string")

print(len(first))
print(len(second))
print(len(third))

if first > second and third:
    print("first")
if second > first and third:
    print("second")
if third > second and first:
    print("third")
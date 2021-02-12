'''
Write a script that takes a string from the user and creates a dictionary of letter that exist
in the string and the number of times they occur. For example:

user_input = "hello"
result = {"h": 1, "e": 1, "l": 2, "o": 1}

'''

input_string = input("input string")
dict_letters = {}

for letter in input_string:
    if letter not in dict_letters:
        dict_letters[letter] = 1
    else:
        dict_letters[letter] += 1

del dict_letters[" "]
print(dict_letters)
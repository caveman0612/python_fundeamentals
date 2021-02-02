'''
Write a script that prints the total number of vowels that are used in a user-inputted string.


CHALLENGE: Can you change the script so that it counts the occurrence of each individual vowel
           in the string and print a count for each of them?

'''

word = input("input word")
vowels = "aeiou"
counter = 0
dictionary = {}
for letter in word:
    if letter in vowels:
        counter += 1
        if letter not in dictionary:
            dictionary[letter] = 1
        else:
            dictionary[letter] += 1
print(counter)
print(dictionary)
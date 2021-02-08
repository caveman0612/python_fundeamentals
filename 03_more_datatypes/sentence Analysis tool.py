# Write a script that takes a sentence from the user and returns:
#
# the number of lower case letters
# the number of uppercase letters
# the number of punctuations characters
# the total number of characters
# Use a dictionary to store the count of each of the above.
#
# Note: ignore all spaces.
alphabet = "abcdefghijklmnopqrstuvwxyz"
caps = alphabet.upper()
punctuations = "!.,\"?()*:;"
sentence = input("input sentence")
# sentence = "I love to work with dictionaries!"
sentence = sentence.replace(" ", "")
lower = 0
upper = 0
punct = 0
total = 0
for letter in sentence:
    total += 1
    if letter in alphabet:
        lower += 1
    if letter in caps:
        upper += 1
    if letter in punctuations:
        punct +=1

print(lower, upper, punct, total)

print(sentence)


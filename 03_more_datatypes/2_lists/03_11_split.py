'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''

string = "hello aloha bye hello  hello bye"

new_string = string.split()
print(new_string)
new_dict = {}

for word in new_string:
    if word not in new_dict:
        new_dict[word] = 1
    else:
        new_dict[word] += 1

a = sorted(new_dict.items(), key=lambda x: x[0], reverse=True)
for key, num in a:
    print(key)
    break



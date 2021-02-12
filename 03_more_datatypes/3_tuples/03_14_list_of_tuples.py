'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''

sentence = input("input sentence to parse")

# sentence = "hello world is magical!"
sentence = sentence.split()
result_list = []
for word in sentence:
    list_word = []
    for letter in word:
        list_word.append(letter)
    tuple_word = tuple(list_word)
    result_list.append(tuple_word)
print(result_list)
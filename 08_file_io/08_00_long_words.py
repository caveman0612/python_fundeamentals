'''
Write a program that reads words.txt and prints only the words
with more than 20 characters (not counting whitespace).
'''
with open("words.txt", "r") as sout:
    words = sout.read()

    print(type(words))
    words = words.split("\n")
    print(type(words))
    for word in words:
        if len(word) > 20:
            print(word)

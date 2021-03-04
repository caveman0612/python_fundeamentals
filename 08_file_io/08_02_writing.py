'''
Write a script that reads in the contents of words.txt and writes the contents in reverse
to a new file words_reverse.txt.
'''

with open("words.txt", "r") as forw:
    forward = forw.read()
    reverse = forward[::-1]
    with open("words_reverse.txt", "w") as revs:
        revs.write(reverse)
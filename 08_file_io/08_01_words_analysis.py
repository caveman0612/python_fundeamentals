'''
Write a script that reads in the words from the words.txt file and finds and prints:

1. The shortest word (if there is a tie, print all)
2. The longest word (if there is a tie, print all)
3. The total number of words in the file.


'''
with open("words.txt", "r") as sout:
    words = sout.read()
    words = words.split("\n")
    smallest = ""
    small_list = []
    longest = ""
    long_list = []
    total = 0
    for word in words:
        total +=1
        if len(word) <= 0:
            continue
        if len(smallest) == 0:
            smallest = word
            small_list.append(word)
            longest = word
            long_list.append(word)
            continue
        if len(word) <= len(smallest):
            if len(word) < len(smallest):
                smallest = word
                small_list.clear()
                small_list.append(word)
            elif len(word) == len(smallest):
                small_list.append(word)
        if len(word) >= len(longest):
            if len(word) > len(longest):
                longest = word
                long_list.clear()
                long_list.append(word)
            elif len(word) == len(longest):
                long_list.append(word)

    if len(small_list) > 1:
        smallest = small_list
    if len(long_list) > 1:
        longest = long_list
    print(f"this file containes {total} of words and the shortest word/s are {smallest[:5]}... and the longest are {longest}")
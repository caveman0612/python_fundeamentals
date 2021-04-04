def reverseWordsInString(string):
    string += " "
    temp = ""
    l_words = []
    for letter in string:
        temp += letter
        if letter == " ":
            l_words.append(temp)
            temp = ""
    new_words = []
    for word in l_words[::-1]:
        new_words.append(word)
    new_words = "".join(new_words)
    if new_words[-1] == " ":
        new_words = new_words[:-1]


    return new_words

    # string = string.split()
    # string.reverse()
    # string = " ".join(string)
    # return string



string = "AlgoExpert is the best!"
print(reverseWordsInString(string))
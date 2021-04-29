def runLengthEncoding(string1):
    answer = []
    current = ""
    counter = 1
    for letter in string1:
        if current == "":
            current = letter
        else:
            if letter == current:
                counter += 1
                if counter == 9:
                    answer.append(f"9{current}")
                    current = ""
                    counter = 1
            elif current != letter:
                answer.append(f"{counter}{current}")
                counter = 1
                current = letter
    answer.append(f"{counter}{current}")
    string3 = "".join(answer)
    return string3


string2 = "AAAAAAAAAAAAAABBBCCCCDD"
print(runLengthEncoding(string2))



    ###
    # go through each element in string
    # if element is current
    # add to counter
    # if element not current
    #     add counter and current to answer and reset counter and current
    # if counter == 9 reset
        # add current plus counter and reset counter and current and a


    ###


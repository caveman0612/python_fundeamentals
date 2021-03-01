def patternMatcher(pattern, string):
    swtiched = False
    #make x the first letter
    if pattern[0] == "y":
        new_pattern = pattern
        new_pattern = new_pattern.replace("x", "a")
        new_pattern = new_pattern.replace("y", "x")
        new_pattern = new_pattern.replace("a", "y")
        swtiched = True
    else:
        new_pattern = pattern
    #get number of xs and ys
    num_of_x = new_pattern.count("x")
    num_of_y = new_pattern.count("y")
    #find first y position if y exists
    if num_of_y != 0:
        i_of_y = new_pattern.index("y")
    #interate through potential lengths of x and calculate len of y
    if num_of_y > 0:
        for i in range(1, len(string)+1):
            len_of_y = (len(string) - (i * num_of_x)) / num_of_y
            if len_of_y % 1 != 0:
                continue
            else:
                len_of_y = int(len_of_y)
            x = string[:i]
            start_y = i * i_of_y
            y = string[start_y:(start_y + len_of_y)]
            l_pattern = list(new_pattern)
            for index, item in enumerate(l_pattern):
                if item == "x":
                    l_pattern[index] = x
                elif item == "y":
                    l_pattern[index] = y
            l_pattern = "".join(l_pattern)
            if l_pattern == string:
                if swtiched:
                    return [y, x]
                return [x, y]
    if num_of_y == 0:
        for i in range(1, len(string)):
            x = string[:i]
            l_pattern = new_pattern.replace("x", x)
            if l_pattern == string:
                if swtiched:
                    return["", x]
                return [x, ""]
    return []


    #check to see if y is vaild

    # and replace pattern with potential x and y and check if it matches the string


# pattern = "xxyxxy"
# pattern = "yyxyyx"
# string = "gogopowerrangergogopowerranger"

# pattern = "xyxxy"
# pattern = "yxyyx"
# string = "gopowerrangergogopowerranger"

# pattern = "xxxx"
pattern = "yyyy"
string = "testtesttesttest"


print(patternMatcher(pattern, string))

# def match_section(part, whole):
#     counter = 0
#     for index, letter in enumerate(whole):
#         if letter == part[0]:
#             section = whole[index: index + len(part)]
#             if section == part:
#                 counter += 1
#     return counter
#
# def patternMatcher(pattern, string):
#     # variables
#     x = []
#     y = []
#     num_x = pattern.count("x")
#     num_y = pattern.count("y")
#     counter = 0
#     # loop to remove words from string
#     while len(string) != 0:
#         word = ""
#         if pattern[0] == "x":
#             total = num_x
#             use = "x"
#         else:
#             total = num_y
#             use = "y"
#
#         for letter in string:
#             word += letter
#             count = string.count(word)
#             if count == total:
#                 if use == "x":
#                     x.append(word)
#                 else:
#                     y.append(word)
#         word = ""
#         if use == "x":
#             if len(x) == 1:
#                 string = string.replace(x[0], "")
#                 pattern = pattern.replace("x", "")
#                 for letter in string:
#                     word += letter
#                     count = string.count(word)
#                     if count == num_y:
#                         if use != "x":
#                             x.append(word)
#                         else:
#                             y.append(word)
#             else:
#                 for item in x:
#                     string = string.replace(x[0], "")
#                     pattern = pattern.replace("x", "")
#                     for letter in string:
#                         word += letter
#                         count = string.count(word)
#                         if count == num_x:
#                             if use != "x":
#                                 x.append(word)
#                             else:
#                                 y.append(word)
#         else:
#             if len(y) == 1:
#                 string = string.replace(y[0], "")
#                 pattern = pattern.replace("y", "")
#             else:
#                 for item in y:
#                     string = string.replace(y[0], "")
#                     pattern = pattern.replace("y", "")
#                     for letter in string:
#                         word += letter
#                         count = string.count(word)
#                         if count == total:
#                             if use != "x":
#                                 x.append(word)
#                             else:
#                                 y.append(word)
#         for items in y:
#             string = string.replace(items, "")
#             if string == "":
#                 y = items
#                 break
#
#         string = ""
#
#     if string == "":
#         return [x, y]













# def patternMatcher(pattern, string):
#     x = "empty"
#     y = "empty"
#     num_x = pattern.count("x")
#     num_y = pattern.count("y")
#     skip = False
#     if num_x == 0 or num_y == 0:
#         skip = True
#     first_pattern = pattern[0]
#     word = ""
#     if first_pattern == "x":
#         total = num_x
#     else:
#         total = num_y
#
#     #loop checker
#     for letter in string:
#         word += letter
#         count = match_section(word, string)
#         if count == total:
#             if first_pattern == "x":
#                 x = word
#                 break
#             else:
#                 y = word
#                 break
#     if skip:
#         answer = [x, y]
#         # print(answer)
#         return answer
#     if y == "empty":
#         total = num_y
#         used = "y"
#     else:
#         total = num_x
#         used = "x"
#     new_string = string.replace(word, "")
#     length = len(new_string)
#     length = int(length / total)
#     new_string = new_string[:length]
#     if used == "y":
#         y = new_string
#     else:
#         x = new_string
#     if x == "empty" or y == "empty":
#         return []
#     answer = [x, y]
#     # print(answer)
#     return answer



# def patternMatcher(pattern, string):
#     x = "empty"
#     y = "empty"
#     num_x = pattern.count("x")
#     num_y = pattern.count("y")
#     first_pattern = pattern[0]
#     word = ""
#     if first_pattern == "x":
#         total = num_x
#     else:
#         total = num_y
#     for letter in string:
#         word += letter
#         count = match_section(word, string)
#         if count == total:
#             if first_pattern == "x":
#                 x = word
#                 break
#             else:
#                 y = word
#                 break
#     if y == "empty":
#         total = num_y
#         used = "y"
#     else:
#         total = num_x
#         used = "x"
#     new_string = string.replace(word, "")
#     length =len(new_string)
#     length = int(length / total)
#     new_string = new_string[:length]
#     if used == "y":
#         y = new_string
#     else:
#         x = new_string
#
#     if x == "empty" or y == "empty":
#         return []
#     answer = [x, y]
#     print(x, y)
#     return answer






# def patternMatcher(pattern, string):
#     x = "empty"
#     y = "empty"
#     used = ""
#     xs = match_section("x", pattern)
#     ys = match_section("y", pattern)
#
#     if pattern[0] != pattern[1] and pattern[0] == pattern[2]:
#         if pattern[0] == "x":
#             used = "x"
#         else:
#             used = "y"
#         word = ""
#         first_letter = string[0]
#         for i2, letter2 in enumerate(string):
#             word += letter2
#             if letter2 == first_letter and i2 != 0:
#                 first_section = string[:i2]
#                 ending_section = string[i2:]
#                 word1 = ""
#                 if first_section[1] == ending_section[1]:
#                     for letter3 in first_section:
#                         word1 += letter3
#                         count = match_section(word1, string)
#                         if used == "x":
#                             check = xs
#                         else:
#                             check = ys
#                         if count == check:
#                             if pattern[0] == "x":
#                                 x = word1
#                                 break
#                             else:
#                                 y = word1
#                                 break
#         if used == "x":
#             replace = x
#         else:
#             replace = y
#         y_string = string.replace(replace, "")
#         for i1, letter1 in enumerate(y_string):
#             first_letter1 = y_string[0]
#             if letter1 == first_letter1 and i1 != 0:
#                 double_i1 = i1 * 2
#                 first_part1 = y_string[:i1]
#                 second_part1 = y_string[i1:double_i1]
#                 if first_part1 == second_part1:
#                     if used == "x":
#                         y = first_part1
#                         break
#                     else:
#                         x = first_part1
#                         break
#
#     if pattern[0] == pattern[1]:
#         for i, letter in enumerate(string):
#             first_letter = string[0]
#             if letter == first_letter and i != 0:
#                 double_i = i * 2
#                 first_part = string[:i]
#                 second_part = string[i:double_i]
#                 if first_part == second_part:
#                     if pattern[0] == "x":
#                         x = first_part
#                         used = "x"
#                         break
#                     else:
#                         y = first_part
#                         used = "y"
#                         break
#         y_string = string.replace(first_part, "")
#         for i1, letter1 in enumerate(y_string):
#             first_letter1 = y_string[0]
#             if letter1 == first_letter1 and i1 != 0:
#                 double_i1 = i1 * 2
#                 first_part1 = y_string[:i1]
#                 second_part1 = y_string[i1:double_i1]
#                 if first_part1 == second_part1:
#                     if used == "x":
#                         y = first_part1
#                         break
#                     else:
#                         x = first_part1
#                         break
#     print(x, y)
